import asyncio

async def async_print(items):
    for key, value  in enumerate(items):
        await asyncio.sleep(key+1)
        print(value)