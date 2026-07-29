from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    created_at = filters.DateFromToRangeFilter()
    is_favorite = filters.BooleanFilter(method="filter_is_favorite")

    class Meta:
        model = Advertisement
        fields = [
            "creator",
            "status",
        ]

    def filter_is_favorite(self, queryset, name, value):
        user = self.request.user

        # для анонимного пользователя ничего не возвращаем
        if not user.is_authenticated:
            return queryset.none()

        if value:
            return queryset.filter(
                favorites__user=user
            ).distinct()

        return queryset
