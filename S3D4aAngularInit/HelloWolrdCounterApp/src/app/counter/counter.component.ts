import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.css']
})
export class CounterComponent {

  count = 0;

  incrementCount() {
    this.count++;
  }

  decrementCounter(){
    this.count--;
  }
  resetCounter(){
    this.count=0
  }
}
