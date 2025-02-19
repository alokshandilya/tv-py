import time

import requests


def fetch_data(url):
    """Fetches data from a URL synchronously."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Or response.text()
        else:
            print(f"Error: {response.status_code} for {url}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e} for {url}")
        return None


def process_data(data):
    """Processes the fetched data (example: calculates length)."""
    if data:
        time.sleep(1)  # Simulate 1 second of processing
        return len(data)  # Example: return the length of the data
    return 0


def main():
    """Main function to fetch and process data sequentially."""
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",  # Example API endpoints
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
    ]

    start_time = time.time()

    results = []
    for url in urls:
        data = fetch_data(url)
        results.append(data)

    processed_results = []
    for result in results:
        processed_data_val = process_data(result)
        processed_results.append(processed_data_val)

    end_time = time.time()

    print("Fetched data:")
    for i, result in enumerate(results):
        print(f"URL {i+1}: {result}")

    print("\nProcessed data:")
    for i, result in enumerate(processed_results):
        print(f"URL {i+1}: Length {result}")

    time_taken = end_time - start_time
    print(f"\nTotal time taken: {time_taken:.2f} seconds")


if __name__ == "__main__":
    main()
