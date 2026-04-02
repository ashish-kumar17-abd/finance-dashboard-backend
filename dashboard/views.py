from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from records.models import FinancialRecord
from decimal import Decimal


class DashboardAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        records = FinancialRecord.objects.filter(user=user)

        # ✅ Totals (safe for Decimal)
        total_income = records.filter(type="INCOME").aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0')

        total_expense = records.filter(type="EXPENSE").aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0')

        balance = total_income - total_expense

        # 📊 Category-wise Expense (Pie Chart)
        category_data = records.filter(type="EXPENSE") \
            .values('category') \
            .annotate(total=Sum('amount')) \
            .order_by('-total')

        # 📈 Monthly Data (Line Chart)
        monthly_data = records.values('date__year', 'date__month') \
            .annotate(total=Sum('amount')) \
            .order_by('date__year', 'date__month')

        # 🕒 Recent Transactions
        recent = records.order_by('-date')[:5].values(
            'amount', 'type', 'category', 'date'
        )

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
            "category_expense": category_data,
            "monthly_data": monthly_data,
            "recent_transactions": recent
        })