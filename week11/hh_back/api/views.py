from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from api.models import Company, Vacancy


def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)

def category_detail(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
            return JsonResponse(company.to_json())
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

def company_vacancies(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        vacancies = company.vacancy_set.all()
        vacancies_json = [v.to_json() for v in vacancies]

        return JsonResponse(vacancies_json, safe=False)

def vacancies_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, vacancy_id):
    if request.method == "GET":
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            return JsonResponse(vacancy.to_json())
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})


def top_vacancies(request):
	if request.method == "GET":
		vacancies = Vacancy.objects.annotate(Count('salary')).order_by('-salary')[:10]
		vacancies_json = [vacancy.to_json() for vacancy in vacancies]
		return JsonResponse(vacancies_json, safe = False)



