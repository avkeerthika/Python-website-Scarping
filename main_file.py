import boto3
from bucket_list import bucketList, deleteBucket, emptyBucket
from website_scarping import hosting_website, web_content
s3 = boto3.client('s3')

def static_hosting(Bucket):
    avail_bucks = bucketList()
    existing_bucks = False
    for data in avail_bucks:
        print(data)
        available_name = data['Name']
        if available_name  == Bucket:
            existing_bucks = True
    if existing_bucks:
        emptyBucket(Bucket)
        deleteBucket(Bucket)
    web_content()
    hosting_website(Bucket)
    print('Success!')
static_hosting("url-buck-01")