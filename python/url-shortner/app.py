from aws_cdk import core as cdk
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_dynamodb as dynamodb

class UrlShortenerStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DynamoDB table for storing URLs
        table = dynamodb.Table(self, "UrlsTable",
            partition_key=dynamodb.Attribute(name="short_url", type=dynamodb.AttributeType.STRING)
        )

        # Lambda function for shortening URLs
        shortener_lambda = _lambda.Function(self, "UrlShortenerFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="shortener.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={"TABLE_NAME": table.table_name}
        )

        # Grant the Lambda function permissions to read/write to the DynamoDB table
        table.grant_read_write_data(shortener_lambda)

        # API Gateway to expose the Lambda function
        api = apigateway.LambdaRestApi(self, "UrlShortenerApi",
            handler=shortener_lambda,
            proxy=False
        )

        # Define routes for API Gateway
        shorten = api.root.add_resource("shorten")
        shorten.add_method("POST")  # for URL shortening

        redirect = api.root.add_resource("{short_url}")
        redirect.add_method("GET")  # for URL redirection

app = cdk.App()
UrlShortenerStack(app, "UrlShortenerStack")
app.synth()
