import websockets
import asyncio

async def test_conn():
    async with websockets.connect('ws://localhost:3000//sampleServer') as ws:
        response = await ws.send('asdf')
        print(response)



def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_conn())
    loop.close()

if __name__ == '__main__':
    main()