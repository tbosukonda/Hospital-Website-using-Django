from django.contrib import admin
from django.urls import path
from .views import acceptappt,declineappt,adminappts,userappt,bookappt,userlogout,userauthenticate,customerwelcomeview,userloginview,signupuser,homepageview,deletedoctor,adddoctor,adminloginview,adminhomepageview,authenticateadmin, logoutadmin


urlpatterns = [
    path('admin/', adminloginview,name='adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/', logoutadmin),
    path('adddoctor/', adddoctor),
    path('deletedoctor/<int:doctorpk>/', deletedoctor),
    path('',homepageview, name = "homepage"),
    path('signupuser/',signupuser),
    path('loginuser/', userloginview, name='userloginpage'),
    path('customer/welcome/',customerwelcomeview,name = 'customerpage'),
    path('customer/authenticate/', userauthenticate),
    path('userlogout/',userlogout),
    path('bookappt/<int:doctorpk>', bookappt),
    path('userappt/',userappt),
    path('adminappts/',adminappts),
    path('acceptappt/<int:apptpk>/', acceptappt),
    path('declineappt/<int:apptpk>/', declineappt)
]