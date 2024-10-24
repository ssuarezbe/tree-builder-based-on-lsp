# Understand tree structure for AST

To build a code chunker based on AST , it is important to understand the underneath data structure
so we can build correct code-chunks.

* https://symflower.com/en/company/blog/2023/parsing-code-with-tree-sitter/
* https://stackoverflow.com/questions/48524059/how-to-flatten-tree-structure-into-array-of-arrays


# tree-builder-based-on-lsp

Dependencies:

* https://github.com/PurpleMyst/sansio-lsp-client


# Get Started


* Install neovim 
    * https://github.com/neovim/neovim/blob/master/INSTALL.md

Best way to go about installing LSP today? 

* https://www.reddit.com/r/neovim/comments/y2rwcf/best_way_to_go_about_installing_lsp_today/    

Make sure you neovim local installation is ready to install neovim-pluings:

* https://stackoverflow.com/questions/48700563/how-do-i-install-plugins-in-neovim-correctly

## Installing vim-plug

```bash
# Ubuntu
$ sudo apt install git
$ curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

Edit the `init.vim`.

```bash 
nano ~/.config/nvim/init.vim
```
Put the content below inside the `init.vim`. 

```bash
call plug#begin('~/.local/share/nvim/plugged')

call plug#end()
```

For example, to add this [vim-surround](https://github.com/tpope/vim-surround), Edit the `init.vim` to look like this:

```bash
call plug#begin('~/.local/share/nvim/plugged')

Plug 'tpope/vim-surround'  "Surround.vim is all about \"surroundings\": parentheses, brackets, quotes, XML tags, and more. The plugin provides mappings to easily delete, change and add such surroundings in pairs.

call plug#end()
```

Now, reload the vim config and the install the plugins. Start `nvim` first and then


Load the config
```bash
:so ~/.config/nvim/init.vim
```
Install the plugins listed in `init.vim`.
```bash
:PlugInstall
```


## 10 minutes setup using lsp-zerp

* Install neovim 
    * https://github.com/neovim/neovim/blob/master/INSTALL.md
* Install neovim LSP server
    * https://github.com/williamboman/mason.nvim
* bb
    * https://lsp-zero.netlify.app/docs/getting-started.html
    ```bash
    Plug 'neovim/nvim-lspconfig'
    Plug 'hrsh7th/nvim-cmp'
    Plug 'hrsh7th/cmp-nvim-lsp'
    Plug 'VonHeikemen/lsp-zero.nvim', {'branch': 'v4.x'}
    ```

# Language support

A LSP server based on [mason.nvim](https://github.com/williamboman/mason.nvim) support a lot of language. EXCEPT VB6, visual basic, and visual script 

* https://github.com/neovim/nvim-lspconfig/blob/master/doc/configs.md

other LSP servers:

* https://lsp.sublimetext.io/language_servers/

## VB6 Visual Basic

TwinBasic is an alternative to VB6. 
https://nolongerset.com/twinbasic-update-september-24-2023/

twinBASIC (along with the Monaco editor) would replace VBA (Maybe)

Here is a LSP PoC for VBA:

* https://github.com/SSlinky/VBA-LanguageServer

For VB6 support check Rubberduck3.

* https://github.com/rubberduck-vba/Rubberduck3 
* https://github.com/rubberduck-vba/Rubberduck


# Interals

This code works by sending a API request to LSP server.

That request is [textDocument/documentSymbol](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentSymbol)

* Build the LSP server. Make sure all the required dependencies are installed: 
    * https://github.com/rubberduck-vba/Rubberduck3/blob/main/Server/Rubberduck.LanguageServer/Rubberduck.LanguageServer.csproj 

## Run LSP server locally

https://stackoverflow.com/questions/56108617/how-to-pass-arguments-in-command-line-using-dotnet

Check the LSP client to understand how start an LSP server

https://github.com/rubberduck-vba/Rubberduck3/blob/main/Client/Rubberduck.Editor/LanguageClientApp.cs   

```bash 
$ cd Server\Rubberduck.LanguageServer
$ dotnet run 
```