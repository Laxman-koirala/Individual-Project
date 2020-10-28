from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.Signup,name='signup'),
    path('',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('change_password/',views.Change_Password,name='changepassword'),
]
