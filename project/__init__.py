from flask import Flask, Blueprint
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import os
from sys import stderr

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config["CORS_HEADERS"] = "Content-Type"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, resources={r"/n": {"origins": "http://localhost:4200"}, 
r"/m": {"origins": "http://localhost:4200"},
r"/t": {"origins": "http://localhost:4200"},
r"/s": {"origins": "http://localhost:4200"},
r"/e": {"origins": "http://localhost:4200"}})

db = SQLAlchemy(app)
db.create_all()
    

from project.views.node_view import node_blueprint
from project.views.map_view import map_blueprint
from project.views.topic_view import topic_blueprint
from project.views.sticker_view import sticker_blueprint
from project.views.edge_view import edge_blueprint

app.register_blueprint(node_blueprint,url_prefix="/n")
app.register_blueprint(map_blueprint,url_prefix="/m")
app.register_blueprint(topic_blueprint,url_prefix="/t")
app.register_blueprint(sticker_blueprint,url_prefix="/s")
app.register_blueprint(edge_blueprint, url_prefix="/e")

@app.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    return response #protecao contra CORS? desfuncional

def createRandomData():
    from project.models import MapNode, StickerNode, TopicNode, Edge
    from random import randint
    n1 = MapNode("Mapa 1")
    n2 = MapNode("Mapa 2")
    n3 = MapNode("Mapa 3")
    db.session.add_all([n1,n2,n3])
    db.session.commit()

    toAdd = []
    for i in range(3):
        newNode = StickerNode("Sticker " + str(i), "Conteudo nele", parent_id=n1.node_id)
        toAdd.append(newNode)
    
    for i in range(3):
        newNode = TopicNode("Topic " + str(i), "Conteudo do Topico nele", parent_id=n1.node_id)
        toAdd.append(newNode)

    Edge(toAdd[1], toAdd[2])
    Edge(toAdd[1], toAdd[3])
    Edge(toAdd[4], toAdd[5])

    db.session.add_all(toAdd)
    db.session.commit()

# for table in db.metadata.tables.items():
    # print(table)

@app.route('/restart') #Debugging route. Immediately drops all tables and information stored
def dropTables():
    db.session.remove()
    db.drop_all()
    db.create_all()
    createRandomData()
    return "<h1>All data restarted succesfully</h1>"
