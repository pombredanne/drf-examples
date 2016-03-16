from rest_framework import serializers

from .models import Invoice, Attribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'name')


class AttrPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        queryset = Attribute.objects.filter(user=user)
        return queryset


class InvoiceSerializer(serializers.ModelSerializer):
    attributes = AttrPKField(many=True)

    class Meta:
        model = Invoice
        fields = ('id', 'name', 'attributes')
