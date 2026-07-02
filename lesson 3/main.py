import asyncio
import aiofiles
import json
from pathlib import Path
from time import time
BASE_DIR = Path(__file__).parent
p = BASE_DIR / 'Pokemon JSON Files'
new_f = BASE_DIR / 'pokemon_moves' 
new_f.mkdir(exist_ok= True)

async def process_file(path):
    async with aiofiles.open(path, 'r') as f:
        contents = await f.read()
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]
    path = BASE_DIR / 'pokemon_moves' / f'{name}_move.txt'
    async with aiofiles.open(path, 'w') as f_2:
        await f_2.write('\n'.join(moves))


async def main():
    tasks = []
    for path in p.glob('*json'):
        task = asyncio.create_task(process_file(path))
        tasks.append(task)
    await asyncio.gather(*tasks)


t0 = time()
asyncio.run(main())
print(time() - t0)