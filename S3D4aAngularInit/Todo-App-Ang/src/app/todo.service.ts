import { Injectable } from '@angular/core';
import { Todo } from './todo';
@Injectable({
  providedIn: 'root'
})
export class TodoService {
  private todos:Todo[]=[];
  
  addTodo(todo:string):void{
    this.todos.push({
      content:todo,
      completed:false
    });
  }
  deleteTodo(id:number){
    // this.todos=this.todos.filter((v,i)=>i!=id);
    this.todos.splice(id,1);
  }
  constructor() { }
  getTodo():Todo[] {
    return this.todos;
  }
}
