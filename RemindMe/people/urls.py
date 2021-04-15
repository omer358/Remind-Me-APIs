from django.urls import path, include
from . import views

urlpatterns = [
    path('people/', views.PeopleList.as_view()),
    path('people/<int:pk>', views.PersonDetails.as_view()),
    path('users/', views.UserList.as_view()),
]
