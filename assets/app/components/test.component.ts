import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class="app">
    bibek
      {{ message }}
    </div>
  `
})
export class AppComponent {
  message: string = 'Hello world!';
}
