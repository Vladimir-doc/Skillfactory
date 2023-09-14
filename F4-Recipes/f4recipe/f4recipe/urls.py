
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin


schema_view = get_schema_view(
    openapi.Info(
        title="Recipes API",
        default_version='1.0.0',
        description="For test app",
        contact=openapi.Contact(email="applicationspb@yandex.ru"),
        license=openapi.License(name="NoLicense"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]