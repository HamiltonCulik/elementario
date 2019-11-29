from flask import Blueprint,jsonify
from project import db
from project.models import Node
from sys import stderr  #TODO write error protection and log debugging


node_blueprint = Blueprint('node',
                              __name__,
                              template_folder='')

@node_blueprint.route('/<id>', methods = ["GET", "DELETE"])
def node(id): #creates or deletes any single node, that is, a single map, sticker or topic
    if(request.method == "GET"):
        resultingNode = Node.query.get(node_id = id).all()[0]
        return jsonify(resultingNode.as_dict())
    
    if(request.method == "DELETE"):
        toDelete = Node.query.get(node_id = id).all()[0]
        if(toDelete.node_type == "map"): #if it's a map, we need to delete all children nodes
            for x in toDelete.children_nodes():
                x.delete()

        toDelete.delete()
        db.session.commit()