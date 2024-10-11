

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