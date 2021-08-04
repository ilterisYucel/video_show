from db import db

class Videos(db.Model):
    id = db.Column('id', db.Integer(), primary_key = True)
    name = db.Column('name', db.String(100))
    path = db.Column('path', db.String(100))
    def __init__(self, name, path):
        self.name = name
        self.path = path
    