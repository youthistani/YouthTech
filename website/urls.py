from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('programs/', views.programs, name='programs'),
    path('programs/<pk>/', views.program_details, name='program_detail'),
    path('admission_success/', views.admission_success, name='admission_success'),
    path('about/', views.about, name='about'),
    # path for contact page
    path('contact/', views.contact, name='contact'),
    path('results', views.show_result, name="results"),
    path('results/verify/', views.verify_result, name='verify_result'),
    path('certificate/verify/', views.verify_certificate, name='verify_certificate'),
]

