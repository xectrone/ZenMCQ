from django import template

register = template.Library()

@register.filter(name='add_attrs')
def add_attrs(field, css):
    return field.as_widget(attrs={'class': css})
