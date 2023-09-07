import boto3
import json

# Function to translate SAS code to Python
def generate_docstring(prompt, source_code):
    
    prompt_data = f'{prompt} :\n\n{source_code}\n\Converted code:'

    bedrock = boto3.client(service_name='bedrock',region_name='us-east-1',endpoint_url='https://bedrock.us-east-1.amazonaws.com')
    bedrock.list_foundation_models()

    body = json.dumps({"prompt": prompt_data, "max_tokens_to_sample": 5000})
    modelId = 'anthropic.claude-v2' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    
    python_code = response_body.get('completion')

    return python_code

# Example SAS code to translate
source_code = '''

def _multivariate_ols_fit(endog, exog, method='svd', tolerance=1e-8):
    y = endog
    x = exog
    nobs, k_endog = y.shape
    nobs1, k_exog= x.shape
    if nobs != nobs1:
        raise ValueError('x(n=%d) and y(n=%d) should have the same number of '
                         'rows!' % (nobs1, nobs))

    # Calculate the matrices necessary for hypotheses testing
    df_resid = nobs - k_exog
    if method == 'pinv':
        # Regression coefficients matrix
        pinv_x = pinv(x)
        params = pinv_x.dot(y)

        # inverse of x'x
        inv_cov = pinv_x.dot(pinv_x.T)
        if matrix_rank(inv_cov,tol=tolerance) < k_exog:
            raise ValueError('Covariance of x singular!')

        # Sums of squares and cross-products of residuals
        # Y'Y - (X * params)'B * params
        t = x.dot(params)
        sscpr = np.subtract(y.T.dot(y), t.T.dot(t))
        return (params, df_resid, inv_cov, sscpr)
    elif method == 'svd':
        u, s, v = svd(x, 0)
        if (s > tolerance).sum() < len(s):
            raise ValueError('Covariance of x singular!')
        invs = 1. / s

        params = v.T.dot(np.diag(invs)).dot(u.T).dot(y)
        inv_cov = v.T.dot(np.diag(np.power(invs, 2))).dot(v)
        t = np.diag(s).dot(v).dot(params)
        sscpr = np.subtract(y.T.dot(y), t.T.dot(t))
        return (params, df_resid, inv_cov, sscpr)
    else:
        raise ValueError('%s is not a supported method!' % method)
'''
prompt = '''
generate docstring following the PEP guidelines for below method written in Python.
'''
###
# Example multivariate_ols Python code
###

markdown_code = generate_docstring(prompt=prompt, source_code=source_code)
print("\n### generated docstring for Python code ###")
print(markdown_code)