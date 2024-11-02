#!/usr/bin/env python3
import os
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_ec2 as ec2

class SandboxVpc(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # Create a VPC with a CIDR block
        vpc = ec2.Vpc(self, "SandboxVpc",
            cidr="192.168.0.0/16",  # Correct parameter for CIDR
            max_azs=3  # Maximum Availability Zones
        )

app = cdk.App()
# Correcting the environment parameters
account = os.getenv('AWS_ACCOUNT_ID', '282526987325')
region = os.getenv('AWS_REGION', 'ap-south-1')

SandboxVpc(app, "Sandbox",
    env=cdk.Environment(account=account, region=region)
)
app.synth()
