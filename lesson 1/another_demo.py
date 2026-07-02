import aiohttp
import asyncio
import aiofiles
import os
from time import time

FOLDER = 'image-2'
URL = 'https://httpbin.org/image/jpeg'

async def write_image(data, num):
    filename = f'{FOLDER}/photo_{num}.jpg'
    async with aiofiles.open(filename, 'wb') as file:
        await file.write(data)

async def fetch_content(url, session, num):
    async with session.get(url, allow_redirects = True) as response:
        data = await response.read()
        await write_image(data, num)


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1,11):
            task = asyncio.create_task(fetch_content(URL, session, i))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    os.makedirs(FOLDER, exist_ok= True)
    asyncio.run(main())
    print(f'время выполнения кода = {time() - t0}')
