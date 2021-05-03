import Connector from '../../utils/Connector'
import { DomainEndpoints } from '../settings'

const endpoint_detail = (_id) => {
    return `${DomainEndpoints}api/campaigns/${_id}/`
}
const endpoint_kpi = (_id) => {
    return `${DomainEndpoints}api/campaigns/${_id}/kpi/`
}
const endpoint_files = (_id) => {
    return `${DomainEndpoints}api/campaigns/${_id}/files/`
}
const endpoint_files_delete = (_campaign_id, _file_id) => {
    return `${DomainEndpoints}api/campaigns/${_campaign_id}/files/${_file_id}/delete/`
}
const endpoint_kpi_detail = (_campaign_id, _kpi_id) => {
    return `${DomainEndpoints}api/campaigns/${_campaign_id}/kpi/${_kpi_id}/`
}
const endpoint_kpi_disable = (_campaign_id, _kpi_id) => {
    return `${DomainEndpoints}api/campaigns/${_campaign_id}/kpi/${_kpi_id}/disable/`
}
const endpoint_activate = (_id) => {
    return `${DomainEndpoints}api/campaigns/${_id}/activate/`
}
const endpoint_disable = (_id) => {
    return `${DomainEndpoints}api/campaigns/${_id}/disable/`
}
const endpoint_add_candidate = (_id_campaign, _id_user) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/candidate/${_id_user}/add/`
}
const endpoint_delete_candidate = (_id_campaign, _id_user) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/candidate/${_id_user}/delete/`
}
const endpoint_add_organization = (_id_campaign, _id_user) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/organization/${_id_user}/add/`
}
const endpoint_delete_organization = (_id_campaign, _id_user) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/organization/${_id_user}/delete/`
}
const endpoint_add_colaborator = (_id_campaign, _id_user) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/colaborator/${_id_user}/add/`
}
const endpoint_delete_colaborator = (_id_campaign, _id_user) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/colaborator/${_id_user}/delete/`
}
const endpoint_add_evaluator = (_id_campaign, _id_user) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/evaluator/${_id_user}/add/`
}
const endpoint_delete_evaluator = (_id_campaign, _id_user) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/evaluator/${_id_user}/delete/`
}
const endpoint_compaings_polls = (_id_campaign) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/polls/`
}

const CampaignServer = {

    async get(id) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_detail(id)
                let conn = new Connector()
                let data = await conn.get(url)
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async activate(_id_campaign) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_activate(_id_campaign),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async disable(_id_campaign) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_disable(_id_campaign),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async add_Candidato(_id_campaign, _id_user) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_add_candidate(_id_campaign, _id_user),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async add_Organization(_id_campaign, _id_user) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_add_organization(_id_campaign, _id_user),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async add_Colaborator(_id_campaign, _id_user) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_add_colaborator(_id_campaign, _id_user),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async add_Evaluator(_id_campaign, _id_user) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_add_evaluator(_id_campaign, _id_user),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async create_Poll(_id_campaign, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_compaings_polls(_id_campaign),
                    _values
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async update(_id_campaign, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let form_data = new FormData();

                console.log(_values)
                form_data.append('name', _values.name);
                form_data.append('description', _values.description);
                form_data.append('twitter_list', _values.twitter_list);
                form_data.append('avatar_percentage', _values.avatar_percentage ? _values.avatar_percentage : 0);
                form_data.append('poll_percentage', _values.poll_percentage ? _values.poll_percentage : 0);
                form_data.append('public_percentage', _values.public_percentage ? _values.public_percentage : 0);

                if (typeof _values.image != "string") {
                    form_data.append('image', _values.image);
                }

                let url = endpoint_detail(_id_campaign)
                let conn = new Connector()
                let data = await conn.patch_WithFile(
                    url,
                    form_data
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async add_Kpi(_id_campaign, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let values = {
                    campaign: _id_campaign,
                    name: _values['name']
                }

                let data = await conn.post(
                    endpoint_kpi(_id_campaign),
                    values
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async get_Kpi(_id_campaign, _kpi_id) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.get(
                    endpoint_kpi_detail(_id_campaign, _id_kpi)
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async edit_Kpi(_id_campaign, _id_kpi, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                console.log(_values)
                let values = {
                    campaign: _id_campaign,
                    name: _values['name']
                }
                let data = await conn.patch(
                    endpoint_kpi_detail(_id_campaign, _id_kpi),
                    values
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async delete_Kpi(_id_campaign, _id_kpi) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.delete(
                    endpoint_kpi_detail(_id_campaign, _id_kpi),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async delete_Candidate(_id_campaign, _id_user) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.delete(
                    endpoint_delete_candidate(_id_campaign, _id_user),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async delete_Organization(_id_campaign, _id_user) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.delete(
                    endpoint_delete_organization(_id_campaign, _id_user),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async delete_Collaborator(_id_campaign, _id_user) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.delete(
                    endpoint_delete_colaborator(_id_campaign, _id_user),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async delete_Evaluator(_id_campaign, _id_user) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.delete(
                    endpoint_delete_evaluator(_id_campaign, _id_user),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async get_Files(_id_campaign, _kpi_id) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.get(
                    endpoint_files(_id_campaign)
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async create_File(_id_campaign, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let form_data = new FormData();
                form_data.append('description', _values.description);
                if (typeof _values.file != "string") {
                    form_data.append('file', _values.file);
                }

                let conn = new Connector()
                let data = await conn.post_WithFile(
                    endpoint_files(_id_campaign),
                    form_data
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async delete_File(_id_campaign, _id_kpi) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.delete(
                    endpoint_files_delete(_id_campaign, _id_kpi),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
}


export default CampaignServer
