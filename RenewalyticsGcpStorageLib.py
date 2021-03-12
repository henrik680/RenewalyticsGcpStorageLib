from google.cloud import storage
from google.cloud.storage import Blob
import logging


def upload_blob_string(bucket_name, data_string, destination_blob_name, metadata, content_type):
    logging.debug('get_storage_metadata(...) \n\tbucket_name={}\n\tlen data_string={}\n\t'
                  'destination_blob_name={}\n\tmetadata={}\n\tcontent_type={}'
                  .format(bucket_name, len(data_string), destination_blob_name, metadata, content_type))
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = Blob(destination_blob_name, bucket)
    if blob.metadata is None:
        blob.metadata = metadata
    else:
        blob.metadata.update(metadata)
    return blob.upload_from_string(
        data=data_string,
        content_type=content_type)