# Django's Libraries
from django import template


register = template.Library()


@register.inclusion_tag(
    'tag_feedback_badge.html',
    takes_context=False
)
def tag_feedback_badge(_color, _text):
    context = {
        'color': _color,
        'text': _text,
    }
    return context


@register.inclusion_tag(
    'tag_feedback_messages.html',
    takes_context=False
)
def tag_feedback_messages(_messages):
    context = {
        'messages': _messages,
    }
    return context


@register.inclusion_tag(
    'tag_feedback_form_errors.html',
    takes_context=False
)
def tag_feedback_form_errors(_form):
    context = {
        'form': _form,
    }
    return context


@register.inclusion_tag(
    'tag_feedback_page_header.html',
    takes_context=False
)
def tag_feedback_page_header(
    _title,
    _subtitle="",
    _breadcrumb=None,
    _toolbar=None
):
    context = {
        'title': _title,
        'subtitle': _subtitle,
        'breadcrumb': _breadcrumb,
        'toolbar': _toolbar
    }
    return context
