from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from parts.requests.models import *


class PartRequestSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = PartRequest
        fields = "__all__"


class DecisionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Decision
        fields = "__all__"
