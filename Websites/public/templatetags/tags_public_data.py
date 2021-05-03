# Django's Libraries
from django import template
from Business.controllers import BackofficeWeb

register = template.Library()


@register.inclusion_tag(
    'tags/tag_public_data_votes.html',
    takes_context=False
)
def tag_public_data_votes(_campaign_id, _candidate_id):
    votes = BackofficeWeb.get_CandidateVotes(
        _campaign_id, _candidate_id
    )
    context = {
        'votes': votes
    }
    return context
