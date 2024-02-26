import logging
import os
from dotenv import load_dotenv
import requests
import json

logger = logging.getLogger("REST_API_TESTS")

load_dotenv(".env/local.env")


class RestClientAPI:
    instance = None

    @classmethod
    def get_instance(cls):
        """This method
        :return: class instance
        """
        if cls.instance is None:
            cls.instance = RestClientAPI()
        return cls.instance

    def __init__(self):
        self.base_url = os.environ["API_BASE_URL"]
        self.access_token = os.environ["ACCESS_TOKEN"]

    def get(self, endpoint, user_id=None):
        url = f"{self.base_url}/{endpoint}{user_id}"

        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.access_token}"}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response.json()

    def put(self, endpoint, user_id=None, data=None):
        url = f"{self.base_url}/{endpoint}{user_id}/"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.access_token}"}
        response = requests.put(url, data=json.dumps(data), headers=headers)
        return response.json()

    def patch(self, endpoint, user_id=None, data=None):
        url = f"{self.base_url}/{endpoint}{user_id}/"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.access_token}"}
        response = requests.patch(url, data=json.dumps(data), headers=headers)
        return response.json()

    def delete(self, endpoint, user_id=None):
        url = f"{self.base_url}/{endpoint}{user_id}/"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.access_token}"}
        response = requests.delete(url, headers=headers)
        return response.status_code

    def graphql_post(self, endpoint, query, variables=None):
        url = f"{self.base_url}/graphql/{endpoint}"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.access_token}"}
        data = {"query": query, "variables": variables}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response.json()


BACKEND_REQUEST_API = RestClientAPI.get_instance()
