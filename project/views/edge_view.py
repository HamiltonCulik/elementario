from flask import Blueprint,jsonify,request
from flask_cors import cross_origin
from project import db
from project.models import Edge, Node
from sys import stderr

edge_blueprint = Blueprint('edge',
                              __name__,
                              template_folder='')


@edge_blueprint.route("/", methods = ["POST"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def addEdge():
    data = request.get_json()
    n1 = Node.query.get(data["n1"])
    n2 = Node.query.get(data["n2"])
    newEdge = Edge(n1, n2)
    db.session.add_all([newEdge])
    db.session.commit()
    return "200"
    
@edge_blueprint.route('/<id1>/<id2>', methods = ["PUT"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def updateEdge(id1,id2):
    currentEdge = Edge.query.filter(lower_id = id1, higher_id = id2).all()[0]
    if(not currentEdge):
        print("Attempted to update Edge that doesn't exit {}-{}".format(id1,id2), file=stderr)
    else:
        data = request.get_json()
        n1 = Node.query.get(data["n1"])
        n2 = Node.query.get(data["n2"])
        db.session.delete(currentEdge) #delete the previous edge, correctly removing previous foreignkeys
        newEdge = Edge(n1,n2) #easier than manipulating inner foreign keys of every node
        db.session.add_all([newEdge])
        db.session.commit()
        return "200"

@edge_blueprint.route('/<id1>/<id2>', methods = ["DELETE"])
def deleteEdge(id1,id2):
    currentEdge = Edge.query.filter(lower_id = id1, higher_id = id2).all()[0]
    db.session.delete(currentEdge)
    db.session.commit()
    return "200"
