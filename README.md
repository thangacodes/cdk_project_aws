# cdk_project:
==============

What is AWS CDK (Cloud Development Kit)?

AWS CDK (Cloud Development Kit) is an open-source software development framework that allows you to define cloud infrastructure using familiar programming languages like TypeScript, JavaScript, Python, Java, and C#. With AWS CDK, you can model your cloud resources as code and deploy them using AWS CloudFormation.

Coming to the project repo,

This project repository contains the AWS Cloud Development Kit (AWS CDK) and includes an Ansible playbook that sets up a local environment. 

It initializes a custom CDK project, creates necessary folders, and activates a virtual environment, among other tasks.

Before you begin the CDK deployment, you need to set up AWS credentials on the system where you are performing the deployment.

```bash
# Go to the ansible_script folder.
$ cd ansible_script
Execute the command sh aws-credential-setup.sh
$ sh aws-credential-setup.sh

# Note:
This is a bash script that will prompt you to enter your IAM credentials, such as your access key, secret access key, region, and output format. 
It will then load the .bashrc file, from which it will retrieve the required API information to connect to your AWS account.

To initialize the project, navigate to the ansible_script folder and follow the procedure below:
$ cd ansible_script
$ ansible-playbook init_cdk_project.yaml

# Outcome should be,
Our aim is to create a VPC with three private and public subnets, along with the required components such as an Internet Gateway, NAT Gateway, and route tables for both the private and public subnets.

VPC Stack name is "SandboxVpc"

The following CDK commands will be called and executed as well.

$ cdk ls          //list all stacks in the app
$ cdk synth      //emits the synthesized CloudFormation template
$ cdk deploy    //deploy this stack to your default AWS account/region
$ cdk diff     //compare deployed stack with current state
$ cdk docs    //open CDK documentation
