import datetime

class DataCleaner:

    def __init__(self, data:dict) -> None:
        self.data = data

    def _get_important_columns(self) -> list:
        return ["user_name", "game_id", "game_name", "type", "viewer_count", "title"]

    def clean(self) -> dict:
        if len(self.data) == 0: #the dictionary is empty, user offline
            output = {key: None for key in self._get_important_columns()}
            output["type"] = "offline"
            output["game_id"] = 0
            output["viewer_count"] = 0
        else: 
            output = {key: self.data[key] for key in self._get_important_columns()}
        
        output["request_time"] = datetime.datetime.now().isoformat()

        return output