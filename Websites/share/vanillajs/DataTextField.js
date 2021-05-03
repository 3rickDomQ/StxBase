import DataField from '../utils/DataField'


class DataTextField extends DataField {

    constructor(_id, _label, _value) {
        super(_id, _label, _value)
    }

    get_Value() {
        let element = document.getElementById(this.id)
        return element.value
    }

    create_Element(_size) {
        let input_div = document.createElement("input")
        input_div.className = "form-control input-square"
        input_div.setAttribute("id", this.id)
        input_div.setAttribute("type", "text")

        if (this.disabled) {
            input_div.setAttribute("disabled", "disabled")
        }

        if (this.value) {
            input_div.value = this.value
        }

        let form_group_div = document.createElement("div")
        form_group_div.className = "form-group"
        form_group_div.appendChild(this.create_Label())
        form_group_div.appendChild(input_div)

        let column_div = document.createElement("div")
        column_div.className = "col-md-6"
        column_div.appendChild(form_group_div)

        return column_div
    }
}

export default DataTextField
