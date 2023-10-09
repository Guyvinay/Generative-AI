// task-list.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent {
  tasks: any[] = [
    { name: 'Task 1', completed: false, dueDate: new Date() },
    { name: 'Task 2', completed: true, dueDate: new Date() },
    // Add more sample tasks here
  ];
}
