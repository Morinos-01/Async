import asyncio
import aiohttp
import requests
import os
from time import time



def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response, num):
    filename = f'image_{response.url.split("/")[-1]}_{num}.jpg'
    with open(f'image/{filename}', 'wb') as file:
        file.write(response.content)

def main():
    t0 = time()
    url = 'https://httpbin.org/image/jpeg'
    for i in range(1, 11):
        write_file(get_file(url), i)
    
    print(time() - t0)


# if __name__ == '__main__':
    # main()



###############################################
FOLDER = 'image-1'
def write_image(data, num):
    filename = f'{FOLDER}/file_{num}.jpg'
    with open(filename, 'wb') as file:
        file.write(data)



async def fetch_content(url, session, num):
    async with session.get(url, allow_redirects = True) as responce:
        data = await responce.read()
        write_image(data, num)



async def main_2():
     url = 'https://httpbin.org/image/jpeg'
     tasks = []
     async with aiohttp.ClientSession() as session:
        for i in range(1, 11):
            task = asyncio.create_task(fetch_content(url, session, i))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    os.makedirs(FOLDER, exist_ok= True)
    t0 = time()
    asyncio.run(main_2())
    print(time() - t0)