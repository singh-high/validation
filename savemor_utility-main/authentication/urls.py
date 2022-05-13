from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('',views.userlogin,name='userlogin'),
    path('login/',views.userlogin,name='userlogin'),

    path('singup/',views.usersingup,name='usersingup'),

    path('logout/',views.userlogout,name='userlogout'),

    path('changepwd/',views.userpwdchange,name='userpwdchange'),

    path('terms/',views.terms,name='terms'),
     
    path('reset_password',auth_views.PasswordResetView.as_view(template_name = 'auth/forget_password.html'),name='reset_password'),

    path('reset_password_done',auth_views.PasswordResetDoneView.as_view(template_name ='auth/password_resetdone.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name ='auth/password_reset.html'),name='password_reset_confirm'),

    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name ='auth/password_complete.html'),name='password_reset_complete'),
]
