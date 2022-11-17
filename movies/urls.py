from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    # path('<int:')
    path('select/', views.select, name='select'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
]
