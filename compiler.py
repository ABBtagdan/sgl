from lexer import Lexer
from parse import Parser
from gen import Generator
import sys

def main():
    p = sys.argv[1]
    file = p
    lex = Lexer(file)
    gen = Generator(p+".html")
    tokens = lex.tokenize()
    parse = Parser(tokens, gen)
    try:
        parse.program()
    except SystemExit as e:
        print(e)
        
if __name__ == "__main__":
    main()