from django.urls import path
from .views import Home, PostDetail, PostCreate, PostUpdate, UserSpecific


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("post/<int:pk>", PostDetail.as_view(), name="post"),
    path("create_post", PostCreate.as_view(), name="create_post"),
    path("update_post/<int:pk>", PostUpdate.as_view(), name="update_post"),
    path("index_page", UserSpecific, name="index_page"),


]