import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ThemeService {
  private darkModeSubject = new BehaviorSubject<boolean>(false);
  isDarkMode$ = this.darkModeSubject.asObservable();

  constructor() {
    const savedTheme = localStorage.getItem('theme');
    this.darkModeSubject.next(savedTheme === 'dark');
  }

  toggleTheme() {
    const isDark = !this.darkModeSubject.value;
    this.darkModeSubject.next(isDark);
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    this.updateBodyClass(isDark);
  }

  updateBodyClass(isDark: boolean) {
    document.body.classList.remove('dark-theme', 'light-theme');
    document.body.classList.add(isDark ? 'dark-theme' : 'light-theme');
  }
}
