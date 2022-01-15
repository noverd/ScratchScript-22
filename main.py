from lexer import Lexer

text_input = "'STRING'"  # Тут строка которую нужно проверить

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
for token in tokens:
    print(token)
