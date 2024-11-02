import boto3
import hashlib
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        return shorten_url(event)
    elif event['httpMethod'] == 'GET':
        return get_original_url(event)

def shorten_url(event):
    body = event['body']
    original_url = body['url']

    url_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]

    return {
        'statusCode': 200,
        'body': f"https://{event['headers']['Host']}/{url_hash}"
    }

def get_original_url(event):
    short_url = event['pathParameters']['short_url']
    response = table.get_item(Key={'short_url': short_url})

    if 'Item' in response:
        original_url = response['Item']['original_url']
        return {
            'statusCode': 301,
            'headers': {'Location': original_url}
        }
    else:
        return {
            'statusCode': 404,
            'body': f"No URL found for short url '{short_url}'."}
    