from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def hello(request):
    return HttpResponse("Hello World")

# def time(request):
#     now = date.today()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(now)
def time(request):
    todaydatetime = datetime.now()
    context = {
        'todaydatetime' : todaydatetime
    }
    return render(request,'demo/current_datetime.html',context)
    #return render(request, 'listings/listings.html', context)






    # now = datetime.now
    # html = "<html><body>It is now {{now}}.</body></html>"
    # return HttpResponse(now)