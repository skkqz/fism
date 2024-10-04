from rest_framework import serializers

from .models import Contract, ContractRisk
from modules.agents.models import Agent, Face
from modules.products.models import Risk
from modules.products.models import Product


class ContractSerializer(serializers.ModelSerializer):
    """
    Сериалайзер страхового договора.
    """

    agent = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all(), label='Агент')
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), label='Продукт')
    policy_holder = serializers.PrimaryKeyRelatedField(queryset=Face.objects.all(), label='Код страхователя')
    insured_person = serializers.PrimaryKeyRelatedField(queryset=Face.objects.all(), label='Код застрахованного лица')
    ownerId = serializers.PrimaryKeyRelatedField(queryset=Face.objects.all(), label='Код собственника')

    class Meta:
        model = Contract
        fields = (
            'id', 'agent', 'product', 'policy_holder', 'insured_person', 'ownerId', 'status', 'date_create',
            'date_signet', 'date_begin', 'date_end', 'premium', 'insurance_sum', 'rate', 'commission',
        )

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response


class ContractRiskSerializer(serializers.ModelSerializer):
    """
    Сериалайзер рисков по договорам.
    """

    contract = serializers.PrimaryKeyRelatedField(queryset=Contract.objects.all(), label='Договора страхования')
    risk = serializers.PrimaryKeyRelatedField(queryset=Risk.objects.all(), label='Страховые риски')

    class Meta:
        model = ContractRisk
        fields = ('id', 'contract', 'risk', 'premium', 'insurance_sum')

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response
