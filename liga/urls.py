import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teams.urls')),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls')),
    path('tienda/', include('tienda.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#path('__debug__/', include(debug_toolbar.urls)),
#static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)