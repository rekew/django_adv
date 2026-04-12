# DRF modules
from rest_framework.routers import DefaultRouter
# Django modules
from django.contrib import admin
from django.urls import path, include
# Project modules
from apps.blogs.views import CategoryViewSet, PostViewSet, StatsViewSet, TagViewSet, post_stream

router = DefaultRouter()

router.register(r"posts", PostViewSet, basename="post")
router.register(r"stats", StatsViewSet, basename="stats")
router.register(r'categories', CategoryViewSet, basename="category")
router.register(r'tags', TagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
    path("stream/posts/", post_stream),

]
