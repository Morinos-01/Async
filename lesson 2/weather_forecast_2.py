import asyncio 
import json
from aiohttp import ClientSession, web



async def get_weather(city, session):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city, 
        'appid': '2a4ff86f9aaa70041ec8e82db64abf56',
        'lang': 'ru',
        'units': 'metric'}
    async with session.get(url = url, params = params) as response:
        data = await response.json()
        try:
            return (               
                f'{data["weather"][0]["description"]}, '
                f'{data["main"]["temp"]}°C')
        except KeyError:
            return('Нет данных')
        


async def handle(request):
    session = request.app['session']
    city = request.rel_url.query['city']
    weather = await get_weather(city, session=session)
    result = {'city': city, 'weather': weather}
    return web.Response(text = json.dumps(result, ensure_ascii = False))


async def main():
    async with ClientSession() as session:
        app = web.Application()
        app['session'] = session
        app.add_routes([web.get('/weather', handle)])
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8080)
        await site.start()
        while True:
            await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())