from datetime import datetime, timedelta
from gc import get_objects

from minio import Minio

# The file to upload, change this path if needed
source_file = "./image.png"
# The destination bucket and filename on the MinIO server
bucket_name = "test"
destination_file = "image.png"


def get_presigned_url():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio("127.0.0.1:9000",
        access_key="bm2i4xRShkXJifonRNvU",
        secret_key="Tgcd4RNp0OXeRwQEd8jGia0kWkTqGiGScjklgGWc",
        secure=False,
    )

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # генерируем подписанную ссылку на 10 минут
    presigned_url = client.get_presigned_url(
        "GET",
        bucket_name=bucket_name,
        object_name=destination_file,
        expires=timedelta(minutes=10))

    get_object = client.presigned_get_object(
        bucket_name=bucket_name,
        object_name=destination_file,
        expires=timedelta(minutes=10)
    )


    print(
        presigned_url,
        get_object
    )

