module.exports = () => {

    return {
        resolve: {
            extensions: ['.js']
        },
        entry: {
            public_master: './public/templates/master/public_master.js',
            public_landing: './public/templates/pages/public_landing.js',
            public_candidates: './public/templates/pages/public_candidates.js',
            public_candidate_retrieve: './public/templates/pages/public_candidate_retrieve.js',
            public_person_retrieve: './public/templates/pages/public_person_retrieve.js',
            public_campaigns: './public/templates/pages/public_campaigns.js',
            public_campaign_retrieve: './public/templates/pages/public_campaign_retrieve.js',
            public_campaigns_candidate: './public/templates/pages/public_campaigns_candidate.js',
            public_campaigns_candidate_vote: './public/templates/pages/public_campaigns_candidate_vote.js',
            public_iniciativa: './public/templates/pages/public_iniciativa.js',
            public_proceso: './public/templates/pages/public_proceso.js',
            public_participa: './public/templates/pages/public_participa.js',
        }
    };
};
