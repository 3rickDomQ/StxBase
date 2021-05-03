module.exports = () => {

    return {
        resolve: {
            extensions: ['.js']
        },
        entry: {
            backoffice_master_in: './backoffice/templates/master/backoffice_master_in.js',
            backoffice_login: './backoffice/templates/pages/backoffice_login.js',
            backoffice_home: './backoffice/templates/pages/backoffice_home.js',
            backoffice_pass_update: './backoffice/templates/pages/backoffice_pass_update.js',
            backoffice_pass_change_confirm: './backoffice/templates/pages/backoffice_pass_change_confirm.js',
            backoffice_activation_done: './backoffice/templates/pages/backoffice_activation_done.js',
            backoffice_user_list: './backoffice/templates/pages/backoffice_user_list.js',
            backoffice_user_new: './backoffice/templates/pages/backoffice_user_new.js',
            backoffice_user_edit: './backoffice/templates/pages/backoffice_user_edit.js',
            backoffice_user_files: './backoffice/templates/pages/backoffice_user_files.js',
            backoffice_campaign_list: './backoffice/templates/pages/backoffice_campaign_list.js',
            backoffice_campaign_new: './backoffice/templates/pages/backoffice_campaign_new.js',
            backoffice_campaign_edit: './backoffice/templates/pages/backoffice_campaign_edit.js',
            backoffice_campaign_files: './backoffice/templates/pages/backoffice_campaign_files.js',
            backoffice_campaign_review: './backoffice/templates/pages/backoffice_campaign_review.js',
            backoffice_campaign_candidate: './backoffice/templates/pages/backoffice_campaign_candidate.js',
            backoffice_campaign_evaluator: './backoffice/templates/pages/backoffice_campaign_evaluator.js',
            backoffice_campaign_exam: './backoffice/templates/pages/backoffice_campaign_exam.js',
            backoffice_campaign_evaluar: './backoffice/templates/pages/backoffice_campaign_evaluar.js',
            backoffice_poll_new: './backoffice/templates/pages/backoffice_poll_new.js',
            backoffice_poll_edit: './backoffice/templates/pages/backoffice_poll_edit.js',
            backoffice_avatar: './backoffice/templates/pages/backoffice_avatar.js',
            backoffice_avatar_admin: './backoffice/templates/pages/backoffice_avatar_admin.js',
            backoffice_testing: './backoffice/templates/pages/backoffice_testing.js'
        }
    };
};
