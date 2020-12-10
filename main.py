from lexer import *

def main():
    input = "/** sdfs sdfdsf dsf ds **/ \t \r  \r\r\r\r\r/** another comment **/ +-*/*"
    lex = Lexer(input)
    t = lex.getToken()
    while t.type != TokenType.EOF:
        print(t.type, t.value)
        t = lex.getToken()

if __name__ == '__main__':
    main()
    
