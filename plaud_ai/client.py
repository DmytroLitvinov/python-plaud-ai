import logging
from urllib.parse import urljoin

import requests

from plaud_ai import __version__
from plaud_ai._modules import (
    DeviceAPI,
    FileAPI,
    OAuthTokenAPI,
    WorkflowAPI,
)
from plaud_ai.enum import HttpMethod
from plaud_ai.response import PlaudAIAPIResponse

logger = logging.getLogger('plaud_ai')


class PlaudAIAPIClient:
    DEFAULT_HEADERS = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': f'python-plaud-ai/{__version__} | (https://github.com/DmytroLitvinov/python-plaud-ai)',
    }

    def __init__(self, api_token: str = ''):
        self.api_token = api_token
        self.base_url = 'https://platform.plaud.ai'
        self.prefix = f'api/'
        self.endpoint = urljoin(self.base_url, self.prefix)

        self._modules = {}

        # Modules
        self.api_token = self._get_module(OAuthTokenAPI)
        self.devices_api = self._get_module(DeviceAPI)
        self.files_api = self._get_module(FileAPI)
        self.workflows_api = self._get_module(WorkflowAPI)

    def _get_headers(self):
        headers = self.DEFAULT_HEADERS.copy()
        headers.update({'Authorization': f'Bearer {self.api_token}'})
        return headers

    def _get_module(self, cls):
        if cls not in self._modules:
            self._modules[cls] = cls(self)
        return self._modules[cls]

    def make_request(
        self,
        method: HttpMethod,
        path: str,
        body: dict | None = None,
        headers: dict | None = None,
    ) -> PlaudAIAPIResponse:
        """
        :param method: HTTP method
        :param path: Api path
        :param body: body of request
        :param headers: override headers for request
        :return: Serialized server response or error
        """
        url = urljoin(self.endpoint, path)
        if headers is None:
            headers = self._get_headers()
        else:
            merged_headers = self.DEFAULT_HEADERS.copy()
            merged_headers.update(headers)
            headers = merged_headers
        body = body or {}

        logger.debug(f'Making {method.value} request to {url} with headers {headers} and body {body}')
        # https://github.com/psf/requests/issues/3070
        response = requests.request(method.value, url, headers=headers, json=body, timeout=10)
        logger.debug(f'Received response with status code {response.status_code} and body {response.text}')

        return PlaudAIAPIResponse(response.json(), response.status_code)
