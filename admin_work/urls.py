from django.urls import path
from . import views

urlpatterns = [
    path('ad/', views.admin_view, name='admin_view'),
    path('admin_programs/', views.admin_programs, name='admin_programs'),
    path('admin_programs/create/', views.program_create, name='program_create'),
    path('admin_programs/<int:pk>/update/', views.program_update, name='program_update'),
    path('admin_programs/<int:pk>/delete/', views.program_delete, name='program_delete'),

    # Course URLs
    path('admin_courses/', views.admin_courses, name='admin_courses'),
    path('admin_courses/create/', views.course_create, name='course_create'),
    path('admin_courses/<int:pk>/update/', views.course_update, name='course_update'),
    path('admin_courses/<int:pk>/delete/', views.course_delete, name='course_delete'),

    # Application URLs
    path('admin_applications/', views.admin_applications, name='admin_applications'),
    path('admin_applications/create/', views.application_create, name='application_create'),
    path('admin_applications/<int:pk>/update/', views.application_update, name='application_update'),
    path('admin_applications/<int:pk>/delete/', views.application_delete, name='application_delete'),
]
