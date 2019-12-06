from flask import Blueprint,jsonify,request
from flask_cors import cross_origin
from project import db
from project.models import TopicNode, Node, Edge
from sys import stderr


topic_blueprint = Blueprint('topic',
                              __name__,
                              template_folder='')

@topic_blueprint.route("/", methods = ["POST"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def addTopic():
    data = request.get_json()
    newTopic = TopicNode(data["node_name"], data["content"], data["node_position_x"], data["node_position_y"], data["parent_id"])
    db.session.add_all([newTopic])
    db.session.commit()
    return "200"

@topic_blueprint.route('/<id>', methods = ["PUT"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def updateTopic(id):
    currentTopic = Node.query.get(id)
    if(not currentTopic):
        print("Attempted to update Topic with id {} when it doesn't exist".format(id), file=stderr)
        return "404"
    else:
        data = request.get_json()
        currentTopic.node_name = data["node_name"]
        currentTopic.content = data["content"]
        currentTopic.node_position_x = data["node_position_x"]
        currentTopic.node_position_y = data["node_position_y"]

        oldLinks = [x.node_id for x in currentTopic.higher_neighbors()]
        newLinks = data["node_links"]
        for node_id in oldLinks:
            if(node_id not in newLinks): #delete all edges not found in new list
                toDelete = Edge.query.filter_by(lower_id= currentTopic.node_id,higher_id=node_id).all()[0]
                db.session.delete(toDelete)

        for node_id in newLinks: #add all new edges
            if(node_id not in oldLinks and node_id != currentTopic.node_id):
                nextNode = Node.query.get(node_id)
                Edge(currentTopic, nextNode)

        db.session.commit()
        return "200"
