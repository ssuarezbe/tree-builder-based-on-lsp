import websockets
import asyncio
"""
async def test_conn():
    async with websockets.connect('ws://localhost:3000/vbaLspSampleServer') as ws:
        response = await ws.send('asdf')
        print(response)
        # receive and print the response from the server
        print(ws.recv())
        # close the connection
        ws.close()



def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_conn())
    loop.close()

if __name__ == '__main__':
    main()
"""
import websockets, asyncio
import json

p = {"jsonrpc":"2.0","method":"initialize","id":1,"params":{"trace":"off","processId":2729,"capabilities":[],"workspaceFolders":None,"rootUri":None,"rootPath":None,"clientInfo":{"version":"0.10.0-dev+Homebrew","name":"Neovim"}}}

async def client(uri):
    websocket = await websockets.connect(uri)
    async def send_recv(msg):
        print(f'-> MSG: {msg}')
        await websocket.send(msg)
        resp = await websocket.recv()
        print(f'<- RESPONSE: {resp}')

    await send_recv(json.dumps(p))
    await send_recv("Goodbye!")
    await websocket.close()

asyncio.run(client('ws://localhost:3000/vbaLspSampleServer'))  