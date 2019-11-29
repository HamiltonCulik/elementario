from flask import Blueprint,jsonify
from project import db
from project.models import MapNode, Node
from sys import stderr


map_blueprint = Blueprint('map',
                              __name__,
                              template_folder='')

@map_blueprint.route("/", methods = ["GET"])
def starterMaps():
    parentlessMaps = Node.query.filter_by(node_parent = None).all()

    result = [x.as_dict for x in parentlessMaps]

    return jsonify(result)

@map_blueprint.route('/<id>', methods = ["GET", "POST", "PUT"])
def Map(id):
    if(request.method == "GET"):#Gets an entire map as its view, that is, all its children and their connections
        mapResult = Node.query.filter_by(node_id = id).all()[0]
        children = [x.as_dict for x in mapResult.children_nodes()]
        return jsonify(children)
    
    elif(request.method == "POST"):
        if(Node.query.get(node_id = id).all()[0]):
            print("Attempted to create a new Map with id {} when it already exists".format(id), file=stderr)
        else:
            data = request.form
            newMap = MapNode(data.name, data.x, data.y, data.parent)
            db.session.add_all([newMap])
            db.commit()
    
    elif(request.method == "PUT"):
        currentMap = Node.query.get(node_id = id).all()[0]
        if(not currentMap):
            print("Attempted to update Map with id {} when it doesn't exist".format(id), file=stderr)
        else:
            data = request.form
            currentMap.node_name = data.name
            currentMap.node_position_x = data.x
            currentMap.node_position_y = data.y
            db.commit()