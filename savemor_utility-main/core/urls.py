from django.urls import path
from . import views

urlpatterns = [
    path('wallet/',views.wallet,name = 'wallet'),
    path('withdraw/',views.withdraw,name = 'withdraw'),
    path('kyc/',views.kyc,name = 'kyc'),
    path('handelrequest/',views.handelrequest,name = 'handelrequest'),
    path('contactus/',views.contactus,name = 'contactus'),
    path('aboutus/',views.aboutus,name = 'aboutus'),
]
