from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


def home(request):
    return HttpResponse("HealthyRice AI API is successfully running on Vercel!")



api_v1_patterns = [
    path("auth/", include("accounts.urls")),
    path("diseases/", include("diseases.urls")),
    path("detections/", include("detection.urls")),
]

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    path("api/v1/", include(api_v1_patterns)),

    path("api/auth/", include("accounts.urls")),
    path("api/diseases/", include("diseases.urls")),
    path("api/detections/", include("detection.urls")),


    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
