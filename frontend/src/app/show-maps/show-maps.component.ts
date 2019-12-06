import { Component, OnInit } from '@angular/core';
import { NotesApiService } from '../notes-api.service';
import { Node } from '../node';

@Component({
  selector: 'app-show-maps',
  templateUrl: './show-maps.component.html',
  styleUrls: ['./show-maps.component.css']
})
export class ShowMapsComponent implements OnInit {

  mapList: Node[];
  map_to_add : Node;

  constructor(public api: NotesApiService) { }

  ngOnInit() {
    this.getMapList();
  }

  private getMapList(){
    this.api.getStarterMaps().then((r:any) =>{ 
      this.mapList = r;
    });
  }
  addMap(name){
    const dummyNode = {node_id: null,
      node_type: "map",
      node_name:name, 
      content: "",
      node_position_x: null,
      node_position_y: null,
      parent_id:null,
      node_links: []};

    this.api.newMap(dummyNode).then((r:any) => {
      this.getMapList();
    });
  }

}
