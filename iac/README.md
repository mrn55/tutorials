Here we use Terraform to provision a simple Kubernetes cluster on AWS and Ansible to configure it. Here’s a brief overview of the process:

## Terraform (Infrastructure Provisioning)

- Creates 4 EC2 instances on AWS: 1 control plane (master) node and 3 worker nodes, all with the nano instance type.
- Sets up a security group to allow SSH access (port 22) and Kubernetes communication ports.
- Generates an SSH key pair for secure access and outputs the public IP addresses of the instances for use by Ansible.

1. Run `terraform init` to initialize Terraform
2. Run `terraform apply` to create the infrastructure
3. Run `terraform destroy` to tear down the infrastructure

I'm using my personal AWS account, so you'll need to set up a new one and configure your credentials in `~/.aws/credentials`. You'll also want to make sure that you have an SSH key pair available for use by Terraform. If you don't already have one, you can generate one with `ssh-keygen -t rsa`.

## Ansible (Configuration and Deployment)

### !!!WIP!!!

This is not complety working, but it's a good start.

- Installs Docker and Kubernetes tools (kubelet, kubeadm, and kubectl) on all nodes.
- Initializes the control plane (master) node using kubeadm init, which sets up the Kubernetes API server and necessary components.
- Applies a network plugin (Calico) on the control plane to allow network communication between pods.
- Retrieves the join command from the control plane and uses it on each worker node to join them to the Kubernetes cluster.

After running this, you’ll have a basic Kubernetes cluster with 1 control plane and 3 worker nodes, ready for containerized applications.

## Coming soon, remote terrafom state

I'll use AWS S3 buckets as a remote state backend. This will allow me to store the terraform state remotely in S3, which is more secure than storing it locally on my laptop. Also will use dynamodb for locking. (the plan anyway)
