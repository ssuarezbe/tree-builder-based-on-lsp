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


def initialize_lsp():
    """
    send a msg with all the values needed to initialize the server
    """
    json_msg = {
        "jsonrpc": "2.0",
        "method": "initialize",
        "params": {
            "rootPath": "/Users/userpc/Desktop/folder",
            "rootUri": "file:////Users/userpc/Desktop/folder",
            "initializationOptions": {},
            "trace": "verbose"
            }
    }

def get_document_symbols():
    """
    Call the endpoint 'textDocument/documentSymbol' to get
    the symbols.

    @warnings: Requires that LSP server is initialized

    Payload examples:
    * https://github.com/microsoft/vscode-json-languageservice/issues/182
    * https://github.com/search?q=repo%3Amicrosoft%2Fvscode-languageserver-node%20provideDocumentSymbols&type=code
    """
    json_msg = {
        "jsonrpc": "2.0",
        "method": "textDocument/documentSymbol",
        "params": {
            "textDocument": {
                "uri": "vscode-userdata:/Users/ulugbekna/Library/Application%20Support/Code%20-%20Insiders/User/keybindings.json"
                }
        }
    }

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