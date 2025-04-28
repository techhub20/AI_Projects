import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AnalyzerService } from '../../services/analyzer.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [ CommonModule,FormsModule],
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css'],
 // providers: [AnalyzerService]
})
export class UploadComponent {
  isDarkMode = true;
  selectedFileName = '';
  jobDescription: string = '';
  selectedFile: File | null = null;

  constructor(private analyzer: AnalyzerService, private router: Router) {}

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.selectedFileName = file.name;
      this.selectedFile = file;
    }
  }

  toggleDarkMode() {
    this.isDarkMode = !this.isDarkMode;
  }

  analyzeResume() {
    // 1. Validate Inputs
    if (!this.selectedFile) {
      alert('Please select a resume file.');
      return;
    }

    if (!this.jobDescription) {
      alert('Please fill in the job description.');
      return;
    }

    // 2. Send Data to Backend
    console.log('Sending data to backend...', this.selectedFile, this.jobDescription);
    this.analyzer.uploadResume(this.selectedFile, this.jobDescription)
      .subscribe({
        next: (res) => {
          console.log('Success:', res);
          this.analyzer.setResult(res);     // Store result temporarily
          console.log('Result set in AnalyzerService:', this.analyzer.getResult());  
          this.router.navigate(['/result']); // Navigate to result page
        },
        error: (error) => {
          console.error('Error:', error);
          alert('An error occurred while uploading the resume.');
        }
      });
  }
}
