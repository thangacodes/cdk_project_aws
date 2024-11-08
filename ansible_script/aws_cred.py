import os
import subprocess

def configure_aws():
    print("Importing AWS IAM user access/secret keys using Python script...")

    # Prompt for AWS Access Key and Secret Access Key
    aws_access_key = input("Enter AWS_ACCESS_KEY: ")
    aws_secret_access_key = input("Enter AWS_SECRET_ACCESS_KEY: ")
    aws_region = input("Enter AWS_REGION: ")
    output_format = input("Enter the OUTPUT_FORMAT: ")

    # Check if the access keys are provided
    if not aws_access_key or not aws_secret_access_key:
        print("Error: AWS_ACCESS_KEY and AWS_SECRET_ACCESS_KEY must be set.")
        exit(1)

    # Set environment variables (optional if you prefer to set them directly in the script)
    os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key
    os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key
    os.environ["AWS_REGION"] = aws_region
    os.environ["AWS_DEFAULT_OUTPUT"] = output_format

    # Configure AWS CLI using subprocess to run aws configure commands
    subprocess.run(["aws", "configure", "set", "aws_access_key_id", aws_access_key])
    subprocess.run(["aws", "configure", "set", "aws_secret_access_key", aws_secret_access_key])
    subprocess.run(["aws", "configure", "set", "region", aws_region])
    subprocess.run(["aws", "configure", "set", "output", output_format])

    # List S3 buckets to verify configuration
    try:
        subprocess.run(["aws", "s3", "ls"], check=True)
        print("AWS CLI configuration is successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing AWS CLI command: {e}")

if __name__ == "__main__":
    configure_aws()
