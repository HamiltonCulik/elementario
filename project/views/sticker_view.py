from flask import Blueprint,jsonify,request
from flask_cors import cross_origin
from project import db
from project.models import StickerNode, Node, Edge
from sys import stderr

sticker_blueprint = Blueprint('sticker',
                              __name__,
                              template_folder='')


@sticker_blueprint.route("/", methods = ["POST","OPTIONS"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def addSticker():
    data = request.get_json()
    newSticker = StickerNode(data["node_name"], data["content"], data["node_position_x"], data["node_position_y"], data["parent_id"])
    db.session.add_all([newSticker])
    db.session.commit()
    return "200"

@sticker_blueprint.route('/<id>', methods = ["PUT"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def updateSticker(id):
    currentSticker = Node.query.get(id)
    if(not currentSticker):
        print("Attempted to update Sticker with id {} when it doesn't exist".format(id), file=stderr)
        return "404"
    else:
        data = request.get_json()
        currentSticker.node_name = data["node_name"]
        currentSticker.content = data["content"]
        currentSticker.node_position_x = data["node_position_x"]
        currentSticker.node_position_y = data["node_position_y"]

        oldLinks = [x.node_id for x in currentSticker.higher_neighbors()]
        newLinks = data["node_links"]
        for node_id in oldLinks:
            if(node_id not in newLinks): #delete all edges not found in new list
                toDelete = Edge.query.filter_by(lower_id= currentSticker.node_id,higher_id=node_id).all()[0]
                db.session.delete(toDelete)

        for node_id in newLinks: #add all new edges
            if(node_id not in oldLinks and node_id != currentSticker.node_id):
                nextNode = Node.query.get(node_id)
                Edge(currentSticker, nextNode)

        db.session.commit()
        return "200"