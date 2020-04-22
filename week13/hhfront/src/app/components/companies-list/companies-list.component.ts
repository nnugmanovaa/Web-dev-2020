import { Component, OnInit } from '@angular/core';
import {Company} from '../../models/entities/company';
import {CompanyService} from '../../services/company.service';

@Component({
  selector: 'app-companies-list',
  templateUrl: './companies-list.component.html',
  styleUrls: ['./companies-list.component.css']
})
export class CompaniesListComponent implements OnInit {
  companies: Company[];
  constructor(public companyService: CompanyService) { }

  ngOnInit(): void {
    this.getCompaniesList();
  }

  getCompaniesList() {
    this.companyService.getCompanies().subscribe(companies => { this.companies = companies });
  }

}
