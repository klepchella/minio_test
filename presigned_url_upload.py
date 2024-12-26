from datetime import timedelta

from minio import Minio


# The file to upload, change this path if needed
source_file = "./test_minio.txt"
# The destination bucket and filename on the MinIO server
bucket_name = "test"
destination_file = "test_minio.txt"


def put_presigned_url():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio("127.0.0.1:9000",
        access_key="bm2i4xRShkXJifonRNvU",
        secret_key="Tgcd4RNp0OXeRwQEd8jGia0kWkTqGiGScjklgGWc",
        secure=False,  # выключаем SSL; в проде, естественно, такого быть не должно
    )

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # генерируем подписанную ссылку на 10 минут
    # curl --location --request PUT 'http://127.0.0.1:9000/test/test_minio.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=bm2i4xRShkXJifonRNvU%2F20241226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241226T132201Z&X-Amz-Expires=600&X-Amz-SignedHeaders=host&X-Amz-Signature=2b0ed8767b7bb1048e40790047e8dc57ca8a08de6dd8d9ccffc603053bbe6327'
    presigned_url = client.presigned_put_object(
        bucket_name=bucket_name,
        object_name=destination_file,
        expires=timedelta(minutes=10))

    with open('./test_minio_2.json', 'rb') as data:
        obj = client.put_object(
            bucket_name=bucket_name,
            object_name='test_minio_2.json',
            data=data,
            length=74
        )
        print(f'obj = {obj}, checksum = {obj.etag}')

    print(
        presigned_url
    )

