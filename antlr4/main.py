import antlr4_tool_runner as antlr4_tool
import os
import sys

def build_grammar(grammar_path:str):
    """
    """
    entrypoint = 'org.antlr.v4.gui.Interpreter'
    version = os.environ.get("ANTLR4_TOOLS_ANTLR_VERSION") or antlr4_tool.latest_version()
    antlr4_tool.initialize_paths()
    grammar_file = os.path.join(grammar_path,'vba.g4')
    args = [grammar_file]
    jar, java = antlr4_tool.install_jre_and_antlr(version)
    call_args = [java, '-cp', jar, entrypoint] + args
    print(f" Running call_args={call_args}")
    cp = antlr4_tool.subprocess.run(call_args)
    sys.exit(cp.returncode)

def get_tokens():
    """
    Call example bash:

    $ antlr4-parse vba.g4 module EOF input-filename /tmp/lsp/vba/sample01.cls -tokens
    """
    return None


grammar_path = os.path.dirname(__file__)  
#grammar_path = os.path.join(current_folder,'code_samples','setup.py')
build_grammar(grammar_path)