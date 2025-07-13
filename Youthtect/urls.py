from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blood/', include('BloodBank.urls')),
    path('', include('website.urls')),
    path('blog/', include('Blogs.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin_work/', include('admin_work.urls'))
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
