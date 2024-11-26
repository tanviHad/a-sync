import threading
import time

# Semaphore to control access to the shared resource.
sem = threading.Semaphore(3)

# Function to be executed by threads.
# Prints a greeting followed by the thread's name.
def print_greeting(name):
    # Acquire semaphore to get access to the shared resource.
    sem.acquire()
    try:
        print("Hello, %s!" % name)
    finally:
        # Release the semaphore to allow other threads to access the shared resource.
        sem.release()

# Create ten threads.
threads = []
for i in range(10):
    thread = threading.Thread(target=print_greeting, args=("Thread %d" % i,))
    threads.append(thread)

# Start the threads.
for thread in threads:
    thread.start()

# Wait for the threads to finish.
for thread in threads:
    thread.join()