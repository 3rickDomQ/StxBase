
class FieldDate {

    constructor(_id) {
        this.format = 'YYYY-MM-DD'
        this.container = $('#' + _id).datetimepicker({
            format: this.format
        })
    }

    get_Value() {
        return this.container.val()
    }
}

export default FieldDate