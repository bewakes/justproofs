import { NgModule } from '@angular/core';
import { AppComponent } from './components/test.component.ts';
import { BrowserModule} from '@angular/platform-browser';

@NgModule({
  declarations: [
    AppComponent,
    // register it inside the declarations array
  ],
  imports: [
    BrowserModule
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule {}
