import { Injectable } from '@angular/core';
import {API_URL} from "./env"
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class NotesApiService {

  constructor(private http:HttpClient) { }

  getNode(id){
    return new Promise((resolve, reject) =>{
      this.http.get(API_URL + "/n/" + id).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  deleteNode(id){
    return new Promise((resolve, reject) =>{
      this.http.delete(API_URL + "/n/" + id).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  getStarterMaps(){
    return new Promise((resolve, reject) =>{
      this.http.get(API_URL + "/m/").toPromise().then(r => {
      // this.http.get(API_URL + "/map").toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  getChildren(mapId){
    return new Promise((resolve, reject) =>{
      this.http.get(API_URL + "/m/" + mapId).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  newMap(map){
    return new Promise((resolve, reject) =>{
      this.http.post(API_URL + "/m/", map).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  updateMap(map){
    return new Promise((resolve, reject) =>{
      this.http.put(API_URL + "/m/" + map.node_id, map).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  newTopic(topic){
    return new Promise((resolve, reject) =>{
      this.http.post(API_URL + "/t/", topic).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  updateTopic(topic){
    return new Promise((resolve, reject) =>{
      this.http.put(API_URL + "/t/" + topic.node_id, topic).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  newSticker(sticker){    
    return new Promise((resolve, reject) =>{
      this.http.post(API_URL + "/s/", sticker).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  updateSticker(sticker){
    return new Promise((resolve, reject) =>{
      this.http.put(API_URL + "/s/" + sticker.node_id, sticker).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  newEdge(n1,n2){
    return new Promise((resolve, reject) =>{        
      this.http.post(API_URL +"/e/",n1,n2).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  updateEdge(n1,n2,n3){
    return new Promise((resolve, reject) =>{        
      this.http.put(API_URL +`/e/${n1}/${n2}`,n1,n3).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  deleteEdge(n1,n2){
    return new Promise((resolve, reject) =>{        
      this.http.delete(API_URL +`/e/${n1}/${n2}`).toPromise().then(r => {
        resolve(r);
      }).catch(e => {
        console.log(e);
        reject(e);
      });
    });
  }

  
}
