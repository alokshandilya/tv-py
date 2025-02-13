# `asyncio` library

- library for writing asynchronous, concurrent programs using the `async` and `await` syntax.
- allows to write non-blocking code that can handle many tasks concurrently, making it ideal for I/O-bound operations like network requests, file I/O, or database queries.

## 1. What Is `asyncio`?

### Purpose

`asyncio` is designed to handle asynchronous programming in Python. It enables you to write programs that can perform multiple tasks concurrently without blocking the main thread. This is particularly useful for tasks that involve waiting, such as:

- Network requests (HTTP, WebSocket).
- File I/O.
- Database queries.
- Real-time communication (e.g., chat applications).

### Key Characteristics

- **Non-blocking:** Tasks do not block the execution of other tasks while waiting.
- **Event Loop:** Manages and schedules coroutines, ensuring efficient task execution.
- **Coroutines:** Functions defined with `async def` that can be paused and resumed.
- **Concurrency, Not Parallelism:** `asyncio` achieves concurrency by interleaving tasks but does not run them in parallel on multiple CPU cores.

## 2. Core Concepts

### a. Coroutines

A coroutine is a function defined with `async def`. It can be paused and resumed using the `await` keyword.

#### Example

```python
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate a non-blocking delay
    print("World")

# Coroutines must be awaited or scheduled in an event loop
```

### b. Event Loop

The event loop is the heart of `asyncio`. It manages and schedules coroutines, ensuring that tasks run efficiently without blocking.

#### Key Functions

- `asyncio.run(coroutine)`: Runs the top-level coroutine and starts the event loop.
- `asyncio.create_task(coroutine)`: Schedules a coroutine to run concurrently.
- `asyncio.gather(*coroutines)`: Runs multiple coroutines concurrently and waits for all to complete.

#### Example

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())
```

### c. Awaitables

An awaitable is an object that can be awaited using the `await` keyword. Examples include:

- Coroutines.
- Tasks.
- Futures.

#### Example

```python
async def fetch_data():
    await asyncio.sleep(2)
    return "Data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

### d. Tasks

A task is a wrapper around a coroutine that schedules it to run on the event loop. Tasks allow you to run coroutines concurrently.

#### Example

```python
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await t1
    await t2

asyncio.run(main())
```

**Output:**

```
Task 1 started
Task 2 started
Task 2 finished
Task 1 finished
```

## 3. Advanced Features

### a. `asyncio.gather()`

Runs multiple coroutines concurrently and waits for all to complete.

#### Example

```python
async def fetch_url(url):
    print(f"Fetching {url}")
    await asyncio.sleep(2)
    return f"Data from {url}"

async def main():
    urls = ["https://example.com", "https://httpbin.org/get"]
    results = await asyncio.gather(*(fetch_url(url) for url in urls))
    print(results)

asyncio.run(main())
```

### b. Timeouts

Use `asyncio.wait_for()` to enforce timeouts on coroutines.

#### Example

```python
async def long_running_task():
    await asyncio.sleep(5)
    return "Done"

async def main():
    try:
        result = await asyncio.wait_for(long_running_task(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out")

asyncio.run(main())
```

### c. Queues

`asyncio.Queue` provides a way to share data between coroutines safely.

#### Example

```python
async def producer(queue):
    for i in range(5):
        print(f"Producing {i}")
        await queue.put(i)
        await asyncio.sleep(1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await producer_task
    await queue.join()  # Wait until the queue is empty
    consumer_task.cancel()

asyncio.run(main())
```

## 4. Practical Use Cases

### a. Web Scraping

Use `aiohttp` for asynchronous HTTP requests.

#### Example

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://example.com", "https://httpbin.org/get"]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result[:100])  # Print first 100 characters

asyncio.run(main())
```

### b. Real-Time Communication

Use `websockets` for real-time communication.

#### Example

```python
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

## 5. Best Practices

### a. Avoid Blocking Calls

Blocking calls (e.g., `time.sleep`) block the event loop. Use `asyncio.sleep` instead.

#### Bad Example

```python
import time

async def bad_task():
    time.sleep(2)  # Blocks the event loop
```

#### Good Example

```python
import asyncio

async def good_task():
    await asyncio.sleep(2)  # Non-blocking
```

### b. Use `asyncio.run()` for Top-Level Coroutines

Always use `asyncio.run()` to start the event loop for top-level coroutines.

#### Example

```python
async def main():
    await asyncio.sleep(1)

asyncio.run(main())
```

### c. Handle Exceptions Gracefully

Use `try-except` blocks to handle exceptions in coroutines.

#### Example

```python
async def risky_task():
    raise ValueError("Oops!")

async def main():
    try:
        await risky_task()
    except ValueError as e:
        print(f"Caught exception: {e}")

asyncio.run(main())
```

## 6. Limitations

### a. Single-Threaded

`asyncio` is single-threaded, meaning it cannot achieve true parallelism for CPU-bound tasks. Use `multiprocessing` or `concurrent.futures` for CPU-bound work.

### b. Debugging Complexity

Asynchronous code can be harder to debug due to concurrency issues like race conditions and deadlocks.

### c. Limited Use Cases

`asyncio` is best suited for I/O-bound tasks. For CPU-bound tasks, consider multiprocessing or threading.

## 7. Comparison with Other Concurrency Models

| Feature             | `asyncio`                     | Multithreading  | Multiprocessing |
| ------------------- | ----------------------------- | --------------- | --------------- |
| **Execution Model** | Single-threaded, event-driven | Multi-threaded  | Multi-process   |
| **Concurrency**     | High for I/O-bound tasks      | Moderate        | High            |
| **Parallelism**     | No                            | Limited by GIL  | Yes             |
| **Complexity**      | Moderate                      | Moderate        | High            |
| **Use Cases**       | I/O-bound tasks               | I/O-bound tasks | CPU-bound tasks |

> By mastering `asyncio`, you can write efficient and scalable Python programs for handling I/O-bound tasks. Its ability to manage thousands of concurrent connections makes it ideal for modern applications like web servers, real-time systems, and data pipelines. However, always choose the right concurrency model based on your specific use case.
