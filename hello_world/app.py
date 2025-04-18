# import json

# # import requests


# def lambda_handler(event, context):
#     """Sample pure Lambda function

#     Parameters
#     ----------
#     event: dict, required
#         API Gateway Lambda Proxy Input Format

#         Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

#     context: object, required
#         Lambda Context runtime methods and attributes

#         Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

#     Returns
#     ------
#     API Gateway Lambda Proxy Output Format: dict

#         Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
#     """

#     # try:
#     #     ip = requests.get("http://checkip.amazonaws.com/")
#     # except requests.RequestException as e:
#     #     # Send some context about this error to Lambda Logs
#     #     print(e)

#     #     raise e

#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             "message": "hello world again 10.0",
#             # "location": ip.text.replace("\n", "")
#         }),
#     }


import json
import numpy as np  # Make sure numpy is installed in your Lambda package

def lambda_handler(event, context):
    """
    Lambda function that uses NumPy to perform a simple calculation.
    """

    # Example: Matrix multiplication using NumPy
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    result = np.matmul(matrix_a, matrix_b)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Matrix multiplication result",
            "result": result.tolist()  # Convert NumPy array to list for JSON serialization
        }),
    }
