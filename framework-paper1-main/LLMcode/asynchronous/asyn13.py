import asyncio

async def fetch_url(url):
    # async fetch of the url
    pass

async def process_url(url):
    # process the fetched url
    pass

async def main():
    urls = ["http://www.example.com/1",
            "http://www.example.com/2",
            "http://www.example.com/3"]
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        await process_url(result)

asyncio.run(main())