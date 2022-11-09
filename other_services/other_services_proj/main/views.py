from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

# Create your views here.

"""
    Данный метод позволяет получить справку выбранного вида
"""
def get_reference_by_student(request):
    

    return JsonResponse({'foo':'bar'})

"""
    Данный метод позволяет заполнить базу данных тестовыми документами студентов
"""
def seed_documents(request):
    pass

@csrf_exempt
def new_student(request):
    iin = request.GET.get("student")

    student = Student(stud_identificator=iin, grade=1)

    student.save()

    return JsonResponse({'response': 'success'})
