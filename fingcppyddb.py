import boto3
ddb = boto3.client("dynamodb")

def handler(request):
    try:
        data = ddb.scan(
            TableName="testhistory"
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return "Successfully executed"
