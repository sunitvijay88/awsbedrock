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

api_example(prompt_data ="""\"convert below SAS code to Python. \\n\\ndata Setosa;\\n  input SepalLength SepalWidth PetalLength PetalWidth @@;\\n  label sepallength='Sepal Length in mm.'\\n        sepalwidth='Sepal Width in mm.'\\n        petallength='Petal Length in mm.'\\n        petalwidth='Petal Width in mm.';\\n  datalines;\\n50 33 14 02  46 34 14 03  46 36 .  02\\n51 33 17 05  55 35 13 02  48 31 16 02\\n52 34 14 02  49 36 14 01  44 32 13 02\\n50 35 16 06  44 30 13 02  47 32 16 02\\n48 30 14 03  51 38 16 02  48 34 19 02\\n50 30 16 02  50 32 12 02  43 30 11 .\\n58 40 12 02  51 38 19 04  49 30 14 02\\n51 35 14 02  50 34 16 04  46 32 14 02\\n57 44 15 04  50 36 14 02  54 34 15 04\\n52 41 15 .   55 42 14 02  49 31 15 02\\n54 39 17 04  50 34 15 02  44 29 14 02\\n47 32 13 02  46 31 15 02  51 34 15 02\\n50 35 13 03  49 31 15 01  54 37 15 02\\n54 39 13 04  51 35 14 03  48 34 16 02\\n48 30 14 01  45 23 13 03  57 38 17 03\\n51 38 15 03  54 34 17 02  51 37 15 04\\n52 35 15 02  53 37 15 02\\n;\\n\\nods graphics on;\\ntitle 'Fisher (1936) Iris Setosa Data';\\nproc corr data=Setosa sscp cov plots=matrix;\\n   var  sepallength sepalwidth;\\n   with petallength petalwidth;\\nrun;\"""")

