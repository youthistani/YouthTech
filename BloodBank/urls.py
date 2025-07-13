from django.urls import path
from . import views
urlpatterns = [
    path("", view=views.index, name="donation_list"),
    path('register_donor/', views.register_donor, name='register_donor')
]
