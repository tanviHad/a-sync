import asyncio

async def compute_square(number):
    print("Computing square of", number)
    await asyncio.sleep(2)
    return number * number

async def compute_cube(number):
    print("Computing cube of", number)
    await asyncio.sleep(2)
    return number * number * number

async def main():
    tasks = [compute_square(2), compute_cube(2)]
    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())