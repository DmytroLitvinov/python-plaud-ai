import base64

from plaud_ai.enum import HttpMethod

__all__ = ('OAuthTokenAPI',)


class OAuthTokenAPI:
    PATH = 'oauth/api-token'

    def __init__(self, client):
        self.client = client

    def generate_token(self, client_id, secret_key):
        path = self.PATH
        credentials = base64.b64encode(f'{client_id}:{secret_key}'.encode()).decode()
        headers = {
            'Authorization': f'Bearer {credentials}',
        }
        return self.client.make_request(HttpMethod.POST, path, headers=headers)
