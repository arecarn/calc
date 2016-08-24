import re
from collections import OrderedDict

TOKEN_MAP = OrderedDict([
    (r'\d+([.]\d+)?|.\d+', 'num'),
    (r'[*]', 'mul'),
    (r'/', 'mul'),
    (r'\-', 'add'),
    (r'\+', 'add'),
    (r'.*', 'unknown'),
])

def tokenize(input_string, tokens):
    output = []
    string = input_string
    while len(string) != 0:
        for regex_str, token_id in tokens.items():
            match = re.match(regex_str, string)
            if match != None:
                match_str = match.group()
                match_str_len = len(match_str)
                output.append((match.group(), token_id))
                string = string[match_str_len:]
                break
    return output

def main():
    while True:
        user_input = input('> ')
        output = tokenize(user_input, TOKEN_MAP)
        print(output)

if __name__ == '__main__':
    main()
