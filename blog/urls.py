from django.urls import path
from .views import Home, PostDetail, PostCreate


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("post/<int:pk>", PostDetail.as_view(), name="post"),
    path("create_post", PostCreate.as_view(), name="create_post"),
]