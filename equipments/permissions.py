from rest_framework import permissions
import ipdb
from django.forms.models import model_to_dict


class IsAdm(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.is_superuser == True:
            return True
