# from .models import Tenant
from .utils import set_current_request


class CurrentRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            db_name = request.user.subdomain
            set_current_request(db_name)
        response = self.get_response(request)
        return response


# class TenantMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         host_parts = request.get_host().split(".")
#         subdomain = host_parts[0] if len(host_parts) > 2 else None

#         try:
#             tenant = Tenant.objects.get(subdomain=subdomain)
#             request.tenant = tenant
#         except Tenant.DoesNotExist:
#             request.tenant = None

#         response = self.get_response(request)
#         return response
