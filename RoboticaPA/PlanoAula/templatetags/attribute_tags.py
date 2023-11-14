from django import template

register = template.Library()

@register.filter
def encontrar_usuario_lista(qs, usuario):
    lista = list(qs.values_list('usuario', flat=True))
    if usuario in lista:
        return True
    else:
        return False