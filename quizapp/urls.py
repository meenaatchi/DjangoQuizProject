from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('registration', views.register, name='registration'),
    path('pythonquiz', views.pythonquiz, name='pythonquiz'),
    path('djangoquiz', views.djangoquiz, name='djangoquiz'),
    path('end', views.end, name='end'),

]
