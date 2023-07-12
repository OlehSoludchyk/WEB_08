import json

from models import *


with open('authors.json', 'r', encoding='utf-8') as a_file:
    json_data = a_file.read()
    data_authors = json.loads(json_data)

for line in data_authors:
    author_fullname = line['fullname']
    author_born_date = line['born_date']
    author_born_location = line['born_location']
    author = Authors(fullname=author_fullname, born_date=author_born_date, born_location=author_born_location)
    author.save()

with open('quotes.json', 'r', encoding='utf-8') as q_file:
    json_data = q_file.read()
    data_quotes = json.loads(json_data)

for line in data_quotes:
    author_quote = line['quote']
    quote_tags = line['tags']
    author_fullname = line['author']
    author = Authors.objects(fullname=author_fullname).first()
    quote = Quotes(quote=author_quote, author=author, tags=quote_tags)
    quote.save()