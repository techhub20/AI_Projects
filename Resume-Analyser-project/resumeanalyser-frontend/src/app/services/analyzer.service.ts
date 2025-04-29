import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AnalyzerService {
  private analysisResult: any;
  private apiUrl = environment.apiUrl + '/upload'; // Use the environment variable for the API URL
  //'http://localhost:8080/api/upload';
  private resultSource = new BehaviorSubject<any>(null);
  currentResult = this.resultSource.asObservable();

  constructor(private http: HttpClient) { }

  uploadResume(file: File, jobDescription: string): Observable<any> {
    const formData = new FormData();
    formData.append('resume', file);
    formData.append('jobDescription', jobDescription);

    return this.http.post<any>(this.apiUrl, formData);
  }

  setResult(result: any) {
    this.analysisResult = result;
    this.resultSource.next(result);
  }

  getResult() {
    return this.analysisResult;
  }
}
