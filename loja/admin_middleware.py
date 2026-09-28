from django.urls import reverse
from django.utils import translation


class AdminLanguageMiddleware:
    """Aplica português somente às páginas do Django Admin."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path_info.startswith(reverse('admin:index')):
            with translation.override('pt-br'):
                return self.get_response(request)
        return self.get_response(request)
