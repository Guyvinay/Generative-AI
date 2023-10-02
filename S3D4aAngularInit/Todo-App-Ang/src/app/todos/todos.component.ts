import { Component, OnInit } from '@angular/core';
import { Todo } from '../todo';
@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css']
})
export class TodosComponent implements OnInit {
  todos: Todo[] = [];
  inputTodo:string="";

  ngOnInit(): void {
  }
  addToDo():void{
    this.todos.push({
      content:this.inputTodo,
      completed:false
    });
    this.inputTodo="";
    console.log(this.todos);
  }
  deleteTodo(id:number){
    this.todos=this.todos.filter((v,i)=>i!=id);
  }
  toggleDone(id:number){
    this.todos.map((ele,ind)=>{
      if(id==ind){
        ele.completed=!ele.completed;
      }
      // return ele;
        console.log(ele);
    })
  }
}
