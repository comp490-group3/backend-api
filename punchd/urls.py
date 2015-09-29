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
    # url(r'^accounts/', include('allauth.urls')),
    # (r'^rest-auth/', include('rest_auth.urls')),
    # (r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^business/$', views.BusinessListView.as_view(), name='business-index'),
    url(r'^business/(?P<pk>[0-9]+)/$', views.BusinessDetailView.as_view(), name='business-detail'),
    url(r'^business/add/$', views.BusinessCreateView.as_view(), name='business-add'),
    url(r'^business/(?P<pk>[0-9]+)/edit/$', views.BusinessUpdateView.as_view(), name='business-update'),
    # url(r'^business/offer/(?P<pk>[0-9]+)/$', views.OfferListView.as_view(), name='offer-index'),
    url(r'^business/(?P<bid>[0-9]+)/offer/(?P<pk>[0-9]+)/$', views.OfferDetailView.as_view(), name='offer-detail'),

]