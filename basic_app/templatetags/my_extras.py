from django import template

register = template.Library()

@register.filter(name='cortar')
def cortar(value,arg):
    """
    this  cuts out all values or "arg" from the string!
    """

    return value.replace(arg,'')

#register.filter('cut',cut)
