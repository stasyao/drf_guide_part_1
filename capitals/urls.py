from django.urls import path

from . import views

urlpatterns = [
    path('api/capitals/', views.GetCapitalInfoView.as_view()),
    path('', views.main_page, name='main_page'),
]
