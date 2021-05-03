class CardPhoto {

    constructor(_input_id, _view_id) {
        this.input = document.getElementById(_input_id)
        this.view = document.getElementById(_view_id)

        this.init()
    }

    init() {
        this.input.addEventListener(
            "change",
            this.render.bind(this)
        )
    }

    render(e) {
        if (e.target.files && e.target.files[0]) {

            var reader = new FileReader()

            let self = this
            reader.onload = function (e) {
                self.view.setAttribute('src', e.target.result)
            }

            reader.readAsDataURL(e.target.files[0])
        }
    }
}

export default CardPhoto
