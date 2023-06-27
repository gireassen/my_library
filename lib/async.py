import asyncio

def sync_function(arg1: int, arg2: int) -> int:
    return arg1+ arg2

async def async_function() -> int:
    '''
    asyncio.run(async_function())
    вызов обычной функции в асинхронной
    '''
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, sync_function, 111, 233)
    print(result)
    return result

if __name__ == "__main__":
    asyncio.run(async_function())