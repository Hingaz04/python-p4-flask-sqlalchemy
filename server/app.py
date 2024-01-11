#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Create the SQLAlchemy instance
db = SQLAlchemy(app)

# Initialize the migration
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5555)
