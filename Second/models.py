from mongoengine import Document, connect, BooleanField, StringField

connect(db='MyDB', host="mongodb+srv://olehsolo:567234567234@cluster0.4hxjc4g.mongodb.net/?retryWrites=true&w=majority")


class Contact(Document):
    completed = BooleanField(default=False)
    consumer = StringField()
    email = StringField()