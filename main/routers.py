from rest_framework import routers

from restapp.apiviews import (
    PersonViewSet,
    AddressViewSet
)

router = routers.DefaultRouter()

router.register('person' , PersonViewSet,basename='person')
router.register('address' , AddressViewSet,basename='address')


urlpatterns = router.urls

