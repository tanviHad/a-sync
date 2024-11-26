import asyncio
import random
from codetiming import Timer

async def task(name, work_queue):
    while not work_queue.empty():
        url = await work_queue.get()
        print(f"Task {name} getting URL: {url}")
        timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
        timer.start()
        # Simulate a network delay instead of a real web request
        await asyncio.sleep(random.uniform(0.1, 0.6))  # Random delay
        timer.stop()
        work_queue.task_done()

async def main():
    # Create the asynchronous queue of work
    work_queue = asyncio.Queue()

    # Put some work in the queue
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]
    for url in urls:
        await work_queue.put(url)

    # Create tasks
    task_one = asyncio.create_task(task("One", work_queue))
    task_two = asyncio.create_task(task("Two", work_queue))

    # Run the tasks and wait until they are completed
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(task_one, task_two)
        await work_queue.join()  # Ensure all tasks are done

# Run the program
asyncio.run(main())
