from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAnalystOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Read-only requests → sabko allowed
        if request.method in SAFE_METHODS:
            return True

        # Write requests → only ANALYST or ADMIN
        return request.user.role in ["ANALYST", "ADMIN"]