from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import PeopleViewSet, UsersViewSet

router = DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')
router.register(r'users', UsersViewSet, basename='users')
urlpatterns = router.urls

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
