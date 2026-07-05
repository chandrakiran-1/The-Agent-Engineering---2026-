import asyncio

async def task1():
    print("Task1 Start:")
    await asyncio.sleep(4)
    print("Task1 End")
async def task2():
    print("Task2 Start")
    await asyncio.sleep(1)
    print("Task2 End")
async def main():
    await asyncio.gather(task1(),task2())
asyncio.run(main())