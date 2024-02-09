from django.urls import path
from .views import *

urlpatterns = [
    path('home',home,name="homepage"),
    path('booking/',booking,name="bookingpage"),
    path('department/',department_fun,name="deptpage"),
    path('doctors/',docs_fun,name="doctorpage"),
    path('about/',about,name="aboutpage"),
    path('',signup,name="signuppage"),
    path('login/',user_login,name="loginpage"),
]