
class Spinner {

    constructor (_container) {
        this.container = document.getElementById(
            _container
        )
    }

    create_HtmlElement () {
        let html_element = document.createElement("div");
        html_element.className = "spinner"
        html_element.setAttribute("id", "spinner")
        html_element.innerHTML = '<div class="spinner-figure"></div>'

        return html_element
    }

    start() {
        if (document.getElementById('spinner') == null) {
            this.container.appendChild(this.create_HtmlElement())
        }
    }

    stop() {
        if (document.getElementById('spinner') != null) {
            document.getElementById('spinner').remove()
        }
    }
}

export default Spinner