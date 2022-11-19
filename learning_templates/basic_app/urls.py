
from django.urls import path,include
#from django.urls import include
from basic_app import views

#TEMPLATES TAGGING
app_name = 'basic_app'

urlpatterns = [
            path('relative/', views.relative, name = 'relative'),
            #cdpath('basic_app/', include('basic_app.urls')),
            path('other/', views.other, name = 'other'),
]
