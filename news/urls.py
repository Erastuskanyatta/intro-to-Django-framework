from django.urls import path
from . import views

urlpatterns=[
    # path('',views.welcome,name = 'welcome')
    path('',views.past_days_news, name = 'pastNews')  
]

urlpatterns=[
    path('',views.new_of_day, name='new_of_day')
    
]

