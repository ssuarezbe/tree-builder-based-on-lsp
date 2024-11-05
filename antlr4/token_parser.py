from typing import List
import pyparsing as pp

class TokenTypeParseAction(object):
    """
    Parser designed to parser string like: 

    <'CONST'>
    <WS>
    <EOF>
    <'INTEGER'>
    """
    def __init__(self,tokens) -> None:
        if len(tokens[0]) > 3:
            # the optional "'" were present
            self.value = tokens[0][2].replace("'","")
        else:
            self.value = tokens[0][1]

    def generate(self):
        return self.value


class TokenValueParseAction(object):
    """
    Parser designed to parser string like: 

    0:4='Const',<'CONST'>
    5:5=' ',<WS>
    936:935='<EOF>',<EOF>
    24:30='Integer',<'INTEGER'>
    """
    def __init__(self,tokens) -> None:
        self.start_byte = tokens[0][0]
        self.end_byte = tokens[0][2]
        self.content = tokens[0][5]
        self.type = tokens[0][8]

    def generate(self):
        "".join(( self.start_byte, self.end_byte, self.content, self.type.generate()))


class TokenRowParseAction(object):
    """
    Parser designed to parser string like: 

    [@6,24:30='Integer',<'INTEGER'>,1:24]
    [@366,932:932=' ',<WS>,41:3]
    [@367,933:935='Sub',<'SUB'>,41:4]
    [@368,936:935='<EOF>',<EOF>,41:7]
    """
    def __init__(self,tokens) -> None:
        print(f"--> row_tokens = {tokens}")
        self.token_number = tokens[0][2]
        self.token = tokens[0][4]
        self.file_line = tokens[0][6]
        self.file_col = tokens[0][8]
        

    def generate(self):
        "".join(( self.token_number, self.token_row.gnerate()))

# Common Pitfalls When Writing Parsers
# https://github.com/pyparsing/pyparsing/wiki/Common-Pitfalls-When-Writing-Parsers
# Gentle intro to pyparsing
# https://dev.to/zchtodd/building-parsers-for-fun-and-profit-with-pyparsing-4l9e
# Read more about quoted string:
#   https://stackoverflow.com/questions/32148790/using-quotedstring-in-pyparsing
"""
== token type parser ==
"""
type_identifier = pp.Word( pp.alphanums + "_"+ '='+")"+"("+",", exclude_chars="'").set_name("type_identifier")
angleQuoteString = pp.QuotedString('<', endQuoteChar='>')
token_type_cls_word = pp.Group(pp.delimitedList(angleQuoteString))
token_type_parser = token_type_cls_word.setParseAction(TokenTypeParseAction)
"""
== token value parser ==
"""
simpleQuoteString = pp.QuotedString("'")
code_token_value = pp.Group(pp.delimitedList(simpleQuoteString)).set_name("code_token_value")
token_str_quotes = ( pp.Char("'") )
token_value_word = pp.Group(
     pp.Word(pp.nums) + pp.Char(":") + pp.Word(pp.nums)
     + pp.Char("=") 
     + code_token_value 
     + pp.Char(",") + token_type_parser
)
token_value_parser = token_value_word.setParseAction(TokenValueParseAction)
"""
== token value parser ==
"""
token_row_word = pp.Group(
    pp.Char("[") + pp.Char("@") + pp.Word(pp.nums) + pp.Char(",")
    + token_value_parser
    + pp.Char(",") + pp.Word(pp.nums) + pp.Char(":") + pp.Word(pp.nums)
    + pp.Char("]")
)
token_row_parser = token_row_word.setParseAction(TokenRowParseAction)



def parse_token_type(value:str):
    """
    How debug unexpected behaviour

    * https://stackoverflow.com/questions/7560583/parseexception-expected-end-of-text
    """
    return token_type_parser.parseString(value, parseAll=True)

def parser_token_value(value:str):
    return token_value_parser.parseString(value, parseAll=True)

def parser_token_row(value:str):
    return token_row_parser.parseString(value, parseAll=True)



if __name__ == "__main__":
    tokens_types_values = ["<'INTEGER'>","<EOF>","<IDENTIFIER>","<WS>","<'AS'>"]
    print("*** Test tokens types ***")
    for v in tokens_types_values:
        print(f"processing v={v}")
        r = parse_token_type(v)
        print("type=",r[0].value)
    token_values = ["936:935='<EOF>',<EOF>", "6:19='PARMFLAG_CONST',<IDENTIFIER>", "21:22='As',<'AS'>"]
    print("\n*** Test tokens values ***")
    for v in token_values:
        print(f"Processing v={v}")
        r = parser_token_value(v)
        print(r)
        print(r[0].start_byte,"|", r[0].end_byte,"|", r[0].content,"|", r[0].type.value )
        print("-----------------------------")
    rows = [
        "[@0,0:4='Const',<'CONST'>,1:0]",
        "[@1,5:5=' ',<WS>,1:5]",
        "[@2,6:19='PARMFLAG_CONST',<IDENTIFIER>,1:6]",
        "[@3,20:20=' ',<WS>,1:20]",
        "[@4,21:22='As',<'AS'>,1:21]",
        "[@5,23:23=' ',<WS>,1:23]",
        "[@6,24:30='Integer',<'INTEGER'>,1:24]",
        "[@366,932:932=' ',<WS>,41:3]",
        "[@367,933:935='Sub',<'SUB'>,41:4]",
        "[@368,936:935='<EOF>',<EOF>,41:7]"
    ]
    print("\n*** Test tokens ROWS ***")
    for v in rows:
        print(f"Processing v={v}")
        print(dict(enumerate(v)))
        r = parser_token_row(v)
        print(r)
        print(r[0].token_number,"|", r[0].token.content,"|", r[0].token.type.value )
        print("-----------------------------")