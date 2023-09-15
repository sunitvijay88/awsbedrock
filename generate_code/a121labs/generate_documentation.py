import boto3
import json

# Function to generate code from documentation
def generate_code(prompt):
    
    prompt_data = f'{prompt}'

    bedrock = boto3.client(service_name='bedrock',region_name='us-east-1',endpoint_url='https://bedrock.us-east-1.amazonaws.com')
    bedrock.list_foundation_models()

    body = json.dumps({"prompt": prompt_data, "maxTokens": 2000, "temperature": 1, "topP": 1})
    modelId = 'ai21.j2-grande-instruct' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())

    python_code = response_body.get('completions')[0].get('data').get('text')

    return python_code

# Example documentation for python code generation
prompt = '''
write a python program to generate a synthetic regression dataset with 100 samples and 10 features.
The data should be generated from a linear model with Gaussian noise.
The first 5 features should be informative, the remaining 5 should be redundant.
The target y should be a linear function of the first 5 features.
The coefficients of the linear model should be random numbers between 0 and 1.
The noise should be drawn from a Gaussian distribution with mean 0 and standard deviation 0.5.
The random seed should be set to 0.
The data should be saved in a file called synthetic_regression.csv.
The first row of the file should contain the names of the features and the target.
The remaining rows should contain the data.
The file should be saved in the data folder, if necessary create the data folder.
'''

markdown_code = generate_code(prompt=prompt)
print("\n### generated code in Python  ###")
print(markdown_code)