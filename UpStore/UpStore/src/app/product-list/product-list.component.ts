import { Component, OnInit } from '@angular/core';
import{Category} from '../category';
import{CategoriesService} from '../categories.service';
import { PRODUCTS } from '../mock-products';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Product } from '../products';
import {ProductService} from '../product.service'

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  category:Category;
 products=PRODUCTS;

   share() {
     window.alert('The product has been shared!');
   }
    constructor( private route: ActivatedRoute,
      private categoriesService: CategoriesService,
      private location: Location
      ) {  }

      ngOnInit(): void {
        this.getCategory();
      }

      getCategory(): void {
        const id = +this.route.snapshot.paramMap.get('id');
        this.categoriesService.getCategory(id)
          .subscribe(category => this.category = category);
      }

      goBack(): void {
        this.location.back();
      }

}
