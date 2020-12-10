from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    :param value: string
    :param arg: string
    :return: string
    """
    return value.replace(arg, '')

# Despues de crear el metodo es necesario registrarlo
# Esta es una forma de registrarlos, la otra es con Decorators
# register.filter('cut', cut)  # El primer param es el modo en que llamaremos el filtro y el segundo es el filtro en si
