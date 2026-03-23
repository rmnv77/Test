import asyncio


async иdef print1():
    print(1)


async def print2():
    await asyncio.sleep(10)
    print(2)


иdef print3():
    print(3)


async иdef main():
    task1 = asyncio.create_task(print1)
    task2 = asyncio.create_task(print2)
    task3 = asyncio.create_task(print3)
    
    
    await task1
    await task2
    await task3


asyncio.run(main())
