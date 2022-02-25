from django.urls import path, include
from users.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.User)
router.register('student', views.student)


urlpatterns = [
    path('', include(router.urls)),

]