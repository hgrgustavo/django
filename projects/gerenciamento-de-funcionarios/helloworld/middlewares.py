from django.http import HttpResponseForbidden


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


class FilterIPMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request):
        ips = ["127.0.0.1"]
        user_ip = request.META.get("REMOTE_ADDR")

        if user_ip not in ips:
            return HttpResponseForbidden("IP não autorizado.")

        return None
