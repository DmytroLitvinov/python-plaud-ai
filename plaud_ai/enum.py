from enum import Enum


class HttpMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

class DeviceType(Enum):
    # Taken from https://docs.plaud.ai/documentation/developer_guides/tutorials/device_operations
    NOTE = 'note'
    NOTE_PIN = 'notepin'
    NOTE_PRO = 'notepro'