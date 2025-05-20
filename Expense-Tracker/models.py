from peewee import Model, IntegerField, CharField, DateField, BooleanField, UUIDField
from uuid import uuid4
from conf import DATABASE as db


class BaseModel(Model):
    class Meta:
        database = db


class Lend(BaseModel):
    id = UUIDField(primary_key=True, default=uuid4, unique=True, index=True)
    to = CharField()
    amount = IntegerField()
    description = CharField()
    repayed = BooleanField(default=False)
    date = DateField(formats='%d-%m-%Y')


class Borrow(BaseModel):
    id = UUIDField(primary_key=True, default=uuid4, unique=True, index=True)
    whom = CharField()
    amount = IntegerField()
    description = CharField()
    repayed = BooleanField(default=False)
    date = DateField(formats='%d-%m-%Y')
