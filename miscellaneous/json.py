import pyparsing as pp
import json

# Define the context-free grammar
json_grammar = pp.Forward()
object_grammar = pp.Dict(pp.ZeroOrMore(pp.Suppress(",") + pp.Group(pp.QuotedString('"') + pp.Suppress(":") + json_grammar)))
json_grammar << pp.Dict(pp.Suppress("{") + object_grammar + pp.Suppress("}")) | pp.Group(pp.Suppress("[") + pp.ZeroOrMore(json_grammar) + pp.Suppress("]")) | pp.QuotedString('"') | pp.Regex(r'-?\d+(\.\d*)?([eE][+-]?\d+)?') | pp.Keyword("true") | pp.Keyword("false") | pp.Keyword("null")

# Define the JSON string to parse
json_string = '{"name": "John Doe", "age": 30, "isStudent": false, "grades": [3.2, 4.0, 3.7]}'

# Parse the JSON string using the grammar
parsed_json = json.loads(json.dumps(json_grammar.parseString(json_string).asDict()))

# Print the parsed JSON
print(parsed_json)
