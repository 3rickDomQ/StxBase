
const BackofficeUrls = {
    home: "/panel/home/",
    user_new: "/panel/users/new/",
    user_edit(_user_id) {
        return `/panel/users/${_user_id}/`
    },
    campaigns: "/panel/campaigns/",
    campaign_edit(_campaign_id) {
        return `/panel/campaigns/${_campaign_id}/`
    },
    campaign_review(_campaign_id) {
        return `/panel/campaigns/${_campaign_id}/review/`
    },
    campaign_files(_campaign_id) {
        return `/panel/campaigns/${_campaign_id}/files/`
    },
    poll_new(_campaign_id) {
        return `/panel/campaigns/${_campaign_id}/poll/new/`
    },
    poll_edit(_campaign_id, _poll_id) {
        return `/panel/campaigns/${_campaign_id}/poll/${_poll_id}/`
    },
    campaign_candidate(_campaign_id) {
        return `/panel/campaigns/${_campaign_id}/candidate/`
    },
    campaign_evaluador(_campaign_id) {
        return `/panel/campaigns/${_campaign_id}/evaluador/`
    },
    exam(_campaign_id, _exam_id) {
        return `/panel/campaigns/${_campaign_id}/exams/${_exam_id}/`
    },
    evaluar(_campaign_id, _exam_id) {
        return `/panel/campaigns/${_campaign_id}/evaluar/${_exam_id}/`
    },
    avatar(_exam_id, _kpi_id) {
        return `/panel/exam/${_exam_id}/kpi/${_kpi_id}/avatar/`
    }
}

export default BackofficeUrls