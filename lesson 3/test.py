import asyncio

async def worker(name, delay):
    print(f"{name}: start")
    await asyncio.sleep(delay)
    print(f"{name}: middle")
    await asyncio.sleep(0)
    print(f"{name}: end")

async def pipeline():
    print("pipeline: start")
    t = asyncio.create_task(worker("P", 0))
    await worker("Q", 0)
    print("pipeline: end")
    await t

async def main():
    print("main: 1")

    t1 = asyncio.create_task(worker("A", 1))
    t2 = asyncio.create_task(pipeline())

    print("main: 2")

    await asyncio.gather(
        worker("B", 0),
        worker("C", 1)
    )

    print("main: 3")

    await t1
    await t2

    print("main: 4")

asyncio.run(main())

# main: 1
# main: 2
# B: start
# C: start - ожидание 1 секунда
# A: start - ожидание 1 секунда
# Pipeline: start
# Q: start
# B: middle
# P: start
# Q: middle 
# B: end
# P: middle
# Q: end
# P: end
# pipeline: end
# C: middle
# A: middle 
# C: end
# main: 3
# A: end
# main: 4