

from rest_framework import permissions

class Istructor_chacker(permissions.BasePermission):
    def has_permission(self, request, view):
        flag=False
        user = request.user
        if user:
            try:
                if user.account_type=='instructors' or user.account_type=='administrator_instructor':
                    flag = True
            except Exception as e:
                return False
        return flag