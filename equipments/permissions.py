from rest_framework import permissions
import ipdb
from django.forms.models import model_to_dict


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return bool(request.user.is_authenticated and request.user.is_superuser)
