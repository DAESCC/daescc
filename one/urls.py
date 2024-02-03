from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('event_calendar/', views.event_calendar, name='event_calendar'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('member_page/', views.member_page, name='member_page'),

]