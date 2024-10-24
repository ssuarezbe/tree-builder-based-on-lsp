

```bash
$ PYTHONPATH=. python -m pdb mechanized/src/tree_sitter_chunker/tests/js/test_code_segmentation_js.py
> /mnt/c/Users/ssuar/Documents/mechanized/mlops-user-account-lambdas/src/mechanized/src/tree_sitter_chunker/tests/js/test_code_segmentation_js.py(1)<module>()
-> from mechanized.src.tree_sitter_chunker.chunker import SupportedLanguage, TreeSitterChunker, CodeSegment
(Pdb) c
2024-10-21 17:56:06 - mechanized.src.base.base_chunker - DEBUG - Initialized BaseChunker with language: javascript, encoding: utf-8, max_chars: 5000, char_byte_size: 1
> /mnt/c/Users/ssuar/Documents/mechanized/mlops-user-account-lambdas/src/mechanized/src/tree_sitter_chunker/chunker.py(147)process_node()
-> node_size = child.end_byte - child.start_byte
(Pdb) hel´p
*** SyntaxError: invalid character '´' (U+00B4)
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) p
*** SyntaxError: invalid syntax
(Pdb) p child
<Node type=import_statement, start_point=(0, 0), end_point=(0, 23)>
(Pdb) pp
*** SyntaxError: invalid syntax
(Pdb) pp child
<Node type=import_statement, start_point=(0, 0), end_point=(0, 23)>
(Pdb)
```