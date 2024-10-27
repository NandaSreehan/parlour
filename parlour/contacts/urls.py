from django.urls import path
from contacts import views
urlpatterns=[
    path('name',views.con,name='contacts'),
    path('add',views.add,name='addContact'),
    path('update',views.update,name='updateContact'),
    path('rem',views.rem,name='deletecontact'),
    
    
]