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

api_example(prompt_data ="""\"Human: convert below SAS code to Python.\\n\\nmacro generate_regression_models(input_files);\\n  %local i;\\n\\n  %do i = 1 %to %sysfunc(countw(&input_files));\\n    %let input_file = %scan(&input_files, &i);\\n\\n    data mydata;\\n      infile \\\"&input_file\\\" dlm=',' firstobs=2;\\n      input x y;\\n    run;\\n\\n    proc reg data=mydata outest=outest&i;\\n      model y = x;\\n    run;\\n\\n    %put Linear regression model for &input_file has been generated;\\n  %end;\\n\\n  %put All regression models have been generated successfully;\\n%mend;\\n\\n%generate_regression_models(input_files = \\\"path/to/file1.csv path/to/file2.csv path/to/file3.csv\\\");""")