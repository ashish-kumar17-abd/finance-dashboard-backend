from rest_framework import viewsets, permissions
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import IsAnalystOrAdminOrReadOnly


class FinancialRecordViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialRecordSerializer
    permission_classes = [permissions.IsAuthenticated, IsAnalystOrAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        queryset = FinancialRecord.objects.filter(user=user)

        # 🔍 Filters
        category = self.request.query_params.get('category')
        record_type = self.request.query_params.get('type')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if category:
            queryset = queryset.filter(category__iexact=category)

        if record_type:
            queryset = queryset.filter(type=record_type)

        if start_date:
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)