import { Injectable } from '@angular/core';
import { Task } from './task.model';

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  private tasks:Task[] = [];

  getTasks(): Task[]{
    return this.tasks
  }

  addTask(task:Task):void {
    task.id = this.tasks.length+1;
    this.tasks.push(task)
  }
  updateTask(task:Task):void{
    const index = this.tasks.findIndex((t)=>t.id==task.id);
    if (index!==-1){
      this.tasks[index]=task;
    }
  }
  deleteTask(itemId:number):void {
    const index = this.tasks.findIndex((i)=>i.id==itemId);
    if (index!==-1){
      this.tasks.splice(index,1);
    }
  }  
  constructor() { }
}
