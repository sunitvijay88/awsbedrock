import boto3
    
import json

def api_example(prompt_data):
 
    bedrock = boto3.client(service_name='bedrock',region_name='us-east-1',endpoint_url='https://bedrock.us-east-1.amazonaws.com')
    bedrock.list_foundation_models()

    body = json.dumps({"prompt": prompt_data, "max_tokens_to_sample": 5000})
    modelId = 'anthropic.claude-instant-v1' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())

    print(response_body.get('completion'))

api_example(prompt_data ="""\"Human: convert below SAS code to Python.\\n\\ndata reformatted_data;\\n   infile 'your_file_path';\\n   input var1 var2 var3 var4 var5;\\n\\n   /* Convert selected variables to strings */\\n   var1 = put(var1, $CHAR.);\\n   var2 = put(var2, $CHAR.);\\n   var3 = put(var3, $CHAR.);\\n\\n   /* Keep var4 and var5 as numeric */\\n\\n   /* Output the reformatted data */\\n   output;\\nrun;""")