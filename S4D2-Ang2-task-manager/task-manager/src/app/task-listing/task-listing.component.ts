import { Component } from '@angular/core';

@Component({
  selector: 'app-task-listing',
  templateUrl: './task-listing.component.html',
  styleUrls: ['./task-listing.component.css']
})
export class TaskListingComponent {

  tasks = [
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
    ]

    deleteTask(id:number):void {
      // console.log(this.tasks.length)
      this.tasks=this.tasks.filter((task)=>task.id!=id);
      // console.log(this.tasks.length)
    }

}
