
const BackofficeApiUrls = {
    appraisal(_appraisal_id) {
        return `/api/appraisal/${_appraisal_id}/`
    },
    applicant(_applicant_id) {
        return `/api/applicant/${_applicant_id}/`
    },
    property(_property_id) {
        return `/api/property/${_property_id}/`
    },
    user_activation(_user_id) {
        return `/api/user/${_user_id}/activation/`
    },
    exam_detail(_exam_id) {
        return `/api/exams/${_exam_id}/`
    },
    kpi_data(_campaign_id, _candidate_id) {
        return `/api/campaigns/${_campaign_id}/candidate/${_candidate_id}/kpis/`
    },
    campaing_kpi_data(_campaign_id) {
        return `/api/campaigns/${_campaign_id}/kpis/`
    },
    avatar_response() {
        return '/api/avatar/response/'
    }
}

export default BackofficeApiUrls