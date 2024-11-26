import asyncio

async def print_numbers():
    for number in range(1, 8):
        print(number)
        await asyncio.sleep(1)

# Create a new event loop
new_loop = asyncio.new_event_loop()
# Set the created event loop as the current event loop
asyncio.set_event_loop(new_loop)

try:
    # Run the coroutine
    new_loop.run_until_complete(print_numbers())
finally:
    # Close the loop
    new_loop.close()
