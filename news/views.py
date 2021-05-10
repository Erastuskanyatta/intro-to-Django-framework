from django.shortcuts import render

from django.http import HttpResponse,Http404
# import datetime as dt
# import datetime

def welcome(request):
    return render(request, 'welcome.html')   

# def past_days_news(request,past_date):
#     try:

#         date = dt.datetim.strptime(past_date, '%Y-%m-%d').date()
#     except ValueError:
#         raise Http404()



# def convert_dates(dates):

#      day_number = datetime.date.weekday(dates)

#      days = ['Monday','Tuesday','Wedno','Thursday','Friday','Saturday','Sunday']    

#      # returning actual day of the week
#      day = days[day_number]   
#      return day

# def new_of_day(request):

#      date = dt.date.today()

#      day = convert_dates(date)
#      html = f'''
#      <html>
#      <body>
#      <h1> News of the {date.day}-{date.month}-{date.year} on {day}   </h1>
#      </body>
#      </html>
#      '''
#      return HttpResponse(html)

# def past_days_news(request,past_date):
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%m-%d-%year').date()
#         day = convert_dates(date)
#         html = f'''
#         <html>
#             <body>
#                 <h1>News for {month} {date.month}-{date.day}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#         return HttpResponse(html)

    
