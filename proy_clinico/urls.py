from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from applications.security.views.home import ModuloTemplateView
from applications.security.views.auth import signin, signout

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ruta principal a la página de inicio
    path('', ModuloTemplateView.as_view(), name='home'),

    # URLs bajo el namespace 'security'
    path('security/', include('applications.security.urls', namespace='security')),

    # Alias para que /auth/signin funcione también correctamente
    path('auth/', include('applications.security.urls', namespace='security_alias')),

    # Para el live reload de desarrollo
    path("__reload__/", include("django_browser_reload.urls")),
]


