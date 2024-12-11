from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from common.articles.views import ArticleViewSet
from common.pages.views import RootView, SlugView

router = DefaultRouter()
router.register(r"articles", ArticleViewSet, basename="article")

urlpatterns = [
    path("", RootView.as_view(), name="root-view"),
    path('<slug:slug>/', SlugView.as_view(), name='slug-view'),
    path("api/", include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )