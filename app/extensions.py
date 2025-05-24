from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate

# Instâncias das extensões
db = SQLAlchemy()
bootstrap = Bootstrap5()
migrate = Migrate()