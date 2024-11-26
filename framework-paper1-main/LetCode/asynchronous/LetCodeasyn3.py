import asyncio
async def display_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)
# Run the coroutine using asyncio.run()
asyncio.run(display_numbers())
