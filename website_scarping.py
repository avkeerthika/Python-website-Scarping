import boto3
import requests
s3 = boto3.client("s3")  
url= input("Enter your url: ")
def web_content():
    response = requests.get(url)
    data=response.text
    with open("index.html", 'w', encoding='utf-8') as file:
            file.write(data)

def hosting_website(Bucket):
        response = s3.create_bucket(
            Bucket=Bucket,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            },
            ObjectLockEnabledForBucket=False,
            ObjectOwnership='BucketOwnerPreferred',
        )
     
        response = s3.put_public_access_block(
            Bucket=Bucket,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )

        response = s3.put_bucket_acl(
            Bucket=Bucket,
            ACL='public-read'
        )       
        
        response = s3.put_bucket_website(
            Bucket=Bucket,
            WebsiteConfiguration={
                'IndexDocument': {
                    'Suffix': 'index.html'  
                },
                'ErrorDocument': {
                    'Key': 'error.html' 
                }
            }
        )
        
        filename = ['index.html']
        for file in filename:
                data = open(file, "r", encoding="utf8").read()
                response = s3.put_object(
                         ACL='public-read',
                         Body=data,
                         Bucket=Bucket,
                         Key="index.html",
                         ContentType='text/html' )
        #response = s3.upload_file('D:\task\MiniProject\website_scarping.py', Bucket, 'index.html')       
        print(response)  
