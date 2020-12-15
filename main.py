from lexer import *


def main():

    input_string = open("input.txt", "r").read()
    out_file = open("out.txt", "w")
    lex = Lexer(input_string)
    t = lex.getToken()

    while t.type != TokenType.EOF:
        # print(t.value, t.type)
        if t.type != TokenType.NEWLINE:
            s = t.value + ", " + t.type.name + "\n"
            out_file.write(s)
        t = lex.getToken()

    out_file.close()


if __name__ == "__main__":
    main()
