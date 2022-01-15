from rply import LexerGenerator

# Тут сам лексер
class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('MOVE', r'move') #после r регулярные выржания, познакомся с ними
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('MOD', r'\%')
        # Number
        self.lexer.add('INT', r'^[-+]?\d+$')
        self.lexer.add('STRING', r"(?<=').+(?=')")
        self.lexer.add('NUMBER', r'[-+]?[0-9]*\.?[0-9]+')
        # Ignore spaces
        self.lexer.ignore('\s+')
        # self.lexer.ignore('\n+')
        # self.lexer.ignore('\\*.*?\\*/')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
