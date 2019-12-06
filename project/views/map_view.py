from flask import Blueprint,jsonify,request
from flask_cors import cross_origin
from project import db
from project.models import MapNode, Node, Edge
from sys import stderr


map_blueprint = Blueprint('map',
                              __name__,
                              template_folder='')

@map_blueprint.route("/", methods = ["GET", "POST"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def starterMaps():
    if(request.method == "GET"):
        parentlessMaps = Node.query.filter_by(parent_id = None).all()
        result = [x.as_dict() for x in parentlessMaps]
        return jsonify(result)

    elif(request.method == "POST"):
        data = request.get_json()
        newMap = MapNode(data["node_name"], data["node_position_x"], data["node_position_y"], data["parent_id"])
        db.session.add_all([newMap])
        db.session.commit()
        return "200"



@map_blueprint.route('/<id>', methods = ["GET", "PUT"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def Map(id):
    if(request.method == "GET"):#Gets an entire map as its view, that is, all its children and their connections
        mapResult = Node.query.get(id)
        children = [x.as_dict() for x in mapResult.children_nodes()]
        return jsonify(children)

    elif(request.method == "PUT"):
        currentMap = Node.query.get(id)
        if(not currentMap):
            print("Error, attempted to update map with id {} when it doesn't exist yet".format(id), stderr)
            return "404"
        data = request.get_json()
        currentMap.node_name = data["node_name"]
        currentMap.node_position_x = data["node_position_x"]
        currentMap.node_position_y = data["node_position_y"]

        oldLinks = [x.node_id for x in currentMap.higher_neighbors()]
        newLinks = data["node_links"]
        for node_id in oldLinks:
            if(node_id not in newLinks): #delete all edges not found in new list
                toDelete = Edge.query.filter_by(lower_id= currentMap.node_id,higher_id=node_id).all()[0]
                db.session.delete(toDelete)

        for node_id in newLinks: #add all new edges
            if(node_id not in oldLinks and node_id != currentMap.node_id):
                nextNode = Node.query.get(node_id)
                Edge(currentMap, nextNode)
    
        db.session.commit()
        return "200"