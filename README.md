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