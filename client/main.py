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
import os
from uuid_v7.base import uuid7

src_code_folder = os.path.join('tmp','lsp','vba')


"""
LSP server lifetime :

* https://microsoft.github.io/language-server-protocol/specifications/specification-3-15/#initialize
"""

def get_initialize_lsp_msg():
    """
    Example of simple initializeParams:

    https://github.com/microsoft/vscode-languageserver-node/blob/a561f1342ba94ad7f550cb15446f65432f5e1367/server/src/node/test/connection.test.ts#L50C15-L50C32

    send a msg with all the values needed to initialize the server

    The init parameters can be found class:

    # `export interface _InitializeParams extends WorkDoneProgressParams`.
    * https://github.com/microsoft/vscode-languageserver-node/blob/a561f1342ba94ad7f550cb15446f65432f5e1367/protocol/src/common/protocol.ts#L1503

    {
        "rootPath": "$PWD/../examples-csharp/MutexSingleInstanceAndNamedPipe",
        "rootUri": "file://$PWD/../examples-csharp/MutexSingleInstanceAndNamedPipe",
        "workspaceFolders": [
          {
            "name": "$PWD/../examples-csharp/MutexSingleInstanceAndNamedPipe",
            "uri": "file://$PWD/../examples-csharp/MutexSingleInstanceAndNamedPipe"
          }
        ]
    }

    Payload details:

    * @locale: See https://en.wikipedia.org/wiki/IETF_language_tag
    """
    call_id:str = str(uuid7())
    json_msg = {
        "jsonrpc": "2.0",
        "id":call_id,
        "method": "initialize",
        "params": {
            "locale": "en",
            "rootPath":src_code_folder,
            "rootUri": f"file://{src_code_folder}",
            "workspaceFolders":[{
                "name": src_code_folder,
                 "uri": f"file://{src_code_folder}"
            }],
            "capabilities":{},
            "initializationOptions": {},
            "trace": "verbose"
            }
    }
    return json.dumps(json_msg)

def get_open_document_on_lsp_server_msg(filename:str, file_content:str):
    """
    Client send a request to the server to set a document as ._activeDocument

    https://microsoft.github.io/language-server-protocol/specifications/specification-3-15/#textDocument_didOpen 

    textDocument/didClose


    the method DOES exists:

    https://github.com/microsoft/vscode-languageserver-node/blob/a561f1342ba94ad7f550cb15446f65432f5e1367/protocol/src/common/protocol.ts#L1961
    """
    call_id:str = str(uuid7())
    close_json_msg = {
        "jsonrpc": "2.0",
        "id":call_id,
        "method": "textDocument/didClose",
        "params": {
            "textDocument": {
                "uri":  f'file:///{filename}',
                "languageId":"vb",
                "text": file_content
                }
        }
    }
    # call example https://github.com/Dart-Code/Dart-Code/issues/3625
    open_json_msg = {
        "jsonrpc": "2.0",
        "id":call_id,
        "method": "textDocument/didOpen",
        "params": {
            "textDocument": {
                "uri":  f'file:///{filename}',
                "languageId":"vb",
                "text": file_content
                }
        }
    }

    change_json_msg = {
        "jsonrpc": "2.0",
        "id":call_id,
        "method": "textDocument/didChange",
        "params": {
            "textDocument": {
                "uri":  f'file:///{filename}',
                "languageId":"vb",
                "text": file_content
                }
        }
    }
    return (json.dumps(close_json_msg), json.dumps(open_json_msg), json.dumps(change_json_msg))

def get_document_symbols_msg(filename:str):
    """
    Documentation:

    * https://microsoft.github.io/language-server-protocol/specifications/specification-3-15/#textDocument_documentSymbol

    Example of basic DocumentSymbolParams :

    * https://github.com/microsoft/vscode-languageserver-node/blob/a561f1342ba94ad7f550cb15446f65432f5e1367/protocol/src/node/test/connection.test.ts#L115

    Call the endpoint 'textDocument/documentSymbol' to get
    the symbols.

    @warnings: Requires that LSP server is initialized

    Payload examples:
    * https://github.com/microsoft/vscode-json-languageservice/issues/182
    * https://github.com/search?q=repo%3Amicrosoft%2Fvscode-languageserver-node%20provideDocumentSymbols&type=code
    """
    call_id:str = str(uuid7())
    """
    How enalble a document into a LSP server:
    * https://stackoverflow.com/questions/76756132/python-client-library-for-language-server-protocol-lsp
    """
    
    json_msg = {
        "jsonrpc": "2.0",
        "id":call_id,
        "method": "textDocument/documentSymbol",
        "params": {
            "textDocument": {
                "uri":  f'file:///{filename}'
                }
        }
    }
    return json.dumps(json_msg)

p = {"jsonrpc":"2.0","method":"initialize","id":1,"params":{"trace":"off","processId":2729,"capabilities":[],"workspaceFolders":None,"rootUri":None,"rootPath":None,"clientInfo":{"version":"0.10.0-dev+Homebrew","name":"Neovim"}}}

async def client(uri):
    websocket = await websockets.connect(uri)
    async def send_recv(msg):
        print(f'-> MSG: {msg}')
        await websocket.send(msg)
        resp = await websocket.recv()
        print(f'<- RESPONSE: {resp}')
        print("\n")

    await send_recv(get_initialize_lsp_msg())
    #await send_recv(get_document_symbols_msg('sample01.cls'))
    src_code_file = '/tmp/lsp/vba/sample01.cls'
    with open(src_code_file, 'r') as f:
        code_str = f.read()
    close_msg, open_msg, change_msg = get_open_document_on_lsp_server_msg(src_code_file, code_str)
    #await send_recv(change_msg)
    #await send_recv(close_msg)
    await send_recv(open_msg)
    await send_recv(get_document_symbols_msg(src_code_file))
    #await send_recv(close_msg)
    await websocket.close()

asyncio.run(client('ws://localhost:3000/vbaLspSampleServer'))  