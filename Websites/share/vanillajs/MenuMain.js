
class MenuMain {

    constructor() {
        this.options = document.getElementsByClassName("nav-item")
        let page_option = this.get_PageOption()
        if (page_option) {
            this.set_Option(page_option)
        }
    }

    get_PageOption() {
        let module_element = document.getElementById("module")

        if (module_element) {
            return module_element.dataset.opt
        }

        return null
    }

    set_Option(_opt) {
        finish:
        for (var item of this.options) {
            if (item.dataset.type == "main-option") {
                let subitems = item.getElementsByTagName("li")
                for (var subitem of subitems) {
                    if (subitem.id === _opt) {
                        item.classList.add("active")
                        item.classList.add("submenu")

                        let item_container = item.getElementsByTagName("div")
                        item_container[0].classList.add("show")

                        subitem.classList.add("active")
                        break finish
                    }
                }
            } else {
                if (item.id === _opt) {
                    item.classList.add("active")
                    break finish
                }
            }
        }
    }
}

export default MenuMain