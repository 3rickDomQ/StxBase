from django import template


register = template.Library()


@register.simple_tag
def calc_PrecioHomologado(_market_item):
    price = _market_item.price if _market_item.price else 0
    surface_builded = _market_item.surface if _market_item.surface else 0
    calc = 0
    if surface_builded != 0:
        calc = price / surface_builded
        calc = round(calc, 2)

    return calc
