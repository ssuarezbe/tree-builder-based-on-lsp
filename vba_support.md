

Lets try to use:

https://github.com/SSlinky/VBA-LanguageServer/blob/master/server/src/server.ts

We need nodeenv to start the nodejs server:

https://github.com/SSlinky/VBA-LanguageServer


# Getting started

* Install [nodeenv](https://github.com/ekalinin/nodeenv)

  ```bash
  $ mkvirtualenv nodeenv-base
  $ pip install nodeenv
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
  ```

* Install typescript compiler ` npm install node-typescript`

* Compile the project

```bash
$ cd VBA-LanguageServer
$ npm install antlr4
$ npm -i
$ npm i @vscode/test-electron
$ npx tsc -b # npm compile
$ npm test
```