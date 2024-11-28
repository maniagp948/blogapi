from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail

urlpatterns = [
    path("users/", UserList.as_view()),  # type: ignore
    path("users/<int:pk>/", UserDetail.as_view()),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
]
