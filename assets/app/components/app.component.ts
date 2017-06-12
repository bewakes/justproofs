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
    <ul>
        <li *ngFor="let x of data">{{x}}</li>
    </ul>
  `
})
export class AppComponent {
    message: string;// = 'Hello world!';
    count: number;
    data: [int];
    constructor() {
        this.message = "Hola World!!";
        this.count = 0;
        this.data = [1,2,3,4,5];
    }
    increaseCounter() {
        this.count++;
    }
}
