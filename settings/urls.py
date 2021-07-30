from django.urls import include, path, re_path
from rest_framework import routers
from core import views
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include("djoser.urls.authtoken")),
    re_path(r"static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    re_path(r"src/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    re_path(
        r"^.*$",
        TemplateView.as_view(template_name="base.html")
    )
]
