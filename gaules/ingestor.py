from api import TwitchAPI
from cleaner import DataCleaner
from writer import DataWriter

class Ingestor:

    def __init__(self, user: str) -> None:
        self.user = user

    def ingest(self) -> None:
        api = TwitchAPI(user=self.user)
        data = api.get_data()
        cleaned_data = DataCleaner(data=data).clean()
        DataWriter(data_to_add = cleaned_data).write()