# Django's Libraries
from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag(
    'tag_control_filter_text.html',
    takes_context=False
)
def tag_control_filter_text(_form_field, _size="6"):
    context = {
        'form_field': _form_field,
        'size': _size
    }
    return context


@register.inclusion_tag(
    'tag_control_filter_select.html',
    takes_context=False
)
def tag_control_filter_select(_form_field, _size="6"):
    context = {
        'form_field': _form_field,
        'size': _size
    }
    return context


@register.inclusion_tag(
    'tag_control_field_text.html',
    takes_context=False
)
def tag_control_field_text(_form_field, _size="6", _hidden=False):

    visibility = "visible"
    if _hidden:
        visibility = "invisible"

    context = {
        'form_field': _form_field,
        'size': _size,
        'visibility': visibility
    }
    return context


@register.inclusion_tag(
    'tag_control_field_file.html',
    takes_context=False
)
def tag_control_field_file(_form_field, _size="6"):

    context = {
        'form_field': _form_field,
        'size': _size
    }
    return context


@register.inclusion_tag(
    'tag_control_field_check.html',
    takes_context=False
)
def tag_control_field_check(_form_field, _size="6"):

    context = {
        'form_field': _form_field,
        'size': _size
    }
    return context


@register.inclusion_tag(
    'tag_control_field_select.html',
    takes_context=False
)
def tag_control_field_select(_form_field, _size="6"):

    context = {
        'form_field': _form_field,
        'size': _size
    }
    return context


@register.inclusion_tag(
    'tag_control_field_date.html',
    takes_context=False
)
def tag_control_field_date(_form_field, _size="6"):

    context = {
        'form_field': _form_field,
        'size': _size
    }
    return context


@register.inclusion_tag(
    'tag_control_btn.html',
    takes_context=False
)
def tag_control_btn(
    _id,
    _label,
    _class,
    _is_submit=False,
    _is_disable=False
):
    btn_type = 'button'
    if _is_submit:
        btn_type = 'submit'

    context = {
        'btn_id': _id,
        'btn_label': _label,
        'btn_type': btn_type,
        'btn_class': _class,
        'btn_disable': _is_disable
    }

    return context


@register.inclusion_tag(
    'tag_control_link.html',
    takes_context=False
)
def tag_control_link(_id, _label, _url, _class='', _is_disable=False):
    url = reverse(_url)

    context = {
        'link_id': _id,
        'link_label': _label,
        'link_url': url,
        'link_class': _class,
        'link_disable': _is_disable
    }

    return context


@register.inclusion_tag(
    'tag_control_image.html',
    takes_context=False)
def tag_control_image(_field, _image):
    image_url = ""

    if _image:
        image_url = _image.url

    contexto = {
        'input_image': _field,
        'imagen': image_url,
    }
    return contexto
