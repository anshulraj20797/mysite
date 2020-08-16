from django.shortcuts import render

def EmpForm(request):
    return render(request,'Employee/index.html')