import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Node } from '../node';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {

  @Input() selectedNode : Node;
  @Input() nodeList: Node[];
  @Output() closed = new EventEmitter<boolean>();

  operation: any;
  selectedMap = false;
  selectedTopic = false;
  selectedSticker = false;


  constructor() { }

  ngOnInit() {
  }

  public openSidebar(node){
    this.selectedNode = node;
    document.getElementById("sidebar").style.width = "50%";
    this.selectedMap = false;
    this.selectedTopic = false;
    this.selectedSticker = false;

    if(this.selectedNode.node_type == "map"){
      this.selectedMap = true;
      
    } else if(this.selectedNode.node_type == "topic"){
      this.selectedTopic = true;
      
    } else if(this.selectedNode.node_type == "sticker"){
      this.selectedSticker = true;
    }

  }
  

  public closeSidebar(){
    document.getElementById("sidebar").style.width = "0";
    this.closed.emit(true);
  }

  public onPost(a){    
    this.closeSidebar()
  }
}
