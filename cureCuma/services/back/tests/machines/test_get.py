import os

import pytest
import requests


class TestMAchineGet:
    """Test Machine Get """

    URL = "http://0.0.0.0:65040/"

    def test_ping(self):
        """test ping """

        url = TestMAchineGet.URL + "machines/ping"
        response = requests.get(url)
        assert response.status_code == 200

    def test_machines(self):
        """test ping """

        url = TestMAchineGet.URL + "machines"
        response = requests.get(url)
        assert response.status_code == 200

        payload = response.json()
        assert isinstance(payload, dict)
        assert "data" in payload.keys()
        assert "meta" in payload.keys()


# if __name__ == "__main__":
#     TestMAchineGet.test_ping()
#     TestMAchineGet.test_machines()
