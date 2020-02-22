import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CategoriesComponent } from './categories/categories.component';
import {ProductComponent} from './product/product.component'
import { PRODUCTS } from './mock-products';

import { ProductListComponent } from './product-list/product-list.component';


const routes: Routes = [
  { path: 'categories', component: CategoriesComponent },
  {path: '', redirectTo: '/categories', pathMatch: 'full' },
  
  { path: 'categoryId/:id', component: ProductListComponent},
  { path: 'productId/:id', component: ProductComponent},
  
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }