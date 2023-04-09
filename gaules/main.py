import time
import datetime
from schedule import repeat, every, run_pending
from ingestor import Ingestor
import logging

#Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    streamer = Ingestor("gaules")

    @repeat(every(10).minutes)
    def job():

        start_time = datetime.datetime(2023, 3, 29, 0, 0, 0)
        end_time = start_time + datetime.timedelta(days = 7)

        if datetime.datetime.now() >= start_time and datetime.datetime.now() <= end_time:
            streamer.ingest()
        else:
            logger.info(f"Run either not started or already completed at {datetime.datetime.now().isoformat()}")

    while True:
        run_pending()
        time.sleep(1)