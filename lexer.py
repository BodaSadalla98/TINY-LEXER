import sys
import enum
import string
class Lexer:
    def __init__(self,input):
        self.input = input + '\0' # Add EOF flag in case the input doesn't have one
        self.curChar = ''
        self.index = -1
        self.nextChar()

    # gets the next char in the input
    def nextChar(self):
        self.index +=1
        if self.index == len(self.input):
            self.curChar == '\0' #  End of File flag
        else:
            self.curChar = self.input[self.index]

    # skips whitespaces and taps
    def skipWhiteSpace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':  
            self.nextChar()

    # peeks into the char that moves after the next one. ex peek(moves = 1) get the char that is rightg after the cur one 
    def peek(self, moves):
        if self.index + moves >= len(self.input):
            return '\0'
        else:
           return self.input[self.index + moves]

    # skips x charachters     
    def skip(self, x):
        self.index += x

    # gets the current token 
    def getToken(self):
        token = None
        value = ""
        self.skipWhiteSpace() # Skip the whitespaces till u reach the start of the token 
        cur = self.curChar

        if cur == '/':        # This could be begin of a comment or a divide
            if self.peek(1) == '*' and self.peek(2) == '*': # then this is start of a comment 
                self.skip(2) # skips the next two char
                self.nextChar()
                while self.curChar!= '*':
                    value += self.curChar
                    self.nextChar()
                    
                value.strip()
                token = Token(TokenType.COMMENT, value)
                self.skip(2) # skip the next two char
            else:
                token = Token(TokenType.DIVIDE, '/') # Divide token

        elif cur == '+':
                token = Token(TokenType.PLUS, '+') # PLUS token
        elif cur == '-':
                token = Token(TokenType.MINUS, '-') # MINUS token
        elif cur == '*':
                token = Token(TokenType.MULT, '*') # MULT token

        elif self.curChar == '\n': # Newline Token
            token = Token( TokenType.NEWLINE, value)
        elif self.curChar == '\0': # End of file Token
            token = Token(TokenType.EOF, value)

        self.nextChar()
        return token


class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value


    

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE =0
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
    # Operators.
    EQ = 201  
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
    ASSIGN = 212
    DIVIDE = 213
    MULT = 214
    # Seperators 
    SEMICOLON = 301
    COMMA = 302
    LEFTPARENTH = 303
    RIGHTPARENTH = 304 