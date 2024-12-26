from minio import S3Error
from minio_client import test_minio
from presigned_url_download import get_presigned_url
from presigned_url_upload import put_presigned_url

if __name__ == "__main__":
    try:
        # upload_file()
        get_presigned_url()
        put_presigned_url()
    except S3Error as exc:
        print("error occurred.", exc)