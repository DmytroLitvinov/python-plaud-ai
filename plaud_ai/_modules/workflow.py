from plaud_ai.enum import HttpMethod

__all__ = ('WorkflowAPI',)


class WorkflowAPI:

    def __init__(self, client):
        self.client = client

    def get_result(self, workflow_id):
        """
        Doc: https://docs.plaud.ai/api-reference/workflow/get-workflow-result
        """
        path = f'workflows/{workflow_id}/result'
        return self.client.make_request(HttpMethod.GET, path)

    def get_status(self, workflow_id):
        """
        Doc: https://docs.plaud.ai/api-reference/workflow/get-workflow-status
        """
        path = f'workflows/{workflow_id}/status'
        return self.client.make_request(HttpMethod.GET, path)

    def submit(self, data: dict):
        """
        Doc: https://docs.plaud.ai/api-reference/workflow/submit-workflow
        """
        path = 'workflows/submit'
        return self.client.make_request(HttpMethod.POST, path, data)
