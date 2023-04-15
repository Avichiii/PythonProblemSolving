import asyncio
from string import ascii_uppercase
import random

async def send_request() -> str:
    await asyncio.sleep(1)
    return random.choices(ascii_uppercase)[0]

async def send_request_politely(s: asyncio.Semaphore) -> str:
    async with s:
        return await send_request()

async def request_manager(n: int) -> str:
    s = asyncio.Semaphore(150)
    tasks = [asyncio.create_task(send_request_politely(s)) for _ in range(n)]
    res = await asyncio.gather(*tasks)
    return ''.join(res)

concatinated_string = asyncio.run(request_manager(300))

print(concatinated_string)