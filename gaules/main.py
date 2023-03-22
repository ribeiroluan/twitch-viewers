import time
import datetime
from schedule import repeat, every, run_pending
from ingestor import Ingestor
import logging

#Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    gaules = Ingestor("gaules")

    @repeat(every(60).seconds)
    def job():

        start_time = datetime.datetime(2023, 3, 21, 0, 0, 0)
        end_time = start_time + datetime.timedelta(days = 7)

        if datetime.datetime.now() >= start_time and datetime.datetime.now() <= end_time:
            gaules.ingest()
        else:
            logger.info(f"Run either not started or already completed at {datetime.datetime.now().isoformat()}")

    while True:
        run_pending()
        time.sleep(1)