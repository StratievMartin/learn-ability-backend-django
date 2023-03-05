# from rest_framework import permissions

# class IsAdminOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow admin users to edit an object.
#     """

#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user.is_staff
