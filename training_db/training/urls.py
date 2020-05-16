from django.urls import path, include
from .views import *

app_name = 'training'

urlpatterns = [
    path('matrix/', HomeView.as_view(), name='home'),
    path('reports/', ReportView.as_view(), name='report'),
    path('search/', SearchView.as_view(), name='search'),
    path('search/specific', SearchEditView.as_view(), name='search-specific'),
    path('matrix/edit/', EditView.as_view(), name='edit'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('logout/', logout_view, name = "logout"),
]