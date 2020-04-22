from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer

class CompanyListApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many= True)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CompanyDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id = id)
        except Company.DoesNotExist as e:
            return Response({'error' : str(e)})
    def get(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    def put(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    def delete(self, request, company_id):
        company = self.get_object(company_id)
        company.delete()
        return Response({'deleted': True})


class VacancyListApiView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many= True)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VacancyDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id = id)
        except Vacancy.DoesNotExist as e:
            return Response({'error' : str(e)})
    def get(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    def put(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    def delete(self, request, vacancy_id):
        company = self.get_object(vacancy_id)
        company.delete()
        return Response({'deleted': True})


class TopVacanciesApiView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many= True)
        return Response(serializer.data)


class VacanciesByCompanyApiView(APIView):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id = company_id)
            serializer = CompanySerializer(company)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})
        vacancies = company.vacancy_set.all()
        serializer = VacancySerializer(vacancies, many= True)
        return  Response(serializer.data)