


import csv
import click


from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
