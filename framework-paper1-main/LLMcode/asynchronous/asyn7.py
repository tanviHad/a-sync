import asyncio

async def long_running_task():
    print("Task started")
    # The task will attempt to sleep for 10 seconds
    await asyncio.sleep(10)
    print("Task finished")

async def main():
    try:
        # The coroutine will only be allowed to run for 5 seconds before a timeout is triggered
        await asyncio.wait_for(long_running_task(), timeout=5)
    except asyncio.TimeoutError:
        print("The task did not complete on time and has been cancelled")

# Run the main function
asyncio.run(main())
