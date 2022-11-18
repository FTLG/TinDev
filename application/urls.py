from django.urls import path
from . import views

app_name = 'application'  # creates a namespace for this application

urlpatterns = [
    path('', views.index, name='index'),
    # path("signup/", views.SignUp.as_view(), name="signup"),
    # path("login/", views.Login.as_view(), name="login"),
    # path('', views.IndexView.as_view(), name='index'),

    path('candidates/', include(([
    ], 'application'), namespace='candidates')),

    path('recruiters/', include(([
    ], 'application'), namespace='recruiters')),

    # /polls/# ex: /polls/1
    # path('<int:pk>/', views.PostDetailView.as_view(), name='view'),
]
