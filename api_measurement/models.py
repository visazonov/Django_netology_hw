from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name="Название")
    description = models.CharField(max_length=50, verbose_name="Описание")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name="Температура")
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name="measurements"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="measurements/", null=True, blank=True)

    def __str__(self):
        return f"{self.sensor.name}: {self.temperature} °C"


# Для сериализаторов используйте ModelSerializer
