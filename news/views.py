from django.shortcuts import render

from django.http import HttpResponse
import datetime as dt

#Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to django')
    
    
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

def convert_dates(dates):

     day_number = datetime.date.weekday(dates)

     days = ['Monday','Tuesday','Wedno','Thursday','Friday','Saturday']    
     # returning actual day of the week

     day = days[day_number]   
     return day

def new_of_day(request):

     date = dt.date.today()

     day = convert_dates()
     html = f'''
     <html>
     <body>
     <h1> News of the {day} {date.day}-{date.month}-{date.year}  </h1>
     </body>
     </html>
     '''
     return HttpResponse(html)

def past_days_news(request,past_date):
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
        day = convert_dates(date)
        html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
        return HttpResponse(html)