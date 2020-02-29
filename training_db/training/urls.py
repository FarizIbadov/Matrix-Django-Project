from django.urls import path, include
from .views import *


app_name = 'training'

urlpatterns = [
    # path('', home, name='home'),
    path('matrix/', HomeView.as_view(), name='home'),
    path('reports/', ReportView.as_view(), name='report'),
    path('search/', SearchView.as_view(), name='search'),
    path('edit/', EditView.as_view(), name='edit'),
    path('upload/', UploadView.as_view(), name='upload'),
]