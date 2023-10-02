import { Component, OnInit } from '@angular/core';
import { Todo } from '../todo';
import { TodoService } from '../todo.service';
@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css']
})
export class TodosComponent implements OnInit {
  todos: Todo[] = [];
  inputTodo:string='';

  constructor(private todoService: TodoService){}

  ngOnInit(): void {
    this.todos=this.todoService.getTodo();
  }
  addToDo():void{
    if(this.inputTodo.trim()!=''){
    // this.todos.push({
    //   content:this.inputTodo,
    //   completed:false
    // });
    this.todoService.addTodo(this.inputTodo)
    this.inputTodo='';
    // console.log(this.todos);
    }
  }
  deleteTodo(id:number){
    this.todoService.deleteTodo(id);
    // this.todos=this.todos.filter((v,i)=>i!=id);
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
