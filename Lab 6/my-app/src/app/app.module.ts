import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  imports: [BrowserModule],
  declarations: [], // Ваши компоненты
  bootstrap: [AppComponent] // Компонент, который будет использоваться в качестве корневого
})
export class AppModule { }
