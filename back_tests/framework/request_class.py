import logging
import os

import requests
import json

logger = logging.getLogger("REST_API_TESTS")


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
        self.base_url = os.environ["URL_API"]
        self.response = None
        self.errors = None
        self.response_code = None

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        return response.json()

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response.json()

    def put(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        response = requests.put(url, data=json.dumps(data), headers=headers)
        return response.json()

    def post_graphql(self, payload):
        """
        Perform a POST request to the internal API
        """
        logger.info(f"Data: {json.dumps(payload)}")
        response = requests.post(
            url=self.base_url,
            data=json.dumps(payload),
            verify=False,
            headers={"Content-Type": "application/json"},
        )
        logger.info(f"URL: {self.base_url}")
        logger.info(f"{response.status_code} {response.reason}, {response.text}")

        self.response_code = response.status_code
        self.response = response.json().get("data", None)
        self.errors = response.json().get("errors", None)


backend_request_api = RestClientAPI.get_instance()
