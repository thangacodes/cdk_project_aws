#!/bin/bash

echo "Importing AWS IAM user access/secret keys using bash script..."

# Prompt for AWS Access Key and Secret Access Key
read -p "Enter AWS_ACCESS_KEY value: " AWS_ACCESS_KEY
export AWS_ACCESS_KEY
read -p "Enter AWS_SECRET_ACCESS_KEY: " AWS_SECRET_ACCESS_KEY
export AWS_SECRET_ACCESS_KEY
read -p "Enter AWS_REGION: " AWS_REGION
export AWS_REGION
read -p "Enter the OUTPUT_FORMAT: " OUTPUT_FORMAT
export OUTPUT_FORMAT

# Check if the environment variables are set
if [[ -z "$AWS_ACCESS_KEY" || -z "$AWS_SECRET_ACCESS_KEY" ]]; then
    echo "Error: AWS_ACCESS_KEY and AWS_SECRET_ACCESS_KEY must be set."
    exit 1
fi

# Configure AWS CLI
aws configure set aws_access_key_id "$AWS_ACCESS_KEY"
aws configure set aws_secret_access_key "$AWS_SECRET_ACCESS_KEY"
aws configure set region "$AWS_REGION"
aws configure set output "$OUTPUT_FORMAT"

# List S3 buckets to verify configuration
aws s3 ls
exit 0
