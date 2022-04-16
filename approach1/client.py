from threading import Thread
import requests
import time


def make_request():
  start = time.time()
  res = requests.get("http://127.0.0.1:8000/")
  print(time.time() - start)


if __name__ == "__main__":
  TOTAL_THREADS = 80

  while True:
    print()
    print("=" * 10 + " Calling " + "=" * 10)
    print()
    for i in range(TOTAL_THREADS):
      t = Thread(target=make_request)
      t.start()
    time.sleep(7)