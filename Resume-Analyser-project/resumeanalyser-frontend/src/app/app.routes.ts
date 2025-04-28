import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';    
import { UploadComponent } from './pages/upload/upload.component';
import { ResultComponent } from './pages/result/result.component';


export const routes: Routes = [
  //  { path: '', component: HomeComponent },
  { path: 'upload', component: UploadComponent },
  { path: 'result', component: ResultComponent },
  { path: '**', redirectTo: '' },
];
@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
  })
  export class AppRoutingModule { }