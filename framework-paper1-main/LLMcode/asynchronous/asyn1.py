import asyncio

async def print_message():
    await asyncio.sleep(2)
    print("Python Exercises!")

asyncio.run(print_message())