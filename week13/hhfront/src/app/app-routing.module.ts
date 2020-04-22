import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {CompaniesListComponent} from './components/companies-list/companies-list.component';
import {CompanyDetailComponent} from './components/company-detail/company-detail.component';



const routes: Routes = [
  {path: '', component: CompaniesListComponent},
  {path: 'companies/:companyId/vacancies', component: CompanyDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
