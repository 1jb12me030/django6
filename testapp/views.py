# from django.shortcuts import render
# from testapp.forms import StudentRegistration

# # Create your views here.
# def showformdata(request):
#     fm = StudentRegistration()
#     return render(request, 'testapp/userregistration.html',{'form':fm})
from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
	context ={}
	context['form']= StudentRegistration()
	return render(request, "testapp/userregistration.html", context)
