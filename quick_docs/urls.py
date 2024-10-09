from django.contrib import admin
from django.urls import path, include
from quick_docs_drf.urls import quick_docs_urls
from rest_framework.routers import DefaultRouter
from quick_docs.views import BlogViewSet, UserViewSet


router = DefaultRouter()
router.register("blog", BlogViewSet, basename="blog")
router.register("users", UserViewSet, basename="user")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
] + quick_docs_urls
