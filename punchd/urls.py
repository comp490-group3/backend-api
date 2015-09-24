from django.conf.urls import include, url

from . import views
from rest_framework import routers

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'businesses', views.BusinessViewSet)

router.register(r'offers', views.OfferViewSet, base_name='offer')
# router.register(r'offerinstances', views.OfferInstanceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]