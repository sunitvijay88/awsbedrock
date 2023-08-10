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

api_example(prompt_data ="""\"convert below code written in SAS to python. data \\n\\nmacro generate_regression_models(input_files);\\n\\n   %local i;  %do i = 1 %to %sysfunc(countw(&input_files));\\n\\n    %let input_file = %scan(&input_files, &i);\\n\\n     data mydata;      infile \\\"&input_file\\\" dlm=',' firstobs=2;      input x y;    run;    proc reg data=mydata outest=outest&i;      model y = x;    run;    %put Linear regression model for &input_file has been generated;  %end;  %put All regression models have been generated successfully;%mend;\\n\\n%generate_regression_models(input_files = \\\"path/to/file1.csv path/to/file2.csv path/to/file3.csv\\\");\\n \\n\\n```\\nimport glob\\nimport pandas as pd\\nimport statsmodels.api as sm\\n\\ndef generate_regression_models(input_files):\\n    for i, input_file in enumerate(glob.glob(input_files)):\\n        df = pd.read_csv(input_file, header=None, names=['x', 'y'], skiprows=1)\\n        y = df['y']\\n        x = df['x']\\n        model = sm.GLM(y, x, family=sm.families.Gaussian())\\n        results = model.fit()\\n        print(f'Linear regression model for {input_file} has been generated')\\n        print(results.summary())\\n    print('All regression models have been generated successfully')\\n\\ngenerate_regression_models(input_files='path/to/file1.csv path\\n \"""")