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
    args = [grammar_file,'-o',grammar_path]
    jar, java = antlr4_tool.install_jre_and_antlr(version)
    #call_args = [java, '-cp', jar, entrypoint] + args
    call_args = ['antlr4'] + args
    print(f" Running call_args={call_args}")
    cp = antlr4_tool.subprocess.run(call_args)
    sys.exit(cp.returncode)

def get_tokens(grammar_path:str):
    """
    Call example bash:

    $ antlr4-parse vba.g4 module EOF input-filename /tmp/lsp/vba/sample01.cls -tokens
    """
    #entrypoint = 'org.antlr.v4.gui.Interpreter'
    version = os.environ.get("ANTLR4_TOOLS_ANTLR_VERSION") or antlr4_tool.latest_version()
    antlr4_tool.initialize_paths()
    grammar_file = os.path.join(grammar_path,'vba.g4')
    start_rule_name = "EOF"
    code_file = os.path.join(grammar_path,'..','code_samples','vba', 'sample01.cls')
    out_args = ['>', os.path.join(grammar_path,'tokens.out')]
    call_args = ['antlr4-parse', grammar_file,'module','EOF','input-filename',code_file,'-tokens']+out_args
    print(f" Running call_args={call_args}")
    cp = antlr4_tool.subprocess.run(call_args)
    sys.exit(cp.returncode)


grammar_path = os.path.dirname(__file__)  
#grammar_path = os.path.join(current_folder,'code_samples','setup.py')
#build_grammar(grammar_path)
get_tokens(grammar_path)