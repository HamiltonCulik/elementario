from flask import Blueprint,jsonify
from project import db
from project.models import StickerNode, Node
from sys import stderr

sticker_blueprint = Blueprint('sticker',
                              __name__,
                              template_folder='')

@sticker_blueprint.route('/<id>', methods = ["POST, PUT"])
def sticker(id):
    if(request.method == "POST"):
        if(Node.query.get(node_id = id).all()[0]):
            print("Attempted to create a new Sticker with id {} when it already exists".format(id), file=stderr)
        else:
            data = request.form
            newSticker = StickerNode(data.name, data.content, data.x, data.y, data.parent)
            db.session.add_all([newSticker])
            db.commit()
    
    elif(request.method == "PUT"):
        currentSticker = Node.query.get(node_id = id).all()[0]
        if(not currentSticker):
            print("Attempted to update Sticker with id {} when it doesn't exist".format(id), file=stderr)
        else:
            data = request.form
            currentSticker.node_name = data.name
            currentSticker.content = data.content
            currentSticker.node_position_x = data.x
            currentSticker.node_position_y = data.y
            db.commit()