from rest_framework import viewsets
from .models import (
    Person,
    Address
)


from .serializers import (
    PersonSerializer,
    AddressSerializer
)


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


