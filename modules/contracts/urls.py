from django.urls import path
from rest_framework import routers

from .views import ContractView, ContractRiskView

app_name = 'agents'

router = routers.SimpleRouter()
router.register('contracts', ContractView, basename='contracts')
router.register('contracts_risk', ContractRiskView, basename='contracts_risk')


urlpatterns = router.urls
