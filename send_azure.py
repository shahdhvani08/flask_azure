from azure.storage.blob import BlockBlobService

from os import listdir

from os.path import isfile, join

# Setting Parameters

ACCOUNT_NAME = "testflask"

ACCOUNT_KEY = "k1a+p1xuG0v7GEHfodtZl/vMXQSv6sS1M2fX+FXrpH11HP3lvd3bt1Q+ClXpKAafdyF7gPA30pu3qyxge2A34g=="

CONTAINER_NAME = "mycontainer"

LOCAL_DIRECT = r"E:\4 SIH 2018\test_api\new-test"

# Code block to upload blob to Blob storage

blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)

local_file_list = [f for f in listdir(LOCAL_DIRECT) if isfile(join(LOCAL_DIRECT, f))]

file_num = len(local_file_list)

for i in range(file_num):

    local_file = join(LOCAL_DIRECT, local_file_list[i])

    blob_name = local_file_list[i]

    try:

        blob_service.create_blob_from_path(CONTAINER_NAME, blob_name, local_file)

        print("File upload successful %s"%blob_name)

    except:

        print ("Something went wrong while uploading the files %s"%blob_name)
