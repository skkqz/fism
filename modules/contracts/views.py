from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .models import Contract, ContractRisk
from .serializer import ContractSerializer, ContractRiskSerializer


class ContractView(ModelViewSet):
    """
    Представление для подразделения агента.
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class ContractRiskView(ModelViewSet):
    """
    Представление для подразделения агента.
    """

    queryset = ContractRisk.objects.all()
    serializer_class = ContractRiskSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
