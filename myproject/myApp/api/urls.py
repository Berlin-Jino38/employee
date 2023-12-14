from . import views
from django.urls import path

urlpatterns = [
   path('employee/', views.MovieListCreate.as_view()),
   path('employee/<int:pk>/', views.MovieRetriveUpdateDestroy.as_view())
   
]