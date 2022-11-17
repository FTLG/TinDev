from django.urls import path
from . import views

app_name = 'application'  # creates a namespace for this application

urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/# ex: /polls/1
    # path('<int:pk>/', views.PostDetailView.as_view(), name='view'),
]
