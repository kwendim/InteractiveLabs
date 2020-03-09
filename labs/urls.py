from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<str:course_id>/', views.course),
#   this can be lab/<int: lab_id>
    path('course/<str:course_id>/<str:lab_id>', views.lab),
# Account paths
    path('accounts/login/', views.MyLoginView.as_view(), name='account_login'),
    path('accounts/signup/', views.MySignupView.as_view(), name='account_signup'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
]