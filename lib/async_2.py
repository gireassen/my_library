import asyncio

async def short_task():
    while True:
        await asyncio.sleep(2)
        print('short')

async def long_task():
    while True:
        await asyncio.sleep(8)
        print('long')

async def main():
    await asyncio.gather(short_task(), long_task())
    #result = await asyncio.gather(short_task(), long_task())

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop) 
    loop.run_until_complete(main())