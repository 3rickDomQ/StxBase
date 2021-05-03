import Connector from '../../utils/Connector'
import { DomainEndpoints } from '../settings'

const endpoint_qst = (_id_poll, _id_kpi) => {
    return `${DomainEndpoints}api/polls/${_id_poll}/kpis/${_id_kpi}/questions/`
}

const endpoint_question_detail = (_question_id) => {
    return `${DomainEndpoints}api/questions/${_question_id}/`
}

const QuestionServer = {
    async create(_id_poll, _id_kpi, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let conn = new Connector()
                let data = await conn.post(
                    endpoint_qst(
                        _id_poll,
                        _id_kpi,

                    ),
                    _values
                )
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    },
    async update(_question_id, _values) {
        return new Promise(async (resolve, reject) => {
            try {
                let url = endpoint_question_detail(_question_id)
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

export default QuestionServer
