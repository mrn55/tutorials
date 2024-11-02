# RabbitMQ Cluster on MiniKube

I used the instructions outlined here: https://www.rabbitmq.com/kubernetes/operator/quickstart-operator

1. Install the RabbitMQ Cluster Operator

```
kubectl apply -f "https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml"
```

2. Check for CRD

```
kubectl get customresourcedefinitions.apiextensions.k8s.io
```

3. Launch a simple cluster using crd

```
kubectl apply -f https://raw.githubusercontent.com/rabbitmq/cluster-operator/main/docs/examples/hello-world/rabbitmq.yaml
```

4. Wait for it come up, check logs

```
kubectl logs hello-world-server-0
```

5. Here is where I ran into some issues, mainly with Windows. Probably could be fixed by installing base64 and updating the envrionment variable assignment. But what I did works, first get the username and password, then use something like this (https://www.base64decode.org/) to convert it from base 64 to plain.

```
kubectl get secret hello-world-default-user -o jsonpath='{.data.username}'
kubectl get secret hello-world-default-user -o jsonpath='{.data.password}'
```

6. Once I had that, I was able to forward 15672 port and connect to it using the username/password.

```
kubectl port-forward "service/hello-world" 15672
```

Open 15672 in a browser; you should be presented with the Raabitmq management console.
