from rest_framework import serializers

from web.models import AppModel

# Add your app serializers here.


class AppModelSerializer(serializers.ModelSerializer):
    queryset = AppModel.objects.all()

    class Meta:
        model = AppModel
        fields = ("id",)
