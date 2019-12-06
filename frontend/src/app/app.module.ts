import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from "@angular/forms";


import { AppComponent } from './app.component';
import { ShowMapsComponent } from './show-maps/show-maps.component';
import { AppRoutingModule } from './app-routing.module';
import { ViewMapComponent } from './view-map/view-map.component';
import { NotesApiService } from './notes-api.service';
import { EditMapComponent } from './edit-map/edit-map.component';
import { EditTopicComponent } from './edit-topic/edit-topic.component';
import { EditStickerComponent } from './edit-sticker/edit-sticker.component';
import { SidebarComponent } from './sidebar/sidebar.component';

@NgModule({
  declarations: [
    AppComponent,
    ShowMapsComponent,
    ViewMapComponent,
    EditMapComponent,
    EditTopicComponent,
    EditStickerComponent,
    SidebarComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [NotesApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
