from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
]
