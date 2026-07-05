import asyncio

async def wish():
    print("1")
    await asyncio.sleep(3)
    print("2")
asyncio.run(wish())