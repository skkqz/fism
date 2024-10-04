from rest_framework.permissions import BasePermission


class IsAgentOrAdminPermission(BasePermission):
    """
    Кастомный пермишен, который проверяет, находится ли пользователь в группе "Agent"
    или является суперпользователем.
    """

    def has_permission(self, request, view):

        test = request.user.groups.filter(name='agent')

        if test.exists() or request.user.is_superuser:
            return True
        return False


class IsUnderwriterOrAdminPermission(BasePermission):
    """
    Кастомный пермишен, который проверяет, находится ли пользователь в группе "Agent"
    или является суперпользователем.
    """

    def has_permission(self, request, view):

        test = request.user.groups.filter(name='underwriter')

        if test.exists() or request.user.is_superuser:
            return True
        return False