import pytest
from gaules.api import TwitchAPI
import requests
from unittest.mock import patch, mock_open



#mock to replace our request.get method
def mocked_requests_get(*args, **kwargs):
    class MockResponse(requests.Response):
        def __init__(self, json_data, status_code):
            super().__init__()
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
        
        def raise_for_status(self) -> None:
            if self.status_code != 200:
                raise Exception
    print(args)
    if kwargs.get('url')== 'valid_endpoint':
        return MockResponse(json_data={"foo":"bar"}, status_code=200)
    else:
        return MockResponse(json_data=None, status_code=404)

class TestTwitchApi:

    @pytest.mark.parametrize(
    "user, expected",
        [
            ("gaules", "https://gwyo-twitch.p.rapidapi.com/stream/gaules"),
            ("nyang", "https://gwyo-twitch.p.rapidapi.com/stream/nyang"),
            ("mch_agg", "https://gwyo-twitch.p.rapidapi.com/stream/mch_agg"),
        ]
    )   
    def test_get_endpoint(self, user, expected):
        api = TwitchAPI(user=user)
        actual = api._get_endpoint()
        assert actual == expected

    def test_get_auth(self):
        api = TwitchAPI(user="test_user")
        actual = api._get_auth()
        expected = {"X-RapidAPI-Key": "e0fb00408emshea80e13f62d0f07p17e386jsnc1878c4b91f4",
                "X-RapidAPI-Host": "gwyo-twitch.p.rapidapi.com"}
        assert actual == expected

    @patch("requests.get")
    @patch("gaules.api.TwitchAPI._get_endpoint", return_value="valid_endpoint")
    @patch("gaules.api.TwitchAPI._get_auth", return_value={"foo":"bar"})
    def test_get_data_requests_is_called(self, mock_get_auth, mock_get_endpoint, mock_requests):
        gaules = TwitchAPI(user="test_user")
        gaules.get_data()
        mock_requests.assert_called_once_with(url="valid_endpoint", headers={"foo":"bar"})

    @patch("requests.get", side_effect=mocked_requests_get)
    @patch("gaules.api.TwitchAPI._get_endpoint", return_value="valid_endpoint")
    @patch("gaules.api.TwitchAPI._get_auth", return_value={"foo":"bar"})
    def test_get_data_with_invalid_endpoint(self, mock_get_auth, mock_get_endpoint, mock_requests):
        with pytest.raises(Exception):
            TwitchAPI.get_data()