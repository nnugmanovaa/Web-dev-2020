import { Component, OnInit } from '@angular/core';
import {Vacancy} from '../../models/entities/vacancy';
import {Company} from '../../models/entities/company';
import {CompanyService} from '../../services/company.service';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {
  vacancies: Vacancy[];
  company: Company;
  id: number;
  constructor(public companyService: CompanyService,
              private route: ActivatedRoute,
              private location: Location,
              public router: Router) { }

  ngOnInit(): void {
    this.getVacancyList();
    this.getCompany();
  }

  getVacancyList() {
    const id = +this.route.snapshot.paramMap.get('companyId');
    this.companyService.getCompanyVacancies(id)
      .subscribe( vacancies => this.vacancies = vacancies);
  }
  getCompany() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getCompany(id).subscribe(company => this.company = company);
  }

}
