import boto3
    
import json

def api_example(prompt_data):
 
    bedrock = boto3.client(service_name='bedrock',region_name='us-east-1',endpoint_url='https://bedrock.us-east-1.amazonaws.com')
    bedrock.list_foundation_models()

    body = json.dumps({"inputText": prompt_data, "textGenerationConfig":{ "maxTokenCount":4096, "temperature": 0, "topP": 1}})
    modelId = 'amazon.titan-tg1-large' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())

    print(response_body.get('results')[0].get('outputText'))  

api_example(prompt_data ="""\"convert below code written in SAS to python. data data reformatted_data;\\n\\n   infile 'your_file_path';\\n\\n    input var1 var2 var3 var4 var5;\\n\\n   /* Convert selected variables to strings */\\n\\n    var1 = put(var1, $CHAR.);   var2 = put(var2, $CHAR.);   var3 = put(var3, $CHAR.);\\n\\n   /* Keep var4 and var5 as numeric */\\n   /* Output the reformatted data */\\n\\n    output;run;\\n\\n\\n```\\nimport pandas as pd\\n\\n# Read in the data\\ndf = pd.read_csv('your_file_path')\\n\\n# Convert selected variables to strings\\ndf['var1'] = df['var1'].astype(str)\\ndf['var2'] = df['var2'].astype(str)\\ndf['var3'] = df['var3'].astype(str)\\n\\n# Keep var4 and var5 as numeric\\n\\n# Output the reformatted data\\ndf.to_csv('reformatted_data.csv', index=False)\\n\\n```\\n\\n Note that this code assumes that the data in your file is comma-separated and that you have pandas installed.\"""")

