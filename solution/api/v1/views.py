from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from ads.models import Advertisement
from ads.serializers import AdvertisementSerializer
from users.serializers import UserRegistrationSerializer


class AdsListAPIView(APIView):
    '''
    View для получения списка объявлений с пагинацией 10, сортированных по id.
    '''
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get(self, request, format=None):
        paginator = self.pagination_class()
        advertisements = Advertisement.objects.all().order_by('id')
        result_page = paginator.paginate_queryset(advertisements, request)
        serializer = AdvertisementSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class AdsDetail(generics.RetrieveAPIView):
    '''
    View для получения информации о конкретном объявлении.
    '''
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class UserRegistrationAPIView(APIView):
    '''
    View для регистрации пользователя, получения и обновления токена.
    '''
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
