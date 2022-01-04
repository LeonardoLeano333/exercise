import asyncio
import time

async def example(wait_time, value):
    await asyncio.sleep(wait_time)
    print(time.time())
    print(value)

async def run(items):
    await asyncio.gather(*[example(2*items.index(item), item) for item in items])


# async def async_print(items):
#     for key, value  in enumerate(items):
#         await asyncio.sleep(key+1)
#         print(value)

# Your code will actually print at 1,3,7,15 seconds from the beginning. can you make it print at 1,2,4,8 seconds? We are looking for concurrency.

# I have tried this again debuging the time and it is realy not in a concurency
# I confess that I was learning about async argument in python I made in other time a 
# class for multiprocessing using a the library multiprocessing that is a bit trick to
# understand...
# https://github.com/LeonardoLeano333/python_basics/blob/master/design_examples/multiprocessing_pool_example.py

if __name__ == "__main__":
    items = ["a","b","c","d"]
    asyncio.run(run(items))
