import boto3
import json

# Function to translate SAS code to Python
def translate_sas_to_python(sas_code):
    
    prompt_data = f'Human: convert below SAS code to Python :\n\n{sas_code}\n\nPython code:'

    bedrock = boto3.client(service_name='bedrock',region_name='us-east-1',endpoint_url='https://bedrock.us-east-1.amazonaws.com')
    bedrock.list_foundation_models()

    body = json.dumps({"prompt": prompt_data, "max_tokens_to_sample": 5000})
    modelId = 'anthropic.claude-instant-v1' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    
    python_code = response_body.get('completion')
    print(python_code)
    return python_code

# Example SAS code to translate
sas_code = '''
data reformatted_data;
   infile 'your_file_path';
   input var1 var2 var3 var4 var5;

   /* Convert selected variables to strings */
   var1 = put(var1, $CHAR.);
   var2 = put(var2, $CHAR.);
   var3 = put(var3, $CHAR.);

   /* Keep var4 and var5 as numeric */

   /* Output the reformatted data */
   output;
run;
'''

###
# Example SAS code to translate
###

python_code = translate_sas_to_python(sas_code)
print("\n### generated simple SAS Code ###")
print(python_code)