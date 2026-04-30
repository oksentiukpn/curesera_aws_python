import boto3

dynamodb = boto3.client("dynamodb")

put_response = dynamodb.put_item(
    TableName="ZipcodeWeather",
    Item={
        "zipcode": {"S": "94105"},
        "temperature": {"N": "72"},
        "humidity": {"N": "60"},
        "wind_speed": {"N": "5"},
    },
)

scan_response = dynamodb.scan(TableName="ZipcodeWeather")
print("Scan Response:", scan_response)


query_response = dynamodb.query(
    TableName="ZipcodeWeather",
    KeyConditionExpression="zipcode = :zip",
    ExpressionAttributeValues={":zip": {"S": "94105"}},
)
print("Query Response:", query_response)
