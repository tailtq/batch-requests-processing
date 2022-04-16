from fastapi import FastAPI
from redis import Redis
import uuid
import time
from anyio.lowlevel import RunVar
from anyio import CapacityLimiter

from const import REDIS_QUEUE_NAME

app = FastAPI()
r = Redis()


@app.get("/")
def act():
  _id = str(uuid.uuid4())
  r.rpush(REDIS_QUEUE_NAME, _id)

  value = None
  counter = 0

  # wait 10s or stop when the result is returned
  while counter < 100:
    # check queue size to see if multiple threads push to this queue
    print(f"Queue size: {r.llen(REDIS_QUEUE_NAME)}")

    # get value of request using hash key
    value = r.get(_id)
    if value:
      r.delete(_id)
      break

    counter += 1
    time.sleep(0.1)

  return {"status": value}


# increase threadpool size to handle more synchronous requests (100 requests/time)
# doc: https://github.com/tiangolo/fastapi/issues/4221#issuecomment-982260467
@app.on_event("startup")
def startup():
    RunVar("_default_thread_limiter").set(CapacityLimiter(100))
