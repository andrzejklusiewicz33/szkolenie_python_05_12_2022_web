import app
from flask_sqlalchemy import SQLAlchemy

def test():
    app.db.create_all()
    print('ok')

class Fruit:
    __tablename__="fruits"
    fruit_id=app.db.Column(app.db.Integer,name="fruit_id",primary_key=True)
    fruit_name=app.db.Column(app.db.String,name="fruit_name",nullable=False)
