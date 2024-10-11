

Lets try to use:

https://github.com/SSlinky/VBA-LanguageServer/blob/master/server/src/server.ts

We need nodeenv to start the nodejs server:

https://github.com/SSlinky/VBA-LanguageServer


# How install VScode extension from github

* https://code.visualstudio.com/api/working-with-extensions/publishing-extension#packaging-extensions
* https://stackoverflow.com/questions/50714638/install-extension-from-a-specific-repo-branch-on-github

```bash
npm install -g vsce
# go to the local extension-repo
npm i # build the extension locally
vsce package  # Generates a .vsix file
code --install-extension lsp-sample-1.0.0.vsix 
```

WARNING: To build the extension locally the publisher name must be changed 

```diff
diff --git a/lsp-sample/package.json b/lsp-sample/package.json
index 58336427..1d40269c 100644
--- a/lsp-sample/package.json
+++ b/lsp-sample/package.json
@@ -8,7 +8,7 @@
                "type": "git",
                "url": "https://github.com/Microsoft/vscode-extension-samples"
        },
-       "publisher": "vscode-samples",
+       "publisher": "Local-test",
        "categories": [],
        "keywords": [
                "multi-root ready"
```

After installing the extension, check if it was installed locally:

```bash
code --list-extensions
```

# Getting started



```bash
node i vscode-languageserver
```

Compile the server:

```bash
npx tsc -b -w
```

# Building the server locally 

* Install [nodeenv](https://github.com/ekalinin/nodeenv)

  ```bash
  $ mkvirtualenv nodeenv-base
  $ pip install nodeenv
  ```

* install https://github.com/antlr/antlr4-tools
  ```bash
  pip install antlr4-tools --break-system-packages
  ```

* install a system wide JRE:
  
  ```bash
  sudo apt install default-jre
  ```

* install the required nodejs version

  ```bash
  $ nodeenv --node=20.18.0 --prebuilt env-20.18.0-prebuilt
  ```
* Active the created nodenev `. env-20.18.0-prebuilt/bin/activate`
* Check the nodejs version 
  
  ```bash
  $ node -v
  v20.18.0
  $ cd VBA-LanguageServer
  $ npm -i .
  ```

* Test that the grammar works locally `npm run antlr4ng`

## Compile the project

In VS Code, a [language server](https://code.visualstudio.com/api/language-extensions/language-server-extension-guide) has two parts:

    * Language Client: A normal VS Code extension written in JavaScript / TypeScript. This extension has access to all VS Code Namespace API.
    * Language Server: A language analysis tool running in a separate process.


```bash
$ cd VBA-LanguageServer
$ npm install antlr4
$ npm i
$ npm run antlr4ng
$ npm run compile
$ # install https://github.com/microsoft/vscode-extension-samples/tree/main/lsp-sample
$ git clone git@github.com:microsoft/vscode-extension-samples.git 
$ cd vscode-extension-samples
$ cd lsp-sample/
$ npm install # install depdency 
$ cd ..
$ code lsp-sample/
$ npm install
$ # install the test-suite for vscode
$ npm i @vscode/test-electron
$ npx tsc -b # npm compile
$ code . # check vscode is available for running test https://code.visualstudio.com/docs/remote/wsl-tutorial
$ alias code="/mnt/c/Users/ssuar/AppData/Local/Programs/Microsoft\ VS\ Code/Code.exe" # enable VS Code launch from WSL: https://stackoverflow.com/questions/43640023/launch-vs-code-from-wsl-bash
$ npm test
```

* Funny story  .... antlr4 supports VB6 
    * https://github.com/antlr/grammars-v4/tree/master/vb6
    * https://github.com/antlr/grammars-v4/tree/master/vba
    * https://github.com/antlr/grammars-v4 


# Useful npm tools

* https://www.npmjs.com/package/rimraf
  * as part of the package.json can be used to remove the out or dist folder `rimraf out && npx tsc`
  * How To Use TypeScript With Express & Node.   
* Example of vscode-languageserver
  * https://github.com/microsoft/vscode-extension-samples/blob/main/lsp-sample/server/src/server.ts
  * https://code.visualstudio.com/api/language-extensions/language-server-extension-guide
* Named pipes are little bit faster than sockets
  * https://supermarket.chef.io/tools/node-js-and-python-integration-powering-versatile-and-scalable-applications
  * https://stackoverflow.com/questions/1235958/ipc-performance-named-pipe-vs-socket 
* Using pipes to make Python and Nodejs work using IPC
  * https://shyamswaroop.hashnode.dev/ipc-between-nodejs-python