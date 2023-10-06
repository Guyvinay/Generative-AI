import { Injectable, OnInit } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProjectService implements OnInit{

  projectList:any[]=[
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
    ];;

  constructor() { }
  
  ngOnInit(): void {
   
  }

    getProjects():any[]{
      return this.projectList;
    }

    deleteProject(id:number):void{
      this.projectList=this.projectList.filter((project)=>project.id!=id);
      // this.projectList = [...this.projectList,this.projectList.find((project)=>project.id==id)]
    }

}
