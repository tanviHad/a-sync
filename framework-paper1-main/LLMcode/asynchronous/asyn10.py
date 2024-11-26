import time
import queue
from codetiming import Timer

def task(name, work_queue):
    while not work_queue.empty():
        delay = work_queue.get()
        with Timer(text=f"Task {name} elapsed time: {{:.1f}}"):
            print(f"Task {name} running")
            time.sleep(delay)  # Simulate work with a sleep delay
        yield  # Yield control back to the main loop

def main():
    # Create two queues of work
    work_queue_one = queue.Queue()
    work_queue_two = queue.Queue()

    # Put some work in the queues
    for work in [15, 5]:
        work_queue_one.put(work)
    for work in [10, 2]:
        work_queue_two.put(work)

    # Create tasks with their respective queues
    tasks = [task("One", work_queue_one), task("Two", work_queue_two)]

    # Run the tasks
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        while tasks:
            for t in tasks.copy():  # Iterate over a shallow copy of the list
                try:
                    next(t)
                except StopIteration:
                    tasks.remove(t)

if __name__ == "__main__":
    main()
