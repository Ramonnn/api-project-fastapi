terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.3.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_instance" "fastapi_server" {
  ami           = "ami-090b049bea4780001"
  instance_type = "t2.micro"

  tags = {
    Name = "FastapiServer"
  }
}

output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.fastapi_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.fastapi_server.public_ip
}
