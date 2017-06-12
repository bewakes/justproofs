import { NgModule } from '@angular/core';
import { AppComponent } from './components/app.component.ts';
import { BrowserModule} from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { HttpModule } from '@angular/http';

// app routes
const appRoutes: Routes = [
  { path: 'crisis-center', component: AppComponent},
  { path: 'hero/:id',      component: AppComponent},
  {
    path: 'heroes',
    component: AppComponent,
    data: { title: 'Heroes List' }
  },
  { path: '',
    redirectTo: '/heroes',
    pathMatch: 'full'
  },
    //{ path: '**', component: PageNotFoundComponent }
];


@NgModule({
  declarations: [
    AppComponent,
    // register it inside the declarations array
  ],
  imports: [
      BrowserModule,
      RouterModule.forRoot(appRoutes),
  ],
  bootstrap: [
      AppComponent
  ]
})
export class AppModule {}
