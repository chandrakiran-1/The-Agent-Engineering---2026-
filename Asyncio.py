import asyncio
async def task1():
    print("Task1 Started:")
    await asyncio.sleep(5)
    print("Task1 Ended")
async def task2():
    print("Task2 Started:")
    await asyncio.sleep(2)
    print("Task2 Ended")
async def main():
    await asyncio.gather(task1(),task2())
asyncio.run(main())