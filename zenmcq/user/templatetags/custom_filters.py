from django import template

register = template.Library()

@register.filter(name='add_attrs')
def add_attrs(field, attrs):
    """
    This filter adds custom attributes to a form field.
    Usage: {{ field|add_attrs:"class=form-control,placeholder=Enter your name" }}
    """
    attrs_dict = {}
    # Split the attributes string and create a dictionary
    for attr in attrs.split(','):
        key, value = attr.split('=')
        attrs_dict[key.strip()] = value.strip()
    # Use as_widget to add attributes to the field
    return field.as_widget(attrs=attrs_dict)
