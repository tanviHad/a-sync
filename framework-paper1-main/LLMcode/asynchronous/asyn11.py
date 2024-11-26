import asyncio
from codetiming import Timer

async def task(name, work_queue):
    while not work_queue.empty():
        delay = await work_queue.get()
        timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
        print(f"Task {name} running")
        timer.start()
        await asyncio.sleep(delay)
        timer.stop()
        work_queue.task_done()

async def main():
    # Create the asynchronous queue of work
    work_queue = asyncio.Queue()

    # Put some work in the queue
    for work in [15, 10, 5, 2]:
        await work_queue.put(work)

    # Create tasks and gather them so the program will wait for both tasks to complete
    task_one = asyncio.create_task(task("One", work_queue))
    task_two = asyncio.create_task(task("Two", work_queue))

    # Use asyncio.gather to run both tasks concurrently
    await asyncio.gather(task_one, task_two)

    # Ensure all work in the queue is done
    await work_queue.join()

# Start the program running asynchronously
asyncio.run(main())
