This project is about research AWS Bedrock service.

This project is using AWS Cloud 9 and AWS Bedrock Service. 


For prerequisites for api_code_to_convert, see the README in the folder.

Setup AWS managed temporary credentials to connect to AWS services. 

Install the packages required by running the following in a virtual environment:

python -m pip install -r requirements.txt

Install Bedrock Python SDK by running the following in a virtual environment:

python3 -m pip install ./boto3-1.26.162-py3-none-any.whl
python3 -m pip install ./botocore-1.29.162-py3-none-any.whl