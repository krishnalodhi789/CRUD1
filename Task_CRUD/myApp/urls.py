from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name='home'),
    path("userSignup",views.userSignup,name='userSignup'),
    path("userLogin",views.userLogin,name='userLogin'),
    path("userLogout",views.userLogout,name='userLogout'),
    
    path("userProfile",views.userProfile,name='userProfile'),
    path("updateProfile",views.updateProfile,name='updateProfile'),
    path("resetPassword1",views.resetPassword1,name='resetPassword1'),
    path("resetPassword2",views.resetPassword2,name='resetPassword2'),
]
