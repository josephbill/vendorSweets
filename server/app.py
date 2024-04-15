#!/usr/bin/env python3
from models.dbmodel import db
from flask_migrate import Migrate
from routes import create_app


app = create_app()

app.json.compact = False

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
