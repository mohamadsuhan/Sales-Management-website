
from django.urls import path

from Sales import views

urlpatterns = [
    path('',views.login_fun,name='log'),
    path('signup/',views.signup_fun),
    path('home/',views.homestudent),
    path('add/',views.addstudent),
    path('Display/',views.DisplayStudent,name="Display"),
    path('Update/<int:id>',views.Update_student,name="update"),
    path('Delete/<int:id>',views.Delete_student,name="delete"),
    ]