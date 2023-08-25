import boto3
import json

# Function to translate SAS code to Python
def translate_sas_to_python(sas_code):
    
    prompt_data = f'convert below SAS code to Python :\n\n{sas_code}\n\nPython code:'

    bedrock = boto3.client(service_name='bedrock',region_name='us-east-1',endpoint_url='https://bedrock.us-east-1.amazonaws.com')
    bedrock.list_foundation_models()

    body = json.dumps({"inputText": prompt_data, "textGenerationConfig":{ "maxTokenCount":4096, "temperature": 1, "topP": 1}})
    modelId = 'amazon.titan-tg1-large' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())

    python_code = response_body.get('results')[0].get('outputText') 

    print(python_code)
    return python_code

# Example SAS code to translate
sas_code = '''
macro generate_regression_models(input_files);
  %local i;

  %do i = 1 %to %sysfunc(countw(&input_files));
    %let input_file = %scan(&input_files, &i);

    data mydata;
      infile "&input_file" dlm=',' firstobs=2;
      input x y;
    run;

    proc reg data=mydata outest=outest&i;
      model y = x;
    run;

    %put Linear regression model for &input_file has been generated;
  %end;

  %put All regression models have been generated successfully;
%mend;

%generate_regression_models(input_files = "path/to/file1.csv path/to/file2.csv path/to/file3.csv");
'''

###
# Example SAS code to translate
###

python_code = translate_sas_to_python(sas_code)
print("\n### generated simple SAS Code ###")
print(python_code)