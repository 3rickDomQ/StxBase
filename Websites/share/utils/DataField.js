import DataTextField from "../vanillajs/DataTextField"

class DataField {

    constructor(_id, _label, _value) {
        this.id = _id
        this.label = _label
        this.value = _value

        this.disabled = false
        this.placeholder = null
        this.url = null
        this.options = []
    }

    create_Label() {
        let label = document.createElement("label")
        label.setAttribute("for", this.id)
        label.textContent = this.label

        return label
    }
}

export default DataField
