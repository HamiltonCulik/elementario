from flask import Blueprint,jsonify
from project import db
from project.models import TopicNode, Node
from sys import stderr


topic_blueprint = Blueprint('topic',
                              __name__,
                              template_folder='')

@topic_blueprint.route('/<id>', methods = ["POST, PUT"])
def topic(id):
    if(request.method == "POST"):
        if(Node.query.get(node_id = id).all()[0]):
            print("Attempted to create a new Topic with id {} when it already exists".format(id), file=stderr)
        else:
            data = request.form
            newTopic = TopicNode(data.name, data.content, data.x, data.y, data.parent)
            db.session.add_all([newTopic])
            db.commit()
    
    elif(request.method == "PUT"):
        currentTopic = Node.query.get(node_id = id).all()[0]
        if(not currentTopic):
            print("Attempted to update Topic with id {} when it doesn't exist".format(id), file=stderr)
        else:
            data = request.form
            currentTopic.node_name = data.name
            currentTopic.content = data.content
            currentTopic.node_position_x = data.x
            currentTopic.node_position_y = data.y
            db.commit()
