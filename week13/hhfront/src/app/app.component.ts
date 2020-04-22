import {Component, OnInit} from '@angular/core';
import {CompanyService} from './services/company.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'hhfront';
  logged = false;

  username = '';
  password = '';

  constructor(public companyService: CompanyService) {}

  ngOnInit() {
    let token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  login() {
    this.companyService.login(this.username, this.password).subscribe(perf => {
      localStorage.setItem('token', perf.token);
      this.logged = true;

      this.username = '';
      this.password = '';
    });
  }

  logout() {
    localStorage.clear();
    this.logged = false;
  }
}
