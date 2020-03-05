from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_an, name='cv_an'),
    path('mech/', views.cv_mech, name='cv_mech'),
]