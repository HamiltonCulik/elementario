import { Injectable } from '@angular/core';
import {API_URL} from "/home/hamilton/Documents/Faculdade n stuff/2019-2/Topicos em Programacao/Elementario/frontend/src/app/env"
import { HttpClient } from '@angular/common/http';


//TODO Write all relevant requests


@Injectable({
  providedIn: 'root'
})
export class NotesApiService {

  constructor(private http:HttpClient) { }

  getNode(id){
    return new Promise((resolve, reject) =>{
      this.http.get(API_URL + "/" + id).toPromise().then(r => {
        // this.usuarios = r;
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  postNode(node){
    return new Promise((resolve, reject) =>{
      this.http.post(API_URL + "/" + node.id, node).toPromise().then(r => {
        // this.usuarios = r;
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  getChildren(mapId){
    return new Promise((resolve, reject) =>{
      this.http.get(API_URL + "/map/" + mapId).toPromise().then(r => {
        // this.usuarios = r;
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }
}
