import time
import datetime
from schedule import repeat, every, run_pending
from ingestor import Ingestor

if __name__ == "__main__":
    gaules = Ingestor("gaules")

    @repeat(every(60).seconds)
    def job():
        gaules.ingest()

    start_time = datetime.datetime(2023, 3, 22, 0, 0, 0, 0)
    end_time = start_time + datetime.timedelta(days = 7)

    while True:
        if datetime.datetime.now() >= start_time and datetime.datetime.now() <= end_time:
            run_pending()
            time.sleep(0.5)