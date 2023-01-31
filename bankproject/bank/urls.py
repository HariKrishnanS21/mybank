from django.urls import path
from . import views
app_name='bank'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('form/',views.forms,name='forms'),
    path('logout/',views.logout,name='logout'),
    path('dist-json/',views.get_json_district,name='dist-json'),
    path('form/branch-json/<str:district>/',views.get_branches,name='branch-json'),
    path('success',views.success,name='success')
]