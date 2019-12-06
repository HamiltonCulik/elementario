import { Component, OnInit, ViewChild } from '@angular/core';
import { Node } from '../node';
import { NotesApiService } from '../notes-api.service';
import { ActivatedRoute} from '@angular/router';
import { SidebarComponent } from '../sidebar/sidebar.component';


@Component({
  selector: 'app-view-map',
  templateUrl: './view-map.component.html',
  styleUrls: ['./view-map.component.css']
})
export class ViewMapComponent implements OnInit {
  public currentMap : Node;
  public parentMap : Node;
  public selectedNode : Node;
  public loadedMap : Node[];
  @ViewChild(SidebarComponent, {static: false})

  private sidebarComponent: SidebarComponent;

  constructor(
    public api: NotesApiService, 
    private actRoute: ActivatedRoute) { }

  ngOnInit() {
    this.getInfo()
  }

  private getInfo(){
    const id = +this.actRoute.snapshot.paramMap.get('id');
    this.api.getNode(id).then((r:any) =>{
      this.currentMap = r;
      if(this.currentMap.parent_id){        
        this.api.getNode(this.currentMap.parent_id).then((r:any)=>{
          this.parentMap = r;
        });
      }
      this.updateChildren();
    });

  }

  public updateChildren(){
    this.api.getChildren(this.currentMap.node_id).then((r:any) =>{ 
      this.loadedMap = r;
    });
  }

  private changeMapTo(map){
    this.api.getNode(map.node_id).then((r:any) =>{
      this.currentMap = r;
      if(this.currentMap.parent_id){        
        this.api.getNode(this.currentMap.parent_id).then((r:any)=>{
          this.parentMap = r;
        });
      }
      this.updateChildren();
    });
  }
  public selectNode(node){
    if(node.node_type == "map"){
      const decision = confirm("Você gostaria de entrar nesse mapa?")
      if(decision){
        this.changeMapTo(node);

      } else {
        this.sidebarComponent.openSidebar(node);
      }
    } else {
      this.sidebarComponent.openSidebar(node);
    }
  }

  public newSticker(){
    const dummyNode = {node_id: null,
      node_type: "sticker",
      node_name:"", 
      content: "",
      node_position_x: null,
      node_position_y: null,
      parent_id:this.currentMap.node_id,
      node_links: []};
    
    this.sidebarComponent.openSidebar(dummyNode);
  }
  
  public newTopic(){
    const dummyNode = {node_id: null,
      node_type: "topic",
      node_name:"", 
      content: "",
      node_position_x: null,
      node_position_y: null,
      parent_id:this.currentMap.node_id,
      node_links: []};
    
    this.sidebarComponent.openSidebar(dummyNode);
  }

  public newMap(){
    const dummyNode = {node_id: null,
      node_type: "map",
      node_name:"", 
      content: "",
      node_position_x: null,
      node_position_y: null,
      parent_id:this.currentMap.node_id,
      node_links: []};
    
    this.sidebarComponent.openSidebar(dummyNode);
  }

  public delete(node){
    this.api.deleteNode(node.node_id).then((r:any) =>{
      this.updateChildren();
    });
  }

  public onClose(a){
    this.updateChildren();
  }
}
