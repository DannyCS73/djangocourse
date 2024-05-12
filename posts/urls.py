from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', PostViewset, basename="posts")

urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.PostListCreateView.as_view(), name="posts_listcreate"),
    path("<int:pk>", views.PostRetrieveUpdateDeleteView.as_view(), name="posts_by_id")

]

# urlpatterns += router.urls

