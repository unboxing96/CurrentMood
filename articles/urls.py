from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.private, name="private"),
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("locations/", views.location_get, name="locations"),
    path("<int:pk>/like/", views.like, name="like"),
    path("<int:pk>/songlike/", views.songlike, name="songlike"),
    path("public/", views.public, name="public"),
    path("test/", views.test, name="test"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path("song/", views.song, name="song"),
    path("song/<slug:video_id>/", views.song_detail, name="song_detail"),
    path("song/<int:pk>/like/", views.song_like, name="song_like"),
    path("create_test/", views.create_test, name="create_test"),
]
