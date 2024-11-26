import aiohttp
import asyncio

# Coroutine to fetch data from a URL
async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.text()

# Main coroutine to fetch data from multiple URLs
async def main():
    # URLs to fetch data from
    url1 = 'http://example.com'
    url2 = 'http://example.org'

    # Create an aiohttp session
    async with aiohttp.ClientSession() as session:
        # Fetch data from both URLs simultaneously
        data1, data2 = await asyncio.gather(
            fetch_data(session, url1),
            fetch_data(session, url2)
        )
        
        # Print the fetched data
        print(data1)
        print(data2)

# Run the main coroutine
asyncio.run(main())
