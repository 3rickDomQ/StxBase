import Connector from '../../utils/Connector'
import { DomainEndpoints } from '../settings'

const endpoint = `${DomainEndpoints}api/exams/`
const endpoint_detail = (_exam_id) => {
    return `${DomainEndpoints}api/exams/${_exam_id}/`
}
const endpoint_finalize = (_exam_id) => {
    return `${DomainEndpoints}api/exams/${_exam_id}/finalize/`
}
const endpoint_rate = (_exam_id) => {
    return `${DomainEndpoints}api/exams/${_exam_id}/rate/`
}
const endpoint_line = (_exam_id, _line_id) => {
    return `${DomainEndpoints}api/exams/${_exam_id}/line/${_line_id}/`
}

const ExamServer = {
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
    async create(_values) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint,
                    _values
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async finalize(_exam_id) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_finalize(_exam_id)
                let conn = new Connector()
                let data = await conn.post(url, {})
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async rate(_exam_id) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_rate(_exam_id)
                let conn = new Connector()
                let data = await conn.post(url, {})
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async update_line(_exam_id, _line_id, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_line(_exam_id, _line_id)
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

export default ExamServer