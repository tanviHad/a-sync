import time
import requests
from queue import Queue

# Create a queue to store the URLs 
urls_queue = Queue()

# Add all the URLs to the queue
urls_queue.put("https://www.example1.com")
urls_queue.put("https://www.example2.com")
urls_queue.put("https://www.example3.com")
urls_queue.put("https://www.example4.com")

# Create a generator to iterate over the queue
def get_urls():
    while not urls_queue.empty():
        yield urls_queue.get()

# Create a function to make synchronous HTTP GET requests
def make_requests(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    print("Time taken for {}: {}".format(url, end_time - start_time))


# Iterate over the generator and make requests synchronously
total_time = 0
for url in get_urls():
    make_requests(url)
    total_time += time.time() - start_time

# Output the total elapsed time for all requests
print("Total elapsed time: {}".format(total_time))