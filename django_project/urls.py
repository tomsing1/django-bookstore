from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = (
    [
        # Django admin
        path("anything-but-admin/", admin.site.urls),
        # User Management
        path("accounts/", include("allauth.urls")),
        # Local apps
        path("", include("pages.urls")),
        path("books/", include("books.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)
