
from django.urls import path
from . import views

urlpatterns = [
    path('text/', views.text_response_view),
    path('template/', views.html_template_view),
]
