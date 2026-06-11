from django.conf.urls.static import static
from django.urls import path

from api_measurement.views import (
    api_measurement,
    SensorViews,
    UpdateSensorViews,
    AddMeasurementViews,
)
from first_project import settings

# from api_measurement.views import Api_demoViews
# from api_measurement.views import WeaponView

urlpatterns = [
    path("api_sensors/", api_measurement),
    path("sensors/", SensorViews.as_view()),
    # path('sensorstest/', SensorTestViews.as_view()),
    path("sensors/<pk>/", UpdateSensorViews.as_view()),
    path("measurements/", AddMeasurementViews.as_view()),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
