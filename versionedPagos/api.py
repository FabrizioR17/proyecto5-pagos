from .models import Services,Expired_payments,Payment_user
from rest_framework import viewsets
from .serializer import versionedPagosSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.get_queryset().order_by('id')
    serializer_class = versionedPagosSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    search_fields = ['Id', 'Name']
    throttle_scope = 'versionedPagos'

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.get_queryset().order_by('id')
    serializer_class = versionedPagosSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'