

class CardAccordion {

    constructor(_id, _icon, _title, _record_id, _data, _save_handler) {
        this.id = _id
        this.icon = _icon
        this.title = _title
        this.record_id = _record_id
        this.data = _data
        this.save_handler = _save_handler
    }

    collapse() {
        let header = document.getElementById(this.id)
        header.className = "card-header collapsed"
        header.setAttribute("aria-expanded", "false")

        let header_accordion = document.getElementById(`${this.id}-collapse`)
        header_accordion.className = "collapse"
    }

    uncollapse() {
        let header = document.getElementById(this.id)
        header.className = "card-header"
        header.setAttribute("aria-expanded", "true")

        let header_accordion = document.getElementById(`${this.id}-collapse`)
        header_accordion.className = "collapse show"
    }

    create_Header() {
        // Icon
        let icon_div = document.createElement("div")
        icon_div.className = this.icon

        let header_icon = document.createElement("div")
        header_icon.className = "span-icon"
        header_icon.appendChild(icon_div)

        // Title
        let header_row = document.createElement("div")
        header_row.className = "span-title"
        header_row.textContent = this.title

        // Span Mode
        let mode_row = document.createElement("div")
        mode_row.className = "span-mode"

        let header_div = document.createElement("div")
        header_div.setAttribute("id", this.id)
        header_div.className = "card-header"
        header_div.dataset.toggle = "collapse"
        header_div.dataset.target = `#${this.id}-collapse`
        header_div.setAttribute("aria-expanded", "true")
        header_div.setAttribute("aria-control", `${this.id}-collapse`)
        header_div.appendChild(header_icon)
        header_div.appendChild(header_row)
        header_div.appendChild(mode_row)

        return header_div
    }

    create_Row() {
        let row_div = document.createElement("div")
        row_div.className = "row"

        return row_div
    }

    create_Body() {
        let body_div = document.createElement("div")
        body_div.className = "card-body"

        if (this.data.length == 0) {
            let message_div = document.createElement("div")
            message_div.className = "content-message"
            message_div.textContent = "Sin información disponible"
            body_div.appendChild(message_div)

        } else {
            let row = this.create_Row()

            for (let item of this.data) {
                row.appendChild(item.create_Element())
            }

            body_div.appendChild(row)
        }

        return body_div
    }

    create_Footer() {
        let icon = document.createElement("i")
        icon.className = "fas fa-save"

        let span = document.createElement("span")
        span.className = "btn-label"
        span.appendChild(icon)

        let button = document.createElement("button")
        button.className = "btn btn-primary btn-border btn-round"
        button.setAttribute("type", "button")
        button.appendChild(span)
        button.textContent = "Guardar"
        button.addEventListener("click", this.save_handler)

        let footer_div = document.createElement("div")
        footer_div.className = "card-footer text-right"
        footer_div.appendChild(button)

        return footer_div
    }

    get_Values(_not_nulls) {
        let values = new Object()

        for (let item of this.data) {

            if (_not_nulls == true && item.get_Value() == "") {
                continue
            }

            if (item.disabled) {
                continue
            }

            values[item.id] =  item.get_Value()
        }

        return values
    }

    render() {
        let accordion_div = document.createElement("div")
        accordion_div.setAttribute("id", `${this.id}-collapse`)
        accordion_div.className = "collapse show"
        accordion_div.setAttribute("aria-labelledby", "headingOne")
        accordion_div.dataset.parent = "#accordion"
        accordion_div.appendChild(this.create_Body())
        accordion_div.appendChild(this.create_Footer())

        let card_div = document.createElement("div")
        card_div.className = "card"
        card_div.appendChild(this.create_Header())
        card_div.appendChild(accordion_div)
        return card_div
    }
}

export default CardAccordion

