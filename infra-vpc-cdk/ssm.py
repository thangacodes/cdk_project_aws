#!/usr/bin/env python3
import os
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_ssm as ssm

class SandboxSSM(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # Create an SSM Parameter
        parameter = ssm.StringParameter(self, "SandboxSSMParameter",
            parameter_name="SandboxSSM-Parameter",
            string_value="DevOps12346!@"
        )
app = cdk.App()
# Correcting the environment parameters
account = os.getenv('AWS_ACCOUNT_ID', '282526987325')
region = os.getenv('AWS_REGION', 'ap-south-1')

SandboxSSM(app, "Sandbox",
    env=cdk.Environment(account=account, region=region)
)
app.synth()
