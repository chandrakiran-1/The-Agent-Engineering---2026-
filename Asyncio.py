import asyncio

async def wish():
    print("1")
    await asyncio.sleep(3)
    print("2")
asyncio.run(wish())

async def num():
    print("one")
    await asyncio.sleep(2)
    print("two")
    await asyncio.sleep(3)
    print("Three")
    await asyncio.sleep(4)
    print("Four")
asyncio.run(num())