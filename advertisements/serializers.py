from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    # def create  делает тоже самое что и def perform_create
    # в views оставить что-то одно
    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        user = self.context["request"].user

        # каким будет статус после сохранения
        new_status = data.get(
            "status",
            self.instance.status if self.instance else AdvertisementStatusChoices.OPEN
        )

        # каким статус был до изменения
        old_status = (
            self.instance.status
            if self.instance
            else None
        )

        # количество текущих открытых объявлений пользователя
        count = Advertisement.objects.filter(
            creator=user,
            status=AdvertisementStatusChoices.OPEN
        ).count()

        # увеличится ли количество OPEN-объявлений?
        will_add_open = (
                new_status == AdvertisementStatusChoices.OPEN
                and old_status != AdvertisementStatusChoices.OPEN
        )

        if will_add_open and count >= 10:
            raise serializers.ValidationError(
                "У пользователя не может быть больше 10 открытых объявлений."
            )

        return data
