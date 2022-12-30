import schedule
from datetime import time, timedelta, datetime
import time as tm

def job():
 print("Learn python everyday")


schedule.every().second .do(job)


while True:
  schedule.run_pending()
  tm.sleep(1)
