from tmengine import TextMateEngine
import json
import os

current_path = os.path.dirname(__file__) 
grammar_file = os.path.join(current_path, 'syntaxes/jcl.tmLanguage.json')
print(f"grammar_file={grammar_file}")
with open(grammar_file, 'r') as f:
    engine2 = TextMateEngine(json.load(f)) 
    print(engine2.languages)