import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../project.service';


@Component({
  selector: 'app-project-listing',
  templateUrl: './project-listing.component.html',
  styleUrls: ['./project-listing.component.css']
})
export class ProjectListingComponent implements OnInit {

  projects:any[]=[];
  projectName:string='';
  projectDescription:string='';


  constructor(private projectService:ProjectService){

  }
  ngOnInit(): void {
    this.projects=this.projectService.getProjects();
  }

  deleteProject(id:number):void{
    // this.projects=this.projects.filter((project)=>project.id!=id);
    this.projectService.deleteProject(id);
    this.projects=this.projectService.getProjects();
    console.log(id);
  }
  addProject():void{
   let project:any={
      id:12,
      name:this.projectName,
      description:this.projectDescription,
    }
    this.projects.push(project)
    console.log(project)
    this.projectName='';
    this.projectDescription='';
  }


}
