import peewee
from peewee import SqliteDatabase
import datetime

db = SqliteDatabase("exchange.db")


class XRate(peewee.Model):
    class Meta:
        database = db
        db_table = "xrates"
        indexes = (
            (("from_currency", "to_currency"), True),
        )

    from_currency = peewee.IntegerField()
    to_currency = peewee.IntegerField()
    rate = peewee.DoubleField()
    updated = peewee.DateTimeField(default=datetime.datetime.now)

