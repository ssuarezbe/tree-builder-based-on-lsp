

# LSP server connection interfaces

Example of LSP IPC server init:

https://snyk.io/advisor/npm-package/vscode-languageserver/functions/vscode-languageserver.createConnection


## Building LSP RPC server


* Difference between module type in tsconfig.json https://stackoverflow.com/questions/41326485/difference-between-module-type-in-tsconfig-json

* Problem while trying to compile the code in 

https://github.com/railsware/upterm/blob/1d04bcb6d5aec8f62e4025ddee4a77db8cc12c52/src/language-server/ShellLanguageServer.ts#L27

for the issue:

```bash
/mnt/c/Users/ssuar/Documents/mechanized/VBA-LanguageServer/server/out/rpc_server.js:7
const vscode_ws_jsonrpc_1 = require("vscode-ws-jsonrpc");
                            ^

Error [ERR_REQUIRE_ESM]: require() of ES Module /mnt/c/Users/ssuar/Documents/mechanized/VBA-LanguageServer/node_modules/vscode-ws-jsonrpc/lib/index.js from /mnt/c/Users/ssuar/Documents/mechanized/VBA-LanguageServer/server/out/rpc_server.js not supported.
Instead change the require of index.js in /mnt/c/Users/ssuar/Documents/mechanized/VBA-LanguageServer/server/out/rpc_server.js to a dynamic import() which is available in all CommonJS modules.
    at Object.<anonymous> (/mnt/c/Users/ssuar/Documents/mechanized/VBA-LanguageServer/server/out/rpc_server.js:7:29) {
  code: 'ERR_REQUIRE_ESM'
}

Node.js v20.18.0
```

https://stackoverflow.com/questions/65265420/how-to-prevent-typescript-from-transpiling-dynamic-imports-into-require


* https://github.com/TypeStrong/ts-node/discussions/1290    

* During tsc something like this can happen 
    * https://stackoverflow.com/questions/66554684/how-to-fix-property-has-no-initializer-and-is-not-definitely-assigned-in-the-co
        * https://github.com/microsoft/TypeScript/issues/51515 :
    * https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#the-usedefineforclassfields-flag-and-the-declare-property-modifier

```
 If this is intentional, add an initializer. Otherwise, add a 'declare' modifier or remove the redundant declaration.
```

# Building LSP client

* https://stackoverflow.com/questions/64000616/creating-lsp-language-server-protocol-for-multiple-clients-using-rpc


* RPC-JSON 
   * https://unautolab.com/posts/jsonrpc-lsp/

* A websocker upgrade event is handshake
   * https://www.rfc-editor.org/rfc/rfc6455#section-1.3
   * Python example: https://renewal-recsystems.readthedocs.io/en/latest/primer.html#websockets-example

## Python

### Webscoket RPC

* Websocket connections explained: https://medium.com/@louis.rosevi/python-web-sockets-5-different-ways-5ffb1a9015f9
* https://renewal-recsystems.readthedocs.io/en/latest/primer.html#websockets-example
* https://piehost.com/websocket/python-websocket


#### Building the LSP client

* https://tamerlan.dev/an-introduction-to-the-language-server-protocol/

### JSON RPC -- XX NOT WORKING

* https://pypi.org/project/json-rpc/

```python
# Needed imports
import json
import socket
import inspect
from threading import Thread

# rpc.py
class RPCServer:
    def __init__(self, host:str='0.0.0.0', port:int=8080) -> None:
        self.host = host
        self.port = port
        self.address = (host, port)
        self._methods = {}
```


### Python JSON-RPC-Client  -- XX NOT WORKING

* https://www.jsonrpcclient.com/en/3.2.0/api.html
* https://www.jsonrpcclient.com/en/stable/index.html
    * `pip install "jsonrpcclient[requests]"` ->  `jsonrpcclient==4.0.3`

# Inspecting LSP server

* https://github.com/Microsoft/language-server-protocol-inspector?tab=readme-ov-file

# Getting the code symbols from LSP server

* How interact with LSP server: https://stackoverflow.com/questions/55312875/guidance-to-writing-lsp-client

Each LSP can offer an capability called `documentSymbolProvider`.

[This capability](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#documentSymbolOptions) is available trough: 

* Request:
    * `method`: `textDocument/documentSymbol`
    * `params`: `DocumentSymbolParams` defined as follows:

```
textDocument/documentSymbol
```

* The nodejs LSP server interface looks like this

```javascript
/**
 * Registration options for a {@link DocumentSymbolRequest}.
 */
export interface DocumentSymbolRegistrationOptions extends TextDocumentRegistrationOptions, DocumentSymbolOptions {
}
/**
 * A request to list all symbols found in a given text document. The request's
 * parameter is of type {@link TextDocumentIdentifier} the
 * response is of type {@link SymbolInformation SymbolInformation[]} or a Thenable
 * that resolves to such.
 */
export declare namespace DocumentSymbolRequest {
    const method: 'textDocument/documentSymbol';
    const messageDirection: MessageDirection;
    const type: ProtocolRequestType<DocumentSymbolParams, DocumentSymbol[] | SymbolInformation[] | null, DocumentSymbol[] | SymbolInformation[], void, DocumentSymbolRegistrationOptions>;
}
```