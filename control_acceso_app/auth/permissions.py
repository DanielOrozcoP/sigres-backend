from rest_framework.permissions import BasePermission



class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='admin').exists()
    
class IsDirectivo(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='directivo').exists()
    
class IsJ_Beca(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='j_beca').exists()
    
class IsEspecialista(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='especialista').exists()

from rest_framework.permissions import BasePermission

class IsJ_BecaOrIsEspecialista(BasePermission):
    def has_permission(self, request, view):
        is_j_beca = request.user and request.user.groups.filter(name='j_beca').exists()
        is_especialista = request.user and request.user.groups.filter(name='especialista').exists()
        return is_j_beca or is_especialista
