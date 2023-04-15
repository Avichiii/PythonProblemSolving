import asyncio
from string import ascii_uppercase
import random

async def send_request() -> str:
    await asyncio.sleep(1)
    return random.choices(ascii_uppercase)[0]


async def request_manager(n: int) -> str:
    tasks = [asyncio.create_task(send_request()) for _ in range(n)]
    res = await asyncio.gather(*tasks)
    return ''.join(res)

contate_string = asyncio.run(request_manager(89))

print(contate_string)