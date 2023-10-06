import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule,Routes} from '@angular/router';
import { TaskListingComponent } from './task-listing/task-listing.component';
import { ProjectListingComponent } from './project-listing/project-listing.component';

const routes:Routes=[
  {path:'projects',component:ProjectListingComponent},
  {path:'tasks',component:TaskListingComponent},
  {path:'',redirectTo:'/projects',pathMatch:'full'},
]


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports:[RouterModule],
})
export class AppRoutingModule { }
