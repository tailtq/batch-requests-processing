import time
from redis import Redis

from const import REDIS_QUEUE_NAME

r = Redis()

# worker runs in parallel to get data from queue and process
while True:
  # should set sleep here for context switching
  time.sleep(2)
  total_messages = r.llen(REDIS_QUEUE_NAME)
  print(f"Queue size: {total_messages}")

  if total_messages == 0:
    continue

  messages = r.lpop(REDIS_QUEUE_NAME, count=total_messages)
  for message in messages:
    # set key to respond back to server
    r.set(message, message)
