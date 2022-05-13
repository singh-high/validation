from django.urls import path
from . import views


urlpatterns = [
    
        path('dist/',views.dist,name = 'dist'),
        path('dist_cust/',views.dist_cust,name = 'dist_cust'),  
        path('send_money/',views.send_money,name = 'send_money'),  
        path('fetch_data/',views.fetch_data,name = 'fetch_data'),  
]
