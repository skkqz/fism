from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import ContractRisk, Contract


@admin.register(Contract)
class ContractAdmin(ModelAdmin):

    list_display = ['agent', 'product', 'policy_holder', 'status', 'date_create']


@admin.register(ContractRisk)
class ContractRiskAdmin(ModelAdmin):

    list_display = ['contract', 'risk', 'premium', 'insurance_sum']
