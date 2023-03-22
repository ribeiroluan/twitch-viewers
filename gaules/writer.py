import logging
import datetime
from sqlalchemy import create_engine, text

#Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class DataWriter:

    def __init__(self, data_to_add:dict) -> None:
        self.data_to_add = data_to_add

    def _write_qry(self):
        return f'''
                INSERT INTO gaules (request_time, user_name, game_id, game_name, "type", viewer_count, title)
                VALUES ('{self.data_to_add['request_time']}', '{self.data_to_add['user_name']}', {self.data_to_add['game_id']}, '{self.data_to_add['game_name']}', '{self.data_to_add['type']}', {self.data_to_add['viewer_count']}, '{self.data_to_add['title']}');
                '''
    def write(self) -> None:
        engine = create_engine('postgresql+psycopg2://root:root@localhost/twitch_db')
        
        with engine.connect() as conn:
            result = conn.execute(text(self._write_qry()))
            conn.commit()

        logger.info(f"Writing data to twitch_db at {datetime.datetime.now().isoformat()}")