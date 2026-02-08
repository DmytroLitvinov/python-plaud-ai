from plaud_ai.enum import HttpMethod

__all__ = ('FileAPI',)


class FileAPI:
    def __init__(self, client):
        self.client = client

    def generate_presigned_urls(self, data: dict):
        """
        Doc: https://docs.plaud.ai/api-reference/file:upload_s3/generate-presigned-urls
        """
        path = 'files/upload-s3/generate-presigned-urls'
        return self.client.make_request(HttpMethod.POST, path, data)

    def complete_upload(self, data: dict):
        """
        Doc: https://docs.plaud.ai/api-reference/file:upload_s3/complete-upload
        """
        path = 'files/upload-s3/complete-upload'
        return self.client.make_request(HttpMethod.POST, path, data)
