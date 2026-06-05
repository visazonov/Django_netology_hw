from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Sensor
from .models import Measurement
from .serializers import (SensorDetailSerializer, SensorSerializer, MeasurementSerializer)


# from .serializers import WeaponSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

@api_view(['GET'])
def api_measurement(request):
    return Response({'message': 'test_api'})


class SensorViews(ListCreateAPIView):
    queryset = Sensor.objects.all()
    # serializer_class = SensorDetailSerializer
    serializer_class = SensorSerializer


class UpdateSensorViews(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class AddMeasurementViews(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer






