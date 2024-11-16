from django.contrib import admin
from django.urls import path, include
from registration import views as rv
from .settings import SECRET_ADMIN_URL

# customize admin site
admin.site.site_header = 'SecureSync Admin'
admin.site.site_title = 'SecureSync Admin Dashboard'
admin.site.index_title = 'SecureSync Admin'

urlpatterns = [
    path(SECRET_ADMIN_URL + 'admin/', admin.site.urls),
    path("", include("registration.urls")),
    path("", include("chat.urls")),
]