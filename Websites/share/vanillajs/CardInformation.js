

class CardInformation {

    constructor(_id, _title, _data) {
        this.id = _id
        this.title = _title
        this.data = _data
    }

    create_Title() {
        let title_div = document.createElement("div")
        title_div.className = "card-title"
        title_div.textContent = this.title

        return title_div
    }

    create_Header() {
        let header_row = document.createElement("div")
        header_row.className = "card-head-row"
        header_row.appendChild(this.create_Title())

        let header_div = document.createElement("div")
        header_div.className = "card-header"
        header_div.appendChild(header_row)

        return header_div
    }

    create_Item(_item) {

        let item_label_div = document.createElement("h6")
        item_label_div.className = "text-uppercase fw-bold mb-1"
        item_label_div.textContent = _item.label

        let item_data1_div = document.createElement("span")
        item_data1_div.className = "text-muted"
        item_data1_div.textContent = _item.data1

        let item_left_div = document.createElement("div")
        item_left_div.className = "flex-1 ml-3 pt-1"

        item_left_div.appendChild(item_label_div)
        item_left_div.appendChild(item_data1_div)

        let item_data2_div = document.createElement("small")
        item_data2_div.className = "text-muted"
        item_data2_div.textContent = _item.data2

        let item_right_div = document.createElement("div")
        item_right_div.className = "float-right pt-1"
        item_right_div.appendChild(item_data2_div)

        let item_div = document.createElement("div")
        item_div.className = "d-flex"
        item_div.appendChild(item_left_div)
        item_div.appendChild(item_right_div)

        return item_div
    }

    create_Separator() {
        let separator_div = document.createElement("div")
        separator_div.className = "separator-dashed"

        return separator_div
    }

    create_Body() {
        let body_div = document.createElement("div")
        body_div.className = "card-body"

        let qty_item = this.data.length

        let count = 1
        for (let item of this.data) {
            body_div.appendChild(this.create_Item(item))

            if (count != qty_item) {
                body_div.appendChild(this.create_Separator())
            }

            count += 1
        }

        return body_div
    }

    render() {
        let card_div = document.createElement("div")
        card_div.className = "card"
        card_div.appendChild(this.create_Header())
        card_div.appendChild(this.create_Body())

        return card_div
    }
}

export default CardInformation