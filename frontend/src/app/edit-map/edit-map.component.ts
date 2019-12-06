import { Component, OnInit, Input, EventEmitter, Output } from '@angular/core';
import { NotesApiService } from '../notes-api.service';
import { Node } from "../node";
import { SidebarComponent } from '../sidebar/sidebar.component';

@Component({
  selector: 'app-edit-map',
  templateUrl: './edit-map.component.html',
  styleUrls: ['./edit-map.component.css']
})
export class EditMapComponent implements OnInit {
  @Input() node: any;
  @Input() nodeList: Node[];
  @Output() posted = new EventEmitter<boolean>();

  constructor(
    public api:NotesApiService,
    public sidebar: SidebarComponent) { }

  ngOnInit() {
    this.node = this.sidebar.selectedNode;
  }

  public new_map : Node;
  onSubmit(){
    this.new_map =  {node_id: this.node.node_id,
      node_type: this.node.node_type,
      node_name:this.node.node_name, 
      content: this.node.content,
      node_position_x: this.node.node_position_x,
      node_position_y: this.node.node_position_y,
      parent_id:this.node.parent_id,
      node_links: this.node.node_links};
          
    if(this.node.node_id != null){
      this.api.updateMap(this.new_map).then((r:any)=>{
        this.posted.emit(true)
      });
    }else {
      this.api.newMap(this.new_map).then((r:any)=>{
        this.posted.emit(true)
      });
    }
  }

  private newEdge(){
    this.node.node_links.push(0);
  }

  private removeEdge(index){
    this.node.node_links.splice(index, 1);
  }

}
