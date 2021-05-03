# Django's Libraries
from django import template

register = template.Library()


@register.inclusion_tag(
    'tag_security_menu_main.html',
    takes_context=True
)
def tag_security_menu_main(context):
    menu = context['USER']['menu']

    context = {
        'menu': menu
    }
    return context
