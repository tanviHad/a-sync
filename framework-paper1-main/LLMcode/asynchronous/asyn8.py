import asyncio
import random

async def producer(queue, producer_id):
    for i in range(3):  # Each producer produces 3 items
        item = (producer_id, i)
        await asyncio.sleep(random.randint(1, 3))  # Simulate random delay
        await queue.put(item)
        print(f"Producer {producer_id} produced {item}")
    # After producing items, send None to signal the consumer to stop
    await queue.put(None)

async def consumer(queue, producers_done, num_producers):
    while not producers_done.is_set():
        item = await queue.get()
        if item is None:
            # Decrement the counter for each None received
            num_producers -= 1
            if num_producers == 0:
                # If all producers are done, signal to stop the consumer
                producers_done.set()
        else:
            print(f"Consumer is processing item {item}")
            await asyncio.sleep(1)  # Simulate processing delay
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    num_producers = 3
    producers_done = asyncio.Event()

    # Start the producers
    producers = [asyncio.create_task(producer(queue, i)) for i in range(num_producers)]

    # Start the consumer
    consumer_task = asyncio.create_task(consumer(queue, producers_done, num_producers))

    # Wait for all producers to finish
    await asyncio.gather(*producers)

    # Wait for the consumer to finish processing after all producers are done
    await producers_done.wait()
    await queue.join()  # Ensures all items have been processed and the queue is empty

    # Cancel the consumer task, now that it's done
    consumer_task.cancel()

# Run the main function
asyncio.run(main())
