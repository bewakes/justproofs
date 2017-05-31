import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class="app">
      {{ message }}
    </div>
    <span>Counts: {{count}}</span>
    <button (click)="increaseCounter()">Increase</button>
    <a routerLink="/crisis-center" routerLinkActive="active">Crisis Center</a>
    <a routerLink="/heroes" routerLinkActive="active">Heroes</a>
  `
})
export class AppComponent {
    message: string;// = 'Hello world!';
    count: number;
    constructor() {
        this.message = "Hola World!!";
        this.count = 0;
    }
    increaseCounter() {
        this.count++;
    }
}
