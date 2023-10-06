import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  taskList:any[]=[
    {
      id:1,
      name:'Task-1',
      description:'Description For Task-1'
    },
    {
      id:2,
      name:'Task-2',
      description:'Description For Task-2'
    },
    {
      id:3,
      name:'Task-3',
      description:'Description For Task-3'
    },
    {
      id:4,
      name:'Task-4',
      description:'Description For Task-4'
    },
    {
      id:5,
      name:'Task-5',
      description:'Description For Task-5'
    },
    ];

    getTask():any[]{
      return this.taskList;
    }

    deleteTask(id:number):void{
      this.taskList=this.taskList.filter((task)=>task.id!=id);
      console.log(id);
    }


  constructor() { }
}
