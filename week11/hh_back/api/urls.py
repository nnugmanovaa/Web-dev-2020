from django.urls import path

from api.views import companies_list,category_detail,vacancies_list,vacancy_detail,company_vacancies,top_vacancies

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:company_id>/', category_detail),
    path('vacancies', vacancies_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('companies/<int:company_id>/vacancies', company_vacancies),
    path('vacancies/top_ten', top_vacancies)
]