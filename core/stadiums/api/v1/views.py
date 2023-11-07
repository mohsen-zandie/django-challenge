from rest_framework import viewsets
from stadiums.api.v1.permissions import IsAdminOrReadOnly


from stadiums.models import Stadium
from stadiums.api.v1.serializers import StadiumSerializer, StadiumPlanSerializer


class StadiumModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()


class StadiumPlanModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StadiumPlanSerializer
    queryset = Stadium.objects.all()
