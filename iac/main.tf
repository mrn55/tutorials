provider "aws" {
  region = "us-west-2"
}

variable "instance_count" {
  default = 4
}

variable "instance_type" {
  default = "t2.nano" # practice on the cheap yo
}

resource "aws_key_pair" "key" {
  key_name   = "k8s-key"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_security_group" "k8s_sg" {
  name        = "k8s-security-group"
  description = "Allow SSH and Kubernetes ports"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 6443
    to_port     = 6443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 10250
    to_port     = 10255
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "k8s_instances" {
  count         = var.instance_count
  ami           = "ami-07c5ecd8498c59db5" # eventually use would probaly be a variable/custom AMI
  instance_type = var.instance_type
  key_name      = aws_key_pair.key.key_name
  security_groups = [aws_security_group.k8s_sg.name]

  tags = {
    Name = "k8s-node-${count.index}"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_ip} >> ip_addresses.txt"
  }
}

output "instance_ips" {
  value = aws_instance.k8s_instances[*].public_ip
}
