import asyncio

async def worker(name, delay):
    print(f"{name}: start")
    await asyncio.sleep(delay)
    print(f"{name}: middle")
    await asyncio.sleep(0)
    print(f"{name}: end")

async def nested():
    print("nested: start")
    await worker("X", 0)
    print("nested: end")

async def main():
    print("main: 1")

    t1 = asyncio.create_task(worker("A", 0))
    t2 = asyncio.create_task(worker("B", 0))

    print("main: 2")

    await nested()

    print("main: 3")

    await asyncio.gather(
        worker("C", 0),
        worker("D", 0)
    )

    print("main: 4")

    await t1
    await t2

    print("main: 5")

asyncio.run(main())