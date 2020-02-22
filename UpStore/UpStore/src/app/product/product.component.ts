import { Component, OnInit } from '@angular/core';

import { PRODUCTS } from '../mock-products';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Product } from '../products';
import {ProductService} from '../product.service'

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  product:Product;
  constructor(private route: ActivatedRoute,
    private productService: ProductService,
    private location: Location) { }

  ngOnInit(): void {
    this.getProduct();
  }

  getProduct(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id)
      .subscribe(product => this.product = product);
  }
  
  goBack(): void {
    this.location.back();
  }

}
