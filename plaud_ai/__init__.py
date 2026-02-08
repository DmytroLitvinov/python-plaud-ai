"""Top-level package for Plaud AI API wrapper."""

__author__ = 'Dmytro Litvinov'
__email__ = 'me@dmytrolitvinov.com'
__version__ = '0.1.0'

from .client import PlaudAIAPIClient
from .webhook import verify_signature
