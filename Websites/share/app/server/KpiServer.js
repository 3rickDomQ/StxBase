import Connector from '../../utils/Connector'
import { DomainEndpoints } from '../settings'

const endpoint_kip = (_id_poll) => {
    return `${DomainEndpoints}api/polls/${_id_poll}/kpis/`
}

const endpoint_kpi_detail = (_kpi_id) => {
    return `${DomainEndpoints}api/kpi/${_kpi_id}/`
}

const KpiServer = {
    async create(_compaign_id, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_kip(_compaign_id),
                    _values
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async update(_kpi_id, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_kpi_detail(_kpi_id)
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
}

export default KpiServer
