from peewee import SqliteDatabase, Model, CharField, BooleanField, PrimaryKeyField

db = SqliteDatabase("data.db")


class TaskEntity(Model):
    id = PrimaryKeyField()
    title = CharField()
    description = CharField()
    completed = BooleanField(default=False)

    class Meta:
        table_name = "tasks"
        database = db


db.create_tables(models=[TaskEntity], safe=True)
