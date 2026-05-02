import boto3

dynamodb = boto3.client("dynamodb")


def lambda_handler(event, context):
    query_response = dynamodb.scan(TableName="LabCustomers")

    lists = [
        [item["ID"]["S"], item["Firstname"]["S"], item["Lastname"]["S"]]
        for item in query_response["Items"]
    ]

    return {"result": lists}
