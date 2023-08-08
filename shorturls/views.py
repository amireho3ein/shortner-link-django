from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import URL
from .serializers import URLSerializer
from rest_framework.permissions import AllowAny
import random
import string



def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code


class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        long_url = serializer.validated_data['long_url']
        short_code = generate_short_code()
        url = URL(long_url=long_url, short_code=short_code)
        url.save()
        headers = self.get_success_headers(serializer.data)
        url_detail = reverse('url-detail', args=[url.id], request=request)
        return Response({'url': url_detail},serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @api_view(['GET'])
    def get_long_url(self, request, short_code):
        try:
            url = URL.objects.get(short_code=short_code)
            return Response({'long_url': url.long_url}, status=status.HTTP_302_FOUND)
        except URL.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class URLListView(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    