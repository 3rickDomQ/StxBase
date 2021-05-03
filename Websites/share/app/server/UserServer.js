import Connector from '../../utils/Connector'
import { DomainEndpoints } from '../settings'

const endpoint = `${DomainEndpoints}api/users/`
const endpoint_detail = (_id) => {
    return `${DomainEndpoints}api/users/${_id}/`
}
const endpoint_files = (_id) => {
    return `${DomainEndpoints}api/users/${_id}/files/`
}
const endpoint_files_delete = (user_id, _file_id) => {
    return `${DomainEndpoints}api/users/${user_id}/files/${_file_id}/delete/`
}

const UserServer = {
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
    async get_Files(_id_user, _kpi_id) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.get(
                    endpoint_files(_id_user)
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async create_File(_id_user, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let form_data = new FormData();
                form_data.append('description', _values.description);
                if (typeof _values.file != "string") {
                    form_data.append('file', _values.file);
                }

                let conn = new Connector()
                let data = await conn.post_WithFile(
                    endpoint_files(_id_user),
                    form_data
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async delete_File(_id_user, _id_kpi) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.delete(
                    endpoint_files_delete(_id_user, _id_kpi),
                    {}
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    }
}


export default UserServer
