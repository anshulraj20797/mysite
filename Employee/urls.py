from django.urls import path
from Employee import views

urlpatterns = [
    path('',views.EmpForm,name='EmpForm')
]
