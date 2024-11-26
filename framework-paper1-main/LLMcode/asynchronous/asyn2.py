import asyncio

async def print_name_with_delay_1():
    await asyncio.sleep(1)
    print("Function with 1 second delay")

async def print_name_with_delay_2():
    await asyncio.sleep(2)
    print("Function with 2 second delay")

async def print_name_with_delay_3():
    await asyncio.sleep(3)
    print("Function with 3 second delay")

async def run_all():
    await asyncio.gather(
        print_name_with_delay_1(),
        print_name_with_delay_2(),
        print_name_with_delay_3(),
    )

asyncio.run(run_all())
