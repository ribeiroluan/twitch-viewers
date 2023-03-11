import time

from schedule import repeat, every, run_pending
from ingestor import Ingestor

if __name__ == "__main__":
    gaules = Ingestor("gaules")


    @repeat(every(10).seconds)
    def job():
        gaules.ingest()

    while True:
        run_pending()
        time.sleep(0.5)