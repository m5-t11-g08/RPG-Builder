from rest_framework import permissions


class OwnAccountOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True

        return bool(request.user.is_authenticated and request.user.id == obj.id)


class OwnAccountPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and request.user.id == obj.id)