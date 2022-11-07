from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return request.user.is_authenticated and request.user.is_superuser
        
class IsOwner(BasePermission):
    def has_permission(self, request, view):
        requested_id = int(request.path.split("/")[3])
        return request.user.id == requested_id