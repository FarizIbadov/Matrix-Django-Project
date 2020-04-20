from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, DetailView
# from rest_framework.views import APIView
# from .forms import *
from training.models import *
from django.core.paginator import Paginator
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import django_excel as excel
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django import forms
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return render(request, 'training/matrix.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'training/matrix.html'
    context_object_name = 'matrix'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups']= TrainingGroup.objects.all()
        context['jobs']= TrainingMatrix.objects.all()
        # context['trainingeqpm']= TrainingMatrix.objects.filter(training__training_group__title="Equipment").all()
        context['trainingeqpm']= TrainingMatrix.objects.all()

        return context

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = 'training/report.html'

class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'training/search_edit.html'

class EditView(LoginRequiredMixin, TemplateView):
    template_name = 'training/edit.html'

class UploadView(LoginRequiredMixin, TemplateView):
    template_name = 'training/upload.html'


# class UploadExcel(TemplateView):
#     template_name = 'training/upload.html'

#     def post(self, request, format=None):
#        try:excel_file = request.FILES['files']
#        except MultiValueDictKeyError:
#             return redirect('training/matrix/')
#             if (str(excel_file).split('.')[-1] == "xls"):
#                 data = xls_get(excel_file, column_limit=4)
#             elif (str(excel_file).split('.')[-1] == "xlsx"):
#                 data = xlsx_get(excel_file, column_limit=4)
#             else:
#                 return redirect('<training/matrix/')
#             companies = data["Company"]
#             jobs = data["Job"]
#             if (len(companies) > 1): # We have company data
#                 for company in companies:
#                     if (len(company) > 0): # The row is not blank
#                     # This is not header
#                         if (company[0] != "No"): # Fill ending columns with blank
#                             if (len(company) < 4):
#                                 i = len(company)
#                                 while (i < 4):
#                                     company.append("")
#                                     i+=1 # Check if company exist
#                         # Assume that company name is unique
#                         name = company[1]
#                         c = Company.objects.filter(name=name)
#                     if ( c.count() == 0):
#                         Company.objects.create(name= company[1],address= company[2],kind= company[3])
#                     for job in jobs:
#                         if (len(job) > 0): # The row is not blank
#                             if (job[0] != "No"): # This is not header
#                                     # Get company that own this job
#                                 comp_id = int(job[-1])
#                                 name = companies[comp_id][1]
#                                 c = Company.objects.filter(name=name)
#                             if (c.count() > 0): # Company exist
#                                     Job.objects.create(company=c[0],name= job[1],salary= int(job[2]))
#                                     return redirect('training/matrix/')
        
# class UploadFileForm(forms.Form):
#     file = forms.FileField()

# def upload(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             filehandle = request.FILES['file']
#             return excel.make_response(filehandle.get_sheet(), "csv",
#                                        file_name="download")
#     else:
#         form = UploadFileForm()
#     return render(
#         request,
#         'training/upload.html',
#         {
#             'form': form,
#             'title': 'Excel file upload and download example',
#             'header': ('Please choose any excel file ' +
#                        'from your cloned repository:')
#         })
