import Spinner from './Spinner'

class PublicMaster {

    constructor (_spinner_id) {
        this.spinner = new Spinner(_spinner_id)

        this.spinner.start()
    }
}

export default PublicMaster