import { Component } from '@angular/core';

@Component({
  selector: 'app-project-listing',
  templateUrl: './project-listing.component.html',
  styleUrls: ['./project-listing.component.css']
})
export class ProjectListingComponent {

  projects = [
  {
    id:1,
    name:'Project-1',
    description:'Description For Project-1'
  },
  {
    id:2,
    name:'Project-2',
    description:'Description For Project-2'
  },
  {
    id:3,
    name:'Project-3',
    description:'Description For Project-3'
  },
  {
    id:4,
    name:'Project-4',
    description:'Description For Project-4'
  },
  {
    id:5,
    name:'Project-5',
    description:'Description For Project-5'
  },
  ]


  deleteTask(id:number):void{
    this.projects=this.projects.filter((project)=>project.id!=id);
  }

}
