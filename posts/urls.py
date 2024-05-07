from . import views
from django.urls import path
from posts.views import PostViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PostViewset, basename="posts")

urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
]

urlpatterns += router.urls

