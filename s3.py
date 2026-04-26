import boto3

client = boto3.client("s3")

response = client.list_buckets()
print("Existing buckets:")
for b in response["Buckets"]:
    print(f"    {b['Name']}")

# response = client.create_bucket(
#     Bucket="myoksesaneka22testbucket",
#     ACL="private",
#     CreateBucketConfiguration={"LocationConstraint": "eu-north-1"},
# )

put_response = client.put_object(
    Bucket="myoksesaneka22testbucket", Key="test.txt", Body="Hello world"
)
