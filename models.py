import peewee
from peewee import SqliteDatabase
import datetime
from config import DB_NAME

db = SqliteDatabase(DB_NAME)


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

    def __str__(self):
        return "XRate(%s=>%s): %s" % (self.from_currency, self.to_currency, self.rate)


def init_db():
    db.drop_tables(XRate)
    XRate.create_table()
    XRate.create(from_currency=840, to_currency=980, rate=1)
    print("db created!")

