import Connector from '../../utils/Connector'
import { DomainEndpoints } from '../settings'

const endpoint = `${DomainEndpoints}api/candidates/`

const CandidateServer = {
    async create(values) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint,
                    values
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
}


export default CandidateServer
