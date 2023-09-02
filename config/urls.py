from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/', include('transaction.urls')),
    path('api/v1/wallets/', include('wallet.urls')),    
]

# SWAGGER
if (settings.DEBUG):
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
    urlpatterns += [        
        path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/v1/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
    
#  DEBUG TOOLBAR
urlpatterns +=[
    path('__debug__/', include(debug_toolbar.urls)),
]
