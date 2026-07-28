from .views import signin, signup, signout, home
from django.urls import path

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),  
    path('', home, name='home'),
]