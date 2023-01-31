from django.urls import path

from studentapp import views

urlpatterns=[
    path('', views.log_fun, name='login'),# it will redirected to log in page
    path('logdata',views.logdata),#it will return to home page & check user is super user or not
    path('reg',views.reg_fun,name='reg'),#it will redirected to register.html page
    path('regdata',views.regdata_fun),# it will create super user
    path('home',views.home,name='home'),
    path('add_students',views.add_stu_fun,name='add'),
    path('reddata',views.reddata_fun) ,# it will insert records into student table
    path('display',views.display,name='dis'),
    path('up/<int:id>',views.update,name='up'),
    path('del/<int:id>',views.delete,name='del'),
    path('logout',views.log_out,name='log_out')


]