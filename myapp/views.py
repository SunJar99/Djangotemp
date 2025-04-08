
from django.http import HttpResponse
from django.shortcuts import render

def text_response_view(request):
    return HttpResponse("Привет! Это текстовый ответ.")

def html_template_view(request):
    return render(request, 'myapp/sample.html')
