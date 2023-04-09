import requests
import logging
import json
import datetime
from os import getenv
from dotenv import load_dotenv

#Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

#Load API Key
load_dotenv()
API_KEY = getenv('KEY')

class UserNotFound(Exception):
    
    def __init__(self, user):
        self.user = user
        self.message = f"User {self.user} not found on Twitch"
        super().__init__(self.message)


class TwitchAPI:

    def __init__(self, user:str) -> None:
        self.user = user
        self.base_endpoint = f"https://gwyo-twitch.p.rapidapi.com/stream"

    def _get_endpoint(self) -> str:
        return f"{self.base_endpoint}/{self.user}"

    def _get_auth(self) -> dict:
        return {"X-RapidAPI-Key": API_KEY,
                "X-RapidAPI-Host": "gwyo-twitch.p.rapidapi.com"}

    def get_data(self) -> dict:
        try:
            endpoint = self._get_endpoint()
            headers = self._get_auth()
            logger.info(f"Getting data from endpoint {endpoint} at {datetime.datetime.now().isoformat()}")
            response = requests.get(url=endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            raise UserNotFound(self.user)