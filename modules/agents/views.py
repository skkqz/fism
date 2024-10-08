from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .models import Face, Agent, Division, AgentAgreements
from .serializer import FaceSerializer, AgentSerializer, DivisionSerialize, AgentAgreementsSerializer
from modules.permissons import IsAgentOrAdminPermission


class DivisionView(ModelViewSet):
    """
    Представление для подразделения агента.
    """

    queryset = Division.objects.all()
    serializer_class = DivisionSerialize
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class AgentView(ModelViewSet):
    """
    Представление для агента.
    """

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class FaceView(ModelViewSet):
    """
    Представление для контрагента.
    """

    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class AgentAgreementsView(ModelViewSet):
    """
    Представление для контрагента.
    """

    queryset = AgentAgreements.objects.all()
    serializer_class = AgentAgreementsSerializer
    permission_classes = [IsAuthenticated, IsAgentOrAdminPermission, DjangoModelPermissions]
