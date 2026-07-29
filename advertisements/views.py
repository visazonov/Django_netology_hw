from django.db.models import Q
# from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, Favorite, AdvertisementStatusChoices
from advertisements.permissions import IsOwnerOrAdmin
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all().order_by("id")
    queryset = (
        Advertisement.objects
        .all()
        .order_by("id")
        .select_related("creator")       # ForeignKey для OneToOneField
        # .prefetch_related("favorites")   # ForeignKey для ManyToManyField
    )
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AdvertisementFilter
    ordering_fields = [
        "created_at",
        "updated_at",
    ]
    throttle_classes = [AnonRateThrottle]
    # permission_classes = [IsOwner]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = (
            Advertisement.objects
            .all()
            .order_by("id")
            .select_related("creator")
            # .prefetch_related("favorites")
        )

        user = self.request.user

        # анонимные пользователи вообще не видят черновики
        if not user.is_authenticated:
            return queryset.exclude(
                status=AdvertisementStatusChoices.DRAFT
            )

        # автор видит свои черновики, остальные — нет
        return queryset.filter(
            Q(status__in=[
                AdvertisementStatusChoices.OPEN,
                AdvertisementStatusChoices.CLOSED
            ]) |
            Q(
                status=AdvertisementStatusChoices.DRAFT,
                creator=user
            )
        )


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        if self.action in ["favorite", "favorites"]:
            return [IsAuthenticated()]
        return super().get_permissions()


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    @action(detail=True, methods=["post", "delete"])
    def favorite(self, request, pk=None):

        advertisement = self.get_object()

        # нельзя добавить своё объявление в избранное
        if advertisement.creator == request.user:
            return Response(
                {"detail": "Нельзя добавить своё объявление в избранное."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Добавляем в БД в таблицу Favorite
        if request.method == "POST":
            favorite, created = Favorite.objects.get_or_create(
                user=request.user,
                advertisement=advertisement,
            )
            if created:
                print("Добавили в избранное")
                return Response(
                    {"detail": "Объявление добавлено в избранное."}
                )
            else:
                print("Уже было в избранном")

            return Response(
                {"detail": "Объявление уже находится в избранном."}
            )

        # удаление из избранного
        if request.method == "DELETE":
            Favorite.objects.filter(
                user=request.user,
                advertisement=advertisement,
            ).delete()

            return Response(
                {"detail": "Объявление удалено из избранного."}
            )


    @action(detail=False, methods=["get"])
    def favorites(self, request):
        queryset = self.get_queryset().filter(
            favorites__user=request.user
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
