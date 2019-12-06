from flask import Blueprint,jsonify,request
from flask_cors import cross_origin
from project import db
from project.models import Node
from sys import stderr 


node_blueprint = Blueprint('node',
                              __name__,
                              template_folder='')

@node_blueprint.route('/<id>', methods = ["GET", "DELETE"], strict_slashes = False)
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def node(id): #creates or deletes any single node, that is, a single map, sticker or topic
    if(request.method == "GET"):
        resultingNode = Node.query.get(id)
        if(not resultingNode):
            print("Error, attempted to get node with id {} when it doesn't exist".format(id), stderr)
            return "404"
        return jsonify(resultingNode.as_dict())
    
    if(request.method == "DELETE"):
        toDelete = Node.query.get(id)
        if(not toDelete):
             print("Error, attempted to delete node with id {} when it doesn't exist".format(id), stderr)
             return "404"

        if(toDelete.node_type == "map"): #if it's a map, we need to delete all children nodes
            for x in toDelete.children_nodes():
                db.session.delete(x)

        for edge in toDelete.lower_edges:
            db.session.delete(edge)

        for edge in toDelete.higher_edges:
            db.session.delete(edge)
       
        db.session.delete(toDelete)
        db.session.commit()
        return "200"