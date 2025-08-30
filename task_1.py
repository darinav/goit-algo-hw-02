import random
import time
from queue import Queue

request_queue = Queue()

def generate_request():
    request = {"id": int(time.time() * 1000)}
    request_queue.put(request)

def process_request():
    if request_queue.empty():
        print("No requests")
        return
    processing_request = request_queue.get()
    print(f"Request {processing_request['id']} was processed."
          f"\n {request_queue.qsize()} requests left")

def main():
    # Generate some amount of starting requests
    for i in range(random.randint(5, 10)):
        generate_request()
    print("Request processing started. Press Ctrl+C to exit")
    try:
        while True:
            generate_request()
            time.sleep(1)
            process_request()
            process_request() # for testing to see progress
    except KeyboardInterrupt:
        print("\nRequest processing stopped")

if __name__ == "__main__":
    main()