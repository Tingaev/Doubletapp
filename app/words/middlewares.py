from django.conf import settings
from rest_framework import request, status
from django.http import JsonResponse


def check_middleware(get_response):
    def middleware(request: request):
        code = request.headers.get('Secret')
        if code != settings.API_SECRET and not request.path.startswith('/admin/'):
            return JsonResponse(data={'error': 'Invalid secret key'}, status=status.HTTP_403_FORBIDDEN)
        response = get_response(request)
        return response
    return middleware
