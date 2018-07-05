from django.urls import path

from timing import views

app_name = 'timing'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('save/', views.save, name='save'),
]
