# Plaud AI API client 📓

[![PyPI](https://img.shields.io/pypi/v/plaud-ai?style=flat-square)](https://pypi.python.org/pypi/plaud-ai/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/plaud-ai?style=flat-square)](https://pypi.python.org/pypi/plaud-ai/)
[![PyPI - License](https://img.shields.io/pypi/l/plaud-ai?style=flat-square)](https://pypi.python.org/pypi/plaud-ai/)

---
**Documentation**: [https://docs.plaud.ai/documentation/get_started/overview](https://docs.plaud.ai/documentation/get_started/overview)

**Source Code**: [https://github.com/DmytroLitvinov/python-plaud-ai](https://github.com/DmytroLitvinov/python-plaud-ai)

**PyPI**: [https://pypi.org/project/plaud-ai/](https://pypi.org/project/plaud-ai/)

---

Python API wrapper around Plaud AI API. Feel free to contribute and make it better! 🚀

## Installation

```sh
pip install plaud-ai
```

## Usage

1) Request creating APP for you via [Plaud API Survey](https://docs.google.com/forms/d/e/1FAIpQLSdndvVU1mcRGg_E7YURPEtB13R1zHs55T-234AC6STJyW1n8w/viewform) (taken link from [documentation](https://docs.plaud.ai/documentation/get_started/overview))


```python
# Example of using Plaud AI API to generate API token
from plaud_ai import PlaudAIAPIClient

client_id = 'xxxxxxxxxxxxxxx'
secret_key = 'yyyyyyyyyyyyyyy'

plaud_ai = PlaudAIAPIClient()
token_response = plaud_ai.api_token.generate_token(client_id, secret_key)
print(token_response.data, token_response.response_code)
api_token = token_response.data['api_token']

# Example of using Plaud AI API client to list devices
from plaud_ai import PlaudAIAPIClient

api_token = 'xxxxxxxxxxxxxxx'

plaud_ai = PlaudAIAPIClient(api_token)

devices_response = plaud_ai.devices_api.list()
print(devices_response.data, devices_response.response_code)
```

## Webhooks

```python
import json

from plaud_ai import is_valid_signature

payload_body = json.dumps(request.json).encode('utf-8')
signature_header = request.headers.get('Plaud-Signature')
webhook_secret = 'your_webhook_secret'

res = is_valid_signature(payload_body, signature_header, webhook_secret)
```

## License

This project is licensed under the terms of the [MIT license](https://github.com/DmytroLitvinov/python-plaud-ai/blob/main/LICENSE).


### HOW TO MAKE A RELEASE

* Add changes to `CHANGELOG.md`
* Change version in `plaud_ai/__init__.py` and `pyproject.toml`
* `source .venv/bin/activate`
* `python3 -m build --sdist --wheel`
* `twine upload dist/*`

Could be issues with `license-file` and other. Run next command to fix it:
* `pip install -U twine setuptools packaging build`
