from django.urls import path, include
from . import views

urlpatterns = [
    path('people/', views.PeopleList.as_view()),
    path('people/<int:pk>/', views.PeopleDetails.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
]
