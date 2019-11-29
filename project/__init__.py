from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()


from project.views.node_view import node_blueprint
from project.views.map_view import map_blueprint
from project.views.topic_view import topic_blueprint
from project.views.sticker_view import sticker_blueprint

app.register_blueprint(node_blueprint,url_prefix="/node")
app.register_blueprint(map_blueprint,url_prefix="/map")
app.register_blueprint(topic_blueprint,url_prefix="/topic")
app.register_blueprint(sticker_blueprint,url_prefix="/sticker")