from django.urls import path

#from api.views import companies_list,category_detail,vacancies_list,vacancy_detail,company_vacancies,top_vacancies
from rest_framework_jwt.views import obtain_jwt_token

from api.views.views_cbv import CompanyListApiView, CompanyDetailApiView , VacancyListApiView, VacancyDetailApiView, \
    TopVacanciesApiView , VacanciesByCompanyApiView

urlpatterns = [
  #  path('companies/', companies_list),
  # path('companies/<int:company_id>/', category_detail),
  #  path('vacancies', vacancies_list),
  # path('vacancies/<int:vacancy_id>/', vacancy_detail),
  #  path('companies/<int:company_id>/vacancies', company_vacancies),
  #  path('vacancies/top_ten', top_vacancies)

    path('login', obtain_jwt_token),
    path('companies/', CompanyListApiView.as_view()),
    path('companies/<int:company_id>/', CompanyDetailApiView.as_view()),
    path('vacancies/', VacancyListApiView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyDetailApiView.as_view()),
    path('vacancies/top_ten', TopVacanciesApiView.as_view()),
    path('companies/<int:company_id>/vacancies', VacanciesByCompanyApiView.as_view()),
]