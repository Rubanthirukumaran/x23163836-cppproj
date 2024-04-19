from django.contrib import admin
from .views import redirect_to_home

from django.urls import path, include


urlpatterns = [
    path('', redirect_to_home, name='root'),
    path('admin/', admin.site.urls),
    path('fundraising/', include('fundraising.urls')),
]
