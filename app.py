# from project import app,db
# from flask import jsonify
# import sys

# from project.models import MapNode, TopicNode, StickerNode, Edge, Node
from project import app

@app.route('/')
def index():
    db.create_all()
    # n1 = MapNode("Mapa 1")
    # db.session.add_all([n1])
    # db.session.commit()


    # n2 = TopicNode("Topic 1", x = 30, y = 30, parent_id = n1.node_id)
    # n3 = TopicNode("Topic 2", x = 60, y = 60, parent_id = n1.node_id)
    # n4 = StickerNode("Sticker 1", "Conteudo dentro dele", x = 90, y = 90, parent_id = n1.node_id)
    # n5 = TopicNode("Topic 3", x = 120, y = 120, parent_id = n1.node_id)

    # Edge(n2,n3)
    # Edge(n2,n4)
    # Edge(n3,n5)

    # db.session.add_all([n1,n2,n3,n4,n5])
    # db.session.commit()

    # primeiroMapa = Node.query.filter_by(node_id = n1.node_id).all()[0]
    # # primeiroMapa = Node.query.all()
    
    # a = [(x,x.lower_neighbors()) for x in primeiroMapa.children_nodes()]
    # b = primeiroMapa.children_nodes()

    # db.session.remove()
    # db.drop_all()
    # return render_template("index.html", mainMap = primeiroMapa, nodeLinks = a, innerNodes = b)
    return

app.run(debug = True)

# TODO 
#   Create Post and Put for Sticker and Map.
#   Create Post and Put for Edges
#   Think angular structure better
#
#
#