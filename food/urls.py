from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.login_view, name='home' ),
    path('inventory/', include('inventory.urls')),
    path('users/', include('users.urls')),
   
]

urlpatterns += staticfiles_urlpatterns()
