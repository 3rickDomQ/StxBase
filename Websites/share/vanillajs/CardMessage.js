const TypeMessage = {
    WARNING: 'warning',
    ERROR: 'error',
    SUCCESS: 'success',
    INFO: 'info'
}


class CardMessage {

    constructor(_type, _message) {
        this.container = null
        this.type = _type
        this.message = _message

        this.init()
    }

    init() {
        var element = document.createElement("div")
        element.id = "message-card"
        element.textContent = this.message

        switch (this.type) {
            case "warning":
                element.className = "alert alert-warning message-card"
                break

            case "error":
                element.className = "alert alert-danger message-card"
                break

            case "success":
                element.className = "alert alert-success message-card"
                break

            case "info":
                element.className = "alert alert-info message-card"
                break
        }

        this.container = element
    }

    render() {
        return this.container
    }
}


export {
    TypeMessage,
    CardMessage
}