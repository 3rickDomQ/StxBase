import Connector from '../../utils/Connector'
import { DomainEndpoints } from '../settings'

const endpoint = `${DomainEndpoints}api/avatars/`
const endpoint_detail = (_avatar_id) => {
    return `${DomainEndpoints}api/avatars/${_avatar_id}/`
}

const AvatarProductServer = {
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
    async get_All() {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint
                let conn = new Connector()
                let data = await conn.get(url)
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
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
    async update(_id, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_detail(_id)
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


export default AvatarProductServer
