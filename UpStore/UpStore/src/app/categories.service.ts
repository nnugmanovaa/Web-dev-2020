import { Injectable } from '@angular/core';
import { Category } from './category';
import { CATEGORIES } from './mock-categories';
import { Observable, of } from 'rxjs';
import {PRODUCTS} from './mock-products'
import { ProductComponent } from './product/product.component';
@Injectable({
  providedIn: 'root'
})
export class CategoriesService {

  constructor() { }

  getCategories():  Observable<Category[]> {
    return of(CATEGORIES);
  }

  getCategory(id: number): Observable<Category> {

    return of(CATEGORIES.find(category => category.id === id));
  }
}
