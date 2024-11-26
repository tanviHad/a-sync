import asyncio
import time

async def do_something(num, delay):
    await asyncio.sleep(delay)
    return f"Task {num} completed after {delay} seconds"

async def main():
    start_time = time.time()
    
    results = await asyncio.gather(
        do_something(1, 1),
        do_something(2, 2),
        do_something(3, 3)
    )

    total_time = time.time() - start_time
    print(f"All tasks completed in {total_time} seconds")

    for result in results:
        print(result)

asyncio.run(main())
