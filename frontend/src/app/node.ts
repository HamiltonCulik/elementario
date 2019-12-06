export class Node {
    node_id: number;
    node_name: string;
    parent_id: number;
    node_type: string;
    node_position_x: number;
    node_position_y: number;
    content: string;
    node_links: number[];

    constructor(node_name: string,
      parent_id: number,
      node_type: string,
      node_position_x: number,
      node_position_y: number,
      content: string
      ){
        this.node_id = null;
        this.node_name = node_name;
        this.node_type = node_type;
        this.node_position_x = node_position_x;
        this.node_position_y = node_position_y;
        this.content = content;
      }
  }