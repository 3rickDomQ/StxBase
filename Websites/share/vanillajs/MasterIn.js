import Spinner from './Spinner'
import MenuMain from './MenuMain'

class MasterIn {

    constructor (_spinner_id) {
        this.spinner = new Spinner(_spinner_id)
        this.MenuMain = new MenuMain()
        this.user_data = this.get_UserData('user-link')

        this.spinner.start()
    }

    get_UserData(_id) {
        let link = document.getElementById(_id)
        return link.dataset
    }
}

export default MasterIn