from django.urls import path
from . import views
from demo.views import hello

urlpatterns = [
    # path('',views.hello,name='hello'),
    path('time',views.time,name='time'),
    path('',hello),
]