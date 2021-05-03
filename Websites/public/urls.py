# Django's Libraries
from django.urls import path

# Own's Libraries
from .views import PublicLandingView

from .views import PublicCampaignsView
from .views import PublicCampaignRetrieveView

from .views import PublicCandidatesView
from .views import PublicCandidateRetrieveView

from .views import PublicPersonRetrieveView

from .views import PublicEvaluatorsView
from .views import PublicOrganizationsView

from .views import PublicCampaignCandidateView
from .views import PublicCampaignCandidateVoteView

from .views import PublicIniciativaView
from .views import PublicProcesoView
from .views import PublicParticipaView
from .views import PublicPrivacidadView

app_name = "public"

urlpatterns = [
    path(
        '',
        PublicLandingView.as_view(),
        name="landing"
    ),
    path(
        'campaigns/',
        PublicCampaignsView.as_view(),
        name="campaigns"
    ),
    path(
        'campaigns/<int:param1>/',
        PublicCampaignRetrieveView.as_view(),
        name="campaign-retrieve"
    ),
    path(
        'campaigns/<int:param1>/candidates/<int:param2>/',
        PublicCampaignCandidateView.as_view(),
        name="campaign-candidate"
    ),
    path(
        'campaigns/<int:param1>/candidates/<int:param2>/vote/',
        PublicCampaignCandidateVoteView.as_view(),
        name="campaign-candidate-vote"
    ),
    path(
        'candidates/',
        PublicCandidatesView.as_view(),
        name="candidates"
    ),
    path(
        'candidates/<int:param1>/',
        PublicCandidateRetrieveView.as_view(),
        name="candidate-retrieve"
    ),
    path(
        'person/<int:param1>/',
        PublicPersonRetrieveView.as_view(),
        name="person-retrieve"
    ),
    path(
        'evaluators/',
        PublicEvaluatorsView.as_view(),
        name="evaluators"
    ),
    path(
        'organizations/',
        PublicOrganizationsView.as_view(),
        name="organizations"
    ),
    path(
        'iniciativa/',
        PublicIniciativaView.as_view(),
        name="iniciativa"
    ),
    path(
        'proceso/',
        PublicProcesoView.as_view(),
        name="proceso"
    ),
    path(
        'participa/',
        PublicParticipaView.as_view(),
        name="participa"
    ),
    path(
        'privacidad/',
        PublicPrivacidadView.as_view(),
        name="privacidad"
    ),
]
