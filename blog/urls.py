from django.urls import path
from .views import (Home, PostDetail, PostCreate,
                    UserSpecific, PostUpdate)
from users.views import Profile


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("post/<int:pk>", PostDetail.as_view(), name="post"),
    path("create_post", PostCreate.as_view(), name="create_post"),
    path("specific_posts", UserSpecific, name="specific_posts"),
]