import asyncio

async def fetch_data():
    print("starting fetching data")
    await asyncio.sleep(2)
    print("data fetched")
    return {"data": "sample"}

async def main():
    print("start main")
    data = await fetch_data()
    print('received_data:', data)
    print("end main")

# run the main coroutine
asyncio.run(main())