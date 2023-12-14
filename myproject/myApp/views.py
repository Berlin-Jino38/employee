from django.shortcuts import render
from .models import EmployeeModel
# Create your views here.
def index(request):
    emp=EmployeeModel.objects.all()
    
    return render(request,'index.html',{'emp':emp})