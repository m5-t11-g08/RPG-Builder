from rest_framework import exceptions, status

class Character404(exceptions.APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Character not found."