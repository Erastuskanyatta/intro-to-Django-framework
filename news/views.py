from django.shortcuts import render

from django.http import HttpResponse

#Create your views here.
def welcome(request):
    return HttpResponse('Welcome to django')
    
    
import datetime as dt
    
def new_of_day(request):
        date = dt.date.today()
        html = f'''
        <html>
        <body>
        <h1>{date.day}-{date.month}-{date.year}</h1>
        </body>
        </html>
        '''
        return HttpResponse(html)
        
        
        