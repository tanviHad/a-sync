import asyncio

async def time_consuming_task():
    try:
        print('Task started, will run for 5 seconds.')
        await asyncio.sleep(5)
        print('Task completed.')
    except asyncio.CancelledError:
        print('Task was cancelled before completion.')

async def main():
    task = asyncio.create_task(time_consuming_task())

    await asyncio.sleep(2)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print('Main also acknowledges the task was cancelled.')

asyncio.run(main())
