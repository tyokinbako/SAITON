from peewee import *

db = SqliteDatabase('Chat.db')

class Chat(Model):
    name = CharField()
    message = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.s


db.create_tables([Chat])