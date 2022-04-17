from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework.viewsets import GenericViewSet 
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
import os 
# index_view = never_cache(TemplateView.as_view(template_name='index.html'))
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class PingViewSet(GenericViewSet, ListModelMixin):
    """
    Helpful class for internal health checks
    for when your server deploys. Typical of AWS
    applications behind ALB which does default 30
    second ping/health checks.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response(
            data={"id": request.GET.get("id")},
            status=HTTP_200_OK
        )
