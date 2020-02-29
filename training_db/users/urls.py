# from django.urls import path, include, re_path
# from .views import *
# from django.contrib.auth.views import LogoutView

# app_name = 'users'

# urlpatterns = [
#     path('login/', CustomLoginView.as_view(), name='login' ),
#     path('logout/', LogoutView.as_view(), name="logout"),
# ]

from django.urls import path, include, re_path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login' ),
]