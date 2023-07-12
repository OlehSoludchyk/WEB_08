import sys


from insert import *
from models import Authors, Quotes, Q


while True:
    user_input = input('Please, enter a command for search smth: ')
    if user_input == 'exit':
        sys.exit()

    splited = user_input.split(': ')
    request1 = splited[0]
    request2 = splited[1]

    if request1 == 'name':
        author_quotes = Authors.objects(fullname=request2).first()
        quotes = Quotes.objects(author=author_quotes)
        for quote in quotes:
            print(quote.quote)
    elif request1 == 'tag':
        quotes = Quotes.objects(tags=request2)
        for quote in quotes:
            print(quote.quote)
    elif request1 == 'tags':
        tags = request2.split(',')
        quotes = Quotes.objects(Q(tags__in=tags))
        for quote in quotes:
            print(quote.quote)

    else:
        print('Invalid command, try again.')