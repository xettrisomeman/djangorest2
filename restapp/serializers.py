from rest_framework import serializers
from .models import (
    Person,
    Address
)


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        moddel = Address
        fields = "__all__"

