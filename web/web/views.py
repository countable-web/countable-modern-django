from rest_framework import generics
from web.models import AppModel
from web.serializers import AppModelSerializer

# Add your API views here.


class AppModelList(generics.ListCreateAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer


class AppModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer
