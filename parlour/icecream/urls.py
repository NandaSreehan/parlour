from django.urls import path
from icecream import views
urlpatterns=[
    path('view',views.view,name="ice"),
    path('update',views.update,name='update'),
    path('remove',views.rem,name='removeObj')
    
]

