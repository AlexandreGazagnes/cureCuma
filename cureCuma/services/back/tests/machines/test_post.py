import os

import pytest
import json
import requests


class TestMAchinePost:
    """Test Machine Get """

    URL = "http://0.0.0.0:65040/"

    def test_machines(self):
        """test post """

        di = {
            "owner": 1,
            "pseudo": "testMachine",
            "location_id": 1,
            "plaque": "TEST-123-TEST",
            "constructor": "TEST",
            "model": "unTest",
            "category": "tracteur",
            "oil_capacity": 12,
            "oil": 1,
            "kms": 0,
            "hours": 0,
        }

        payload = json.dumps(di)

        url = TestMAchinePost.URL + "machines"
        response = requests.post(url, payload)
        print(response.text)
        assert response.status_code == 200

        # payload = response.json()
        # assert isinstance(payload, dict)
        # assert "data" in payload.keys()
        # assert "meta" in payload.keys()

