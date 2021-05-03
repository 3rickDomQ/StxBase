import Connector from '../../utils/Connector'
import { DomainEndpoints } from '../settings'

const endpoint_detail = (_id_campaign, _id_poll) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/polls/${_id_poll}/`
}

const endpoint_activate = (_id_campaign, _id_poll) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/polls/${_id_poll}/activate/`
}

const endpoint_disable = (_id_campaign, _id_poll) => {
    return `${DomainEndpoints}api/campaigns/${_id_campaign}/polls/${_id_poll}/disable/`
}

const PollServer = {
    async get(_id_campaign, _id_poll) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_detail(_id_campaign, _id_poll)
                let conn = new Connector()
                let data = await conn.get(url)
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async update(_id_campaign, _id_poll, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_detail(_id_campaign, _id_poll)
                let conn = new Connector()
                let data = await conn.patch(
                    url,
                    _values
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async disable(_id_campaign, _id_poll) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_disable(_id_campaign, _id_poll),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async activate(_id_campaign, _id_poll) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_activate(_id_campaign, _id_poll),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
}

export default PollServer
