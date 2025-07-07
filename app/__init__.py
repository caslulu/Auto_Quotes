from flask import Flask
from app.extensions import db, bootstrap, migrate
from app.routes.cotacao_routes import cotacao_bp
from app.routes.cotar_routes import cotar_bp
from app.routes.preco_routes import colocarPreco_bp
from app.routes.apagar_routes import apagar_bp
from app.routes.editar_routes import editar_bp
from app.routes.rta_routes import rta_bp
from app.routes.duplicar_routes import duplicar_bp
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cotacao_bp, url_prefix='/')
    app.register_blueprint(cotar_bp)
    app.register_blueprint(colocarPreco_bp)
    app.register_blueprint(apagar_bp, url_prefix='/')
    app.register_blueprint(editar_bp, url_prefix='/')
    app.register_blueprint(rta_bp)
    app.register_blueprint(duplicar_bp)

    with app.app_context():
        db.create_all()

    return app