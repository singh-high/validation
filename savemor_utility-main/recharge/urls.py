from django.urls import path
from . import views

urlpatterns = [
    path('mrecharge/',views.Mobile_recharge,name = 'mrecharge'),
    path('dthrecharge/',views.Dth_Recharge,name = 'dthrecharge'),
    path('electricityrecharge/',views.electricityrecharge,name = 'electricityrecharge'),

    path('subscription/',views.Subscription,name = 'subscription'),


    path('success/',views.success,name = 'success'),
    path('successApi/',views.successApi,name = 'successApi'),

]
