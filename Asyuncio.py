import asyncio

async def wish():
    return "hello all"
Wish = wish()
asyncio.run(wish())