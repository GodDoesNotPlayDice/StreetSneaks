from django import template

register = template.Library()

@register.filter
def precio(value):
    formatted_number = "{:,.0f}".format(value).replace(",", ".")
    return formatted_number