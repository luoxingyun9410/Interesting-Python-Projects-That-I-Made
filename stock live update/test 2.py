import schedule
import time

def job1():
    print("Job 1")

schedule.every().minute.at(":30").do(job1)

while True:
    schedule.run_pending()