import asyncio
import time

import aiohttp


async def fetch_data(session, url):
    """Fetches data from a URL asynchronously."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()  # Or response.text() if it's not JSON
            else:
                print(f"Error: {response.status} for {url}")
                return None
    except aiohttp.ClientError as e:
        print(f"Client error: {e} for {url}")
        return None


async def process_data(data):
    """Processes the fetched data (example: calculates length)."""
    if data:
        # Simulate some processing time (replace with your actual logic)
        await asyncio.sleep(1)  # Simulate 1 second of processing
        return len(data)  # Example: return the length of the data
    return 0


async def main():
    """Main function to fetch and process data concurrently."""
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",  # Example API endpoints
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
    ]

    start_time = time.time()  # Record start time

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)  # Run fetches concurrently

    processing_tasks = [process_data(result) for result in results]
    processed_results = await asyncio.gather(
        *processing_tasks
    )  # Run processing concurrently

    end_time = time.time()  # Record end time

    print("Fetched data:")
    for i, result in enumerate(results):
        print(f"URL {i+1}: {result}")

    print("\nProcessed data:")
    for i, result in enumerate(processed_results):
        print(f"URL {i+1}: Length {result}")

    time_taken = end_time - start_time
    print(f"\nTotal time taken: {time_taken:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
