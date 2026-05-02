import boto3

dynamodb = boto3.client("dynamodb")


def lambda_handler(event, context):
    print(event)
    id = event["queryStringParameters"]["id"]
    firstname = event["queryStringParameters"]["firstname"]
    lastname = event["queryStringParameters"]["lastname"]

    ####
    # Challenge: put the customer id, firstname, last name into the dynamo db table
    ####
    put_response = dynamodb.put_item(
        TableName="LabCustomers",
        Item={
            "ID": {"S": id},
            "Firstname": {"S": firstname},
            "Lastname": {"S": lastname},
        },
    )

    return {"result": "Saved"}
