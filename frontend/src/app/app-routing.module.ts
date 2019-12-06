import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ShowMapsComponent } from './show-maps/show-maps.component';
import { ViewMapComponent } from './view-map/view-map.component';

const routes: Routes = [
  {path: "",  redirectTo: '/listMaps', pathMatch: 'full' },
  {path: "listMaps", component: ShowMapsComponent},
  {path: "map/:id", component: ViewMapComponent},
]


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
