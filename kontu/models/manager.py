import peewee


class Project(peewee.Model):
    name = peewee.CharField()
