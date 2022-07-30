from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from common import views as common_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace='authentication')),
    path('product/', include('product.urls', namespace='product')),
    path('vendor/', include('vendor.urls', namespace='vendor')),
    path('asset/', include('asset.urls', namespace='asset')),
    path('sale/', include('sale.urls', namespace='sale')),
    path('notification/', include('notification.urls', namespace='notification')),
    path('transaction/', include('vendor_transaction.urls', namespace='transaction')),
    path('trash/', include('trash.urls', namespace='trash')),

    #search view
    path('search', common_views.search, name='search'),

    #smart select
    path('chaining/', include('smart_selects.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)