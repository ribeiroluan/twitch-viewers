import pytest
from gaules.api import TwitchAPI
from gaules.cleaner import DataCleaner
import requests
from unittest.mock import patch, mock_open

class TestDataCleaner:
    def test_get_important_columns(self):
        actual = DataCleaner(data={'foo':'bar'})._get_important_columns()
        expected = ["user_name", "game_id", "game_name", "type", "viewer_count", "title"]
        assert actual == expected

    @patch("gaules.cleaner.DataCleaner._get_important_columns", return_value=["test_column"])
    def test_clean_dict_empty(self, mock):
        actual = DataCleaner(data={}).clean().get("type")
        expected = "offline"
        assert actual == expected
