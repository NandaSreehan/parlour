from django.urls import path
from notification import views
urlpatterns=[
    path('notice',views.note,name='Notes'),
]