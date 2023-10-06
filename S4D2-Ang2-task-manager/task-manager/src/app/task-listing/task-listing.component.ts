import { Component, OnInit } from '@angular/core';
import { TaskService } from '../task.service';

@Component({
  selector: 'app-task-listing',
  templateUrl: './task-listing.component.html',
  styleUrls: ['./task-listing.component.css']
})
export class TaskListingComponent implements OnInit {

  taskName:string='';
  taskDescription:string='';



  ngOnInit(): void {
   this.tasks=this.taskService.getTask();
  }

  tasks:any[]=[];

  // tasks = [
  //   {
  //     id:1,
  //     name:'Task-1',
  //     description:'Description For Task-1'
  //   },
  //   {
  //     id:2,
  //     name:'Task-2',
  //     description:'Description For Task-2'
  //   },
  //   {
  //     id:3,
  //     name:'Task-3',
  //     description:'Description For Task-3'
  //   },
  //   {
  //     id:4,
  //     name:'Task-4',
  //     description:'Description For Task-4'
  //   },
  //   {
  //     id:5,
  //     name:'Task-5',
  //     description:'Description For Task-5'
  //   },
  //   ]

    constructor(private taskService:TaskService){}

    deleteTask(id:number):void {
      // console.log(this.tasks.length)
      // this.tasks=this.tasks.filter((task)=>task.id!=id);
     this.taskService.deleteTask(id);
     this.tasks=this.taskService.getTask();
     console.log(this.tasks);
      // console.log(this.tasks.length)
    }

    addTask(){
      let task:any={
        id:6,
        name:this.taskName,
        description:this.taskDescription
      };
      this.tasks.push(task);
      this.taskName='';
      this.taskDescription='';
    }




}
