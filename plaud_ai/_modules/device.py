from plaud_ai.enum import HttpMethod

__all__ = ('DeviceAPI',)


class DeviceAPI:
    def __init__(self, client):
        self.client = client

    def list(self, token):
        path = 'devices'
        return self.client.make_request(HttpMethod.POST, path)

    def detail(self, device_id):
        """
        :param device_id:
        :return:
        """
        path = f'devices/{device_id}'
        return self.client.make_request(HttpMethod.GET, path)

    def bind(self, owner_id, device_type, serial_number):
        """
        Doc: https://docs.plaud.ai/documentation/developer_guides/tutorials/device_operations
        """
        path = 'devices/bind'
        data = {
            'owner_id': owner_id,
            'sn_type': device_type,
            'sn': serial_number,
        }
        return self.client.make_request(HttpMethod.POST, path, data)

    def unbind(self, owner_id, device_type, serial_number):
        """
        Doc: https://docs.plaud.ai/documentation/developer_guides/tutorials/device_operations#unbind-device
        """
        path = 'devices/unbind'
        data = {
            'owner_id': owner_id,
            'sn_type': device_type,
            'sn': serial_number,
        }
        return self.client.make_request(HttpMethod.POST, path, data)