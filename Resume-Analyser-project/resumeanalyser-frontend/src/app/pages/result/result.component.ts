import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AnalyzerService } from '../../services/analyzer.service';

@Component({
  selector: 'app-result',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './result.component.html',
  styleUrl: './result.component.css'
  
})
export class ResultComponent implements OnInit {
  analysis: any;
  

  constructor(private analyzer: AnalyzerService) {}

  ngOnInit(): void {
    this.analyzer.currentResult.subscribe(result => {
      console.log('Fetched from service:', result);
      this.analysis = result;
      if (!result) {
        console.warn('No result found — did you navigate here directly?');
      }
    });
  }
}
