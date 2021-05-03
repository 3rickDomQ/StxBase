# Django's Libraries
from django import template

register = template.Library()


@register.inclusion_tag(
    'tags/tag_card_candidate.html',
    takes_context=False
)
def tag_card_candidate(_campaign, _user):
    rol = ""
    if _user['position_name'] == 'ADMINISTRADOR' or _user['is_superuser']:
        rol = "administrador"
    else:
        for candidate in _campaign.candidates.all():
            if _user['pk'] == candidate.id:
                rol = "candidate"

        for colaborator in _campaign.collaborators.all():
            if _user['pk'] == colaborator.id:
                rol = "colaborador"

        for evaluator in _campaign.evaluators.all():
            if _user['pk'] == evaluator.id:
                rol = "evaluador"

        for organization in _campaign.organizations.all():
            if _user['pk'] == organization.id:
                rol = "administrador"

    context = {
        'campaign': _campaign,
        'rol': rol
    }
    return context
