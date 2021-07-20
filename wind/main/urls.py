from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('question/<int:pk>', views.view_question, name='question'),
    path('create', views.create_question, name='create')
]
