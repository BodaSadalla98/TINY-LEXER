import sys
import enum
import string


class Lexer:
    def __init__(self, input):
        self.input = input + "\0"  # Add EOF flag in case the input doesn't have one
        self.curChar = ""
        self.index = -1
        self.nextChar()

    # gets the next char in the input
    def nextChar(self):
        self.index += 1
        if self.index >= len(self.input):
            self.curChar == "\0"  #  End of File flag
        else:
            self.curChar = self.input[self.index]

    # skips whitespaces and taps
    def skipWhiteSpace(self):
        while self.curChar == " " or self.curChar == "\t" or self.curChar == "\r":
            self.nextChar()

    # peeks into the char that moves after the next one. ex peek(moves = 1) get the char that is rightg after the cur one
    def peek(self, moves):
        if self.index + moves >= len(self.input):
            return "\0"
        else:
            return self.input[self.index + moves]

    # skips x charachters
    def skip(self, x):
        self.index += x

    @staticmethod
    def isKeyword(text):
        text = text.upper()
        for type in TokenType:
            if type.value in range(100, 201) and text == type.name:
                return type
        return False

    # gets the current token
    def getToken(self):
        token = None
        value = ""
        self.skipWhiteSpace()  # Skip the whitespaces till u reach the start of the token

        if self.curChar == "/":  # This could be begin of a comment or a divide
            if (
                self.peek(1) == "*" and self.peek(2) == "*"
            ):  # then this is start of a comment
                self.skip(2)  # skips the next two char
                self.nextChar()
                while self.curChar != "*":
                    value += self.curChar
                    self.nextChar()

                value.strip()
                token = Token(TokenType.COMMENT, value)
                self.skip(2)  # skip the next two char
            else:
                token = Token(TokenType.DIV, "/")  # Divide token

        elif self.curChar == "+":
            token = Token(TokenType.PLUS, "+")  # PLUS token

        elif self.curChar == "-":
            token = Token(TokenType.MINUS, "-")  # MINUS token

        elif self.curChar == "*":
            token = Token(TokenType.MULT, "*")  # MULT token

        elif self.curChar == "=":
            token = Token(TokenType.EQUAL, "=")  # Equal Token

        elif self.curChar == "\n":  # Newline Token
            token = Token(TokenType.NEWLINE, value)

        elif self.curChar == "\0":  # End of file Token
            token = Token(TokenType.EOF, value)

        elif self.curChar == ";":  # Semicolon Token
            token = Token(TokenType.SEMICOLON, ";")
        elif self.curChar == ",":  # Comma Token
            token = Token(TokenType.COMMA, ",")

        elif self.curChar == "(":  # Open Bracket Token
            token = Token(TokenType.OPENBRACKET, "(")

        elif self.curChar == ")":  # Open Bracket Token
            token = Token(TokenType.CLOSEDBRACKET, ")")

        elif self.curChar == "<":
            if self.peek(1) == "=":  # Less Than or Eq Token
                token = Token(TokenType.LESSTHANEQ, "<=")
                self.skip(1)
            else:  # Less than Token
                token = Token(TokenType.LESSTHAN, "<")

        elif self.curChar == ":" and self.peek(1) == "=":  # Assign Token
            self.skip(1)
            token = Token(TokenType.ASSIGN, ":=")

        elif self.curChar.isalpha():
            while self.curChar.isalnum():
                value += self.curChar
                if self.peek(1).isalnum():
                    self.nextChar()
                else:
                    break
            if self.isKeyword(value) != False:
                token = Token(self.isKeyword(value), value)  # Keyword Token
            else:
                token = Token(TokenType.IDENTIFIER, value)  # Identifier Token

        elif self.curChar.isdigit():  # Number Token
            while self.curChar.isdigit():
                value += self.curChar
                if self.peek(1).isdigit():
                    self.nextChar()
                else:
                    break
            token = Token(TokenType.NUMBER, value)

        else:
            token = Token(TokenType.UNKNOWN_TOKEN, self.curChar)

        self.nextChar()
        return token


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENTIFIER = 2
    COMMENT = 3
    UNKNOWN_TOKEN = 4
    # Keywords.
    WRITE = 101
    READ = 102
    IF = 103
    ELSE = 104
    RETURN = 105
    BEGIN = 106
    END = 107
    MAIN = 108
    STRING = 109
    INT = 110
    REAL = 111
    THEN = 112
    REPEAT = 113
    UNTIL = 114
    # Operators.
    EQUAL = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LESSTHAN = 208
    LESSTHANEQ = 209
    GT = 210
    GTEQ = 211
    ASSIGN = 212
    DIV = 213
    MULT = 214
    # Seperators
    SEMICOLON = 301
    COMMA = 302
    OPENBRACKET = 303
    CLOSEDBRACKET = 304
