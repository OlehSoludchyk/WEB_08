from mongoengine import *
from mongoengine.fields import StringField, ReferenceField, ListField
from mongoengine import Q


try:
    connect(db='MyDB', host='mongodb+srv://olehsolo:567234@cluster0.4hxjc4g.mongodb.net/?retryWrites=true&w=majority')
    print("Connected to the database successfully!")
except Exception as e:
    print("Error connecting to the database:")
    print(e)




class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()


class Quotes(Document):
    quote = StringField()
    author = ReferenceField(Authors)
    tags = ListField(StringField())


Authors.drop_collection()
Quotes.drop_collection()