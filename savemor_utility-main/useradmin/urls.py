from django.urls import path
from . import views

urlpatterns = [
    
    path('adminuser/',views.admindisplay,name = 'admindisplay'),
    path('allusers/',views.allusers,name = 'allusers'),

    path('adminedit/<int:pk>/',views.admin_user_edit,name = 'admin_user_edit'),
    path('recharge_done/<int:pk>/',views.recharge_done,name = 'recharge_done'),
    path('recharge_admin/',views.recharge_admin,name = 'recharge_admin'),
    path('allforms/',views.allforms,name = 'allforms'),



]
