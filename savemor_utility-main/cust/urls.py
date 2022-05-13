from django.urls import path
from. import views


urlpatterns = [
   
    path('profile/',views.profile,name='profile'),


    path('applyFd/',views.applyFd,name = 'applyFd'),
    

    path('editprofile/',views.editprofile,name = 'editprofile'),
    path('setting/',views.setting,name = 'setting'),
   

    # path('certificate/',views.Viewpdf.as_view(),name = 'generate_certificate'),
    path('userfdform/',views.userfdform,name = 'userfdform'),
    path('applyForDistributor/',views.applyForDistributor,name = 'applyForDistributor'),


 
]
