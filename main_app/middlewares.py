from .utils import set_current_request
from rest_framework.authentication import TokenAuthentication
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser


class CurrentRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host_parts = request.get_host().split(".")
        subdomain = host_parts[0] if len(host_parts) >= 2 else None
        if subdomain:
            set_current_request(subdomain)

        response = self.get_response(request)
        return response
