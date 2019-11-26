from project import db
from sqlalchemy.ext.declarative import declared_attr

class Node(db.Model):
    __tablename__ = "node"
    __mapper_args__ = {'polymorphic_on': 'node_type'}
    # __table_args__ = {'extend_existing': True}

    node_id = db.Column(db.Integer, primary_key=True)
    node_name = db.Column(db.Text)
    node_position_x = db.Column(db.Float)
    node_position_y = db.Column(db.Float)
    map_children = db.relationship("Node", backref = db.backref("parent", remote_side=[node_id]))
    parent_id = db.Column(db.Integer, db.ForeignKey("node.node_id"))
    node_type = db.Column(db.Text)


    def __init__(self, name, x = None, y = None, parent_id = None):
        self.parent_id = parent_id
        self.node_name = name
        self.node_position_x = x
        self.node_position_y = y

    def higher_neighbors(self):
        return [x.higher_node for x in self.lower_edges]

    def lower_neighbors(self):
        return [x.lower_node for x in self.higher_edges]


class Edge(db.Model):
    __tablename__ = "edge"
    __table_args__ = {'extend_existing': True}

    lower_id = db.Column(db.Integer, db.ForeignKey("node.node_id"), primary_key=True)

    higher_id = db.Column(db.Integer, db.ForeignKey("node.node_id"), primary_key=True)

    lower_node = db.relationship(
        Node, primaryjoin=lower_id == Node.node_id, backref="lower_edges"
    )

    higher_node = db.relationship(
        Node, primaryjoin=higher_id == Node.node_id, backref="higher_edges"
    )

    def __init__(self, n1, n2):
        self.lower_node = n1
        self.higher_node = n2


class MapNode(Node):
    __mapper_args__ = {'polymorphic_identity': 'map'}

    def children_nodes(self):
        return [x for x in self.map_children]

class TopicNode(Node):
    __mapper_args__ = {'polymorphic_identity': 'topic'}

    @declared_attr
    def content(cls):
        return Node.__table__.c.get('content', db.Column(db.Text))

class StickerNode(Node):
    __mapper_args__ = {'polymorphic_identity': 'sticker'}

    @declared_attr
    def content(cls):
        return Node.__table__.c.get('content', db.Column(db.Text))

    def __init__(self, name, content,  x=None, y=None, parent_id=None):
        self.parent_id = parent_id
        self.node_name = name
        self.node_position_x = x
        self.node_position_y = y
        self.content = content


