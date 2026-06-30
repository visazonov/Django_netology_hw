from django_filters import rest_framework as filters

from students.models import Course


class CourseFilter(filters.FilterSet):

    id = filters.ModelMultipleChoiceFilter(
        field_name="id",
        to_field_name="id",
        queryset=Course.objects.all(),
    )

    class Meta:
        model = Course
        fields = ("id", "name", )


# Тип именно ModelMultipleChoiceFilter означает:можно выбрать несколько объектов модели ?id=1&id=2&id=5
