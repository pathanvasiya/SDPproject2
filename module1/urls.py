from django.urls import path
from .views import *

urlpatterns = [
    path("hello/",hello1),
    path('hello1/',hello,name='hello'),
    path("",newhomepage,name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('r/',random123,name='random123'),
    path('ran1/',random1,name='random1'),
    path('date1/',getdate1,name='getdate1'),
    path('date/',get_date,name='get_date'),
    path('time/',tzfunctioncall,name='pytzexample'),
    path('reg/',registerloginfunction,name='registerloginfunction'),
    path('register/',registerlogin,name='registerlogin'),
    path('pie1/', Pie, name='Pie'),
    path('s/',slide,name='slide'),
    path('t/',temp,name='temp'),
    path('w/',weatherlogic,name='weatherlogic'),
    path('login/',login1,name='login1'),
    path('signup/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('lo/',login,name='login'),
    path('si/',signup,name='signup'),

]