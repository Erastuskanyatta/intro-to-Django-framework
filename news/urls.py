from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome')
]

urlpatterns=[
    path('',views.new_of_day, name='new_of_day')
]