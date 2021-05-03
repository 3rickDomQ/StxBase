# Django's Libraries
from django.urls import path
from django.urls import re_path

from .views import LoginView
from .views import LogoutView
from .views import HomeView
from .views import PasswordUpdateView
from .views import PasswordChangeRequestView
from .views import PasswordChangeConfirmView
from .views import PasswordChangeDoneView
from .views import AdminActivationConfirmView

from .views import CandidateActivationConfirmView
from .views import OrganizationActivationConfirmView
from .views import CollaboratorActivationConfirmView
from .views import EvaluatorActivationConfirmView

from .views import ActivationDoneView

from .views import UserListView
from .views import UserNewView
from .views import UserEditView
from .views import ProfileFilesView

from .views import CampaignListView
from .views import CampaignNewView
from .views import CampaignEditView
from .views import CampaignFilesView
from .views import CampaignReviewView
from .views import CampaignCandidateView
from .views import CampaignEvaluadorView

from .views import CampaignPollNewView
from .views import CampaignPollEditView
from .views import CampaignEvaluarView
from .views import CampaignExamView

from .views import CampaignAvatarView
from .views import AvatarProductView
from .views import TestingView

app_name = "backoffice"


SECURITY = [
    path(
        'login/',
        LoginView.as_view(),
        name="login"
    ),
    path(
        'password/update/',
        PasswordUpdateView.as_view(),
        name="password-update"
    ),
    path(
        'password/change/',
        PasswordChangeRequestView.as_view(),
        name="password-change-request"
    ),
    re_path(
        r'password/change/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordChangeConfirmView.as_view(),
        name='password-change-confirm'
    ),
    path(
        'password/change/done/',
        PasswordChangeDoneView.as_view(),
        name='password-change-done'
    ),
    re_path(
        r'candidate/activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<campaign_id>\w+)/$',
        CandidateActivationConfirmView.as_view(),
        name='candidate-activation-confirm'
    ),
    re_path(
        r'organization/activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<campaign_id>\w+)/$',
        OrganizationActivationConfirmView.as_view(),
        name='organization-activation-confirm'
    ),
    re_path(
        r'collaborator/activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<campaign_id>\w+)/$',
        CollaboratorActivationConfirmView.as_view(),
        name='collaborator-activation-confirm'
    ),
    re_path(
        r'evaluator/activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<campaign_id>\w+)/$',
        EvaluatorActivationConfirmView.as_view(),
        name='evaluator-activation-confirm'
    ),
    re_path(
        r'admin/activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        AdminActivationConfirmView.as_view(),
        name='admin-activation-confirm'
    ),
    path(
        'activation/done/',
        ActivationDoneView.as_view(),
        name='activation-done'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name="logout"
    ),
    path(
        'home/',
        HomeView.as_view(),
        name="home"
    )
]

CORE = [
    path(
        'users/',
        UserListView.as_view(),
        name="user-list"
    ),
    path(
        'users/new/',
        UserNewView.as_view(),
        name="user-new"
    ),
    path(
        'users/<int:param1>/',
        UserEditView.as_view(),
        name="user-edit"
    ),
    path(
        'users/<int:param1>/files/',
        ProfileFilesView.as_view(),
        name="user-files"
    ),
]

CATALOGUES = [

]

PROCESS = [
    path(
        'campaigns/',
        CampaignListView.as_view(),
        name="campaign-list"
    ),
    path(
        'campaigns/new/',
        CampaignNewView.as_view(),
        name="campaign-new"
    ),
    path(
        'campaigns/<int:param1>/',
        CampaignEditView.as_view(),
        name="campaign-edit"
    ),
    path(
        'campaigns/<int:param1>/files/',
        CampaignFilesView.as_view(),
        name="campaign-files"
    ),
    path(
        'campaigns/<int:param1>/review/',
        CampaignReviewView.as_view(),
        name="campaign-review"
    ),
    path(
        'campaigns/<int:param1>/candidate/',
        CampaignCandidateView.as_view(),
        name="campaign-candidate"
    ),
    path(
        'campaigns/<int:param1>/evaluador/',
        CampaignEvaluadorView.as_view(),
        name="campaign-evaluador"
    ),
    path(
        'campaigns/<int:param1>/poll/new/',
        CampaignPollNewView.as_view(),
        name="poll-new"
    ),
    path(
        'campaigns/<int:param1>/poll/<int:param2>/',
        CampaignPollEditView.as_view(),
        name="poll-edit"
    ),
    path(
        'exam/<int:param1>/kpi/<int:param2>/avatar/',
        CampaignAvatarView.as_view(),
        name="examen-kpi-avatar"
    ),
    path(
        'campaigns/<int:param1>/exams/<int:param2>/',
        CampaignExamView.as_view(),
        name="campaign-exam"
    ),
    path(
        'campaigns/<int:param1>/evaluar/<int:param2>/',
        CampaignEvaluarView.as_view(),
        name="campaign-evaluar"
    ),
    path(
        'avatars/',
        AvatarProductView.as_view(),
        name="avatar-product"
    ),
    path(
        'testing/<int:param1>/kpi/<int:param2>/avatar/',
        TestingView.as_view(),
        name="testing"
    ),
]

urlpatterns = SECURITY + \
    CORE + \
    CATALOGUES + \
    PROCESS
