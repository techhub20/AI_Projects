import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UploadComponent } from "./pages/upload/upload.component";
import { HttpClientModule } from '@angular/common/http';
import { ResultComponent } from "./pages/result/result.component";
import { HomeComponent } from "./pages/home/home.component";
import { ThemeService } from './services/theme.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, UploadComponent, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  isDarkMode = true;
  constructor() {
    const savedTheme = localStorage.getItem('theme') || 'dark-theme';
    this.isDarkMode = savedTheme === 'dark-theme';
  
    // Apply dark theme on initial load
    document.body.classList.add('dark-theme');
  }
  ngOnInit() {
    const savedTheme = localStorage.getItem('theme') || 'dark-theme';
    this.isDarkMode = savedTheme === 'dark-theme';
  
    document.body.classList.add(savedTheme);
  }
  
  // toggleTheme() {
  //   this.isDarkMode = !this.isDarkMode;
  //   if (this.isDarkMode) {
  //     document.body.classList.add('dark-theme');
  //     localStorage.setItem('theme', 'dark');
  //   } else {
  //     document.body.classList.remove('dark-theme');
  //     localStorage.setItem('theme', 'light');
  //   }
  // }
  toggleTheme() {
    this.isDarkMode = !this.isDarkMode;
    const classToAdd = this.isDarkMode ? 'dark-theme' : 'light-theme';
    const classToRemove = this.isDarkMode ? 'light-theme' : 'dark-theme';
  
    document.body.classList.remove(classToRemove);
    document.body.classList.add(classToAdd);
  
    localStorage.setItem('theme', classToAdd);
  }
  
  
}
