from django.urls import path

from influencers import views


urlpatterns = [
    path('', views.mainpage, name='mainpage')




]