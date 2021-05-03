# Own's Libriries
from Utils.views import SimpleView
from Business.controllers import BackofficeWeb


class PublicLandingView(SimpleView):
    page_title = "Inicio"
    template_name = "pages/public_landing.html"
    get_method = "load_LandingPage"
    app_class = BackofficeWeb


class PublicCampaignsView(SimpleView):
    page_title = "Candidaturas"
    template_name = "pages/public_campaigns.html"
    app_class = BackofficeWeb
    get_method = "load_CampaignListPublicPage"


class PublicCampaignRetrieveView(SimpleView):
    page_title = "Candidatura"
    template_name = "pages/public_campaign_retrieve.html"
    app_class = BackofficeWeb
    get_method = "load_CampaignRetrievePage"
    post_method = "submit_CampaignRetrievePage"


class PublicCampaignCandidateView(SimpleView):
    page_title = "Candidatura - Candidatx"
    template_name = "pages/public_campaigns_candidate.html"
    app_class = BackofficeWeb
    get_method = "load_PublicCampaignCandidatePage"


class PublicCampaignCandidateVoteView(SimpleView):
    page_title = "Candidatura - Candidatx - Voto"
    template_name = "pages/public_campaigns_candidate_vote.html"
    app_class = BackofficeWeb
    get_method = "load_CampaignCandidateVotePage"
    post_method = "post_CampaignCandidateVotePage"


class PublicCandidatesView(SimpleView):
    page_title = "Candidatxs"
    template_name = "pages/public_candidates.html"
    app_class = BackofficeWeb
    get_method = "load_CandidateListPage"


class PublicCandidateRetrieveView(SimpleView):
    page_title = "Candidatx"
    template_name = "pages/public_candidate_retrieve.html"
    app_class = BackofficeWeb
    get_method = "load_CandidateRetrievePage"


class PublicEvaluatorsView(SimpleView):
    page_title = "Evaluadores"
    template_name = "pages/public_evaluators.html"


class PublicOrganizationsView(SimpleView):
    page_title = "Organizaciones"
    template_name = "pages/public_organizations.html"


class PublicIniciativaView(SimpleView):
    page_title = "Iniciativa"
    template_name = "pages/public_iniciativa.html"


class PublicProcesoView(SimpleView):
    page_title = "Proceso"
    template_name = "pages/public_proceso.html"


class PublicParticipaView(SimpleView):
    page_title = "Participa"
    template_name = "pages/public_participa.html"

class PublicPrivacidadView(SimpleView):
    page_title = "Aviso de Privacidad"
    template_name = "pages/public_privacidad.html"


class PublicPersonRetrieveView(SimpleView):
    page_title = "Perfil"
    template_name = "pages/public_person_retrieve.html"
    app_class = BackofficeWeb
    get_method = "load_PersonRetrievePage"
