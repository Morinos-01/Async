import asyncio 
from aiohttp import ClientSession



async def get_weather(city, session):
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 
                  'appid': '2a4ff86f9aaa70041ec8e82db64abf56',
                  'lang': 'ru',
                  'units': 'metric'}
        async with session.get(url = url, params = params) as response:
            data = await response.json()
            print(
                f'{city}: '
                f'{data["weather"][0]["description"]}, '
                f'{data["main"]["temp"]}°C')
#            print(data)


async def main(cities):
    tasks = []
    async with ClientSession() as session:
        for city in cities:
            task = asyncio.create_task(get_weather(city, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    cities = ['Moscow', 'St. Petersburg']
    
    asyncio.run(main(cities))
