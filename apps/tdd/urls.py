from django.urls import path
from . import views

app_name="tdd"

urlpatterns = [
    path('', views.index, name="index")
]