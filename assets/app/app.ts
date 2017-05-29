import { NgModule } from '@angular/core';
import { BrowserModule} from '@angular/platform-browser';

platformBrowserDynamic().bootstrapModule(AppModule);

import { AppComponent } from './components/test.component.ts';

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
