from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):

        # администратор может всё
        if request.user.is_staff:
            return True

        # обычный пользователь — только свои объявления
        return obj.creator == request.user


