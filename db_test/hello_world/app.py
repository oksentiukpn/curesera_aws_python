import json
from os import environ

import boto3
import pymysql
from dotenv import load_dotenv

load_dotenv(override=True)

HOSTNAME = environ.get("DB_HOSTNAME", environ.get("HOSTNAME"))
USERNAME = environ.get("DB_USERNAME", environ.get("USERNAME"))
PASSWORD = environ.get("DB_PASSWORD", environ.get("PASSWORD"))


def get_db_connection():
    connection = pymysql.connect(
        host=HOSTNAME,
        user=USERNAME,
        password=PASSWORD,
        database="mydb",
    )
    return connection


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    connection = get_db_connection()

    query = "SELECT * FROM users"
    cursor = connection.cursor()
    cursor.execute(query)

    results = cursor.fetchall()

    return {
        "statusCode": 200,
        "body": json.dumps(results),
    }


if __name__ == "__main__":
    print(lambda_handler({}, {}))
