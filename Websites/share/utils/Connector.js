var cookies = require('browser-cookies')


class Connector {

    contructor () {
        this.token = null
    }

    get_Cookie() {
        this.token = cookies.get('csrftoken')
        return this.token
    }

    get_Headers() {
        let headers = {
            'Content-Type': 'application/json',
            "X-CSRFToken": this.get_Cookie()
        }

        return headers
    }

    get(_url) {
        return new Promise( async (resolve, reject) => {
            try {
                let response = await fetch(_url, {
                    method: 'GET',
                    headers: this.get_Headers()
                })
                if (response.status >= 400 && response.status <= 451) {
                    let data_fail = await response.json()
                    reject(data_fail)

                } else if (response.status == 500) {
                    const {
                        status,
                        statusText
                    } = response

                    const value = `${status} -> ${statusText}`
                    reject(value)

                } else {
                    let data = await response.json()
                    resolve(data)
                }

            } catch (error) {
                reject(error)
            }
        })
    }

    delete(_url, _data) {
        return new Promise( async (resolve, reject) => {
            try {
                let response = await fetch(_url, {
                    method: 'DELETE',
                    headers: this.get_Headers()
                })
                if (response.status >= 400 && response.status <= 451) {
                    let data_fail = await response.json()
                    reject(data_fail)

                } else if (response.status == 500) {
                    const {
                        status,
                        statusText
                    } = response

                    const value = `${status} -> ${statusText}`
                    reject(value)

                } else if (response.status == 204) {

                    let data = "Registro eliminado con exito"
                    resolve(data)

                } else if (response.statusText) {
                    let data = "OK"
                    resolve(data)

                } else {
                    let data = await response.json()
                    resolve(data)
                }

            } catch (error) {
                reject(error)
            }
        })
    }

    post(_url, _data) {
        return new Promise( async (resolve, reject) => {
            try {
                let response = await fetch(_url, {
                    method: 'POST',
                    body: JSON.stringify(_data),
                    headers: this.get_Headers()
                })
                if (response.status >= 400 && response.status <= 451) {
                    let data_fail = await response.json()
                    reject(data_fail)

                } else if (response.status == 500) {
                    const {
                        status,
                        statusText
                    } = response

                    const value = `${status} -> ${statusText}`
                    reject(value)

                } else {
                    let data = await response.json()
                    resolve(data)
                }

            } catch (error) {
                reject(error)
            }
        })
    }

    patch(_url, _data) {
        return new Promise( async (resolve, reject) => {
            try {
                let response = await fetch(_url, {
                    method: 'PATCH',
                    body: JSON.stringify(_data),
                    headers: this.get_Headers()
                })

                if (response.status == 404) {
                    reject("No existe el recurso en el servidor")
                }

                if (response.status == 400 || response.status == 405) {
                    let data_fail = await response.json()
                    reject(data_fail.detail)

                }

                if (response.status == 500) {
                    const {
                        status,
                        statusText
                    } = response

                    const value = `${status} -> ${statusText}`
                    reject(value)

                }

                let data = await response.json()
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    }

    patch_WithFile(_url, _data) {
        return new Promise( async (resolve, reject) => {
            try {
                let response = await fetch(_url, {
                    method: 'PATCH',
                    body: _data,
                    headers: {
                        "X-CSRFToken": this.get_Cookie()
                    }
                })

                if (response.status == 404) {
                    reject("No existe el recurso en el servidor")
                }

                if (response.status == 400 || response.status == 405) {
                    let data_fail = await response.json()
                    reject(data_fail.detail)

                }

                if (response.status == 500) {
                    const {
                        status,
                        statusText
                    } = response

                    const value = `${status} -> ${statusText}`
                    reject(value)

                }

                let data = await response.json()
                resolve(data)

            } catch (error) {
                reject(error)
            }
        })
    }

    post_WithFile(_url, _data) {
        return new Promise( async (resolve, reject) => {
            try {
                let response = await fetch(_url, {
                    method: 'POST',
                    body: _data,
                    headers: {
                        "X-CSRFToken": this.get_Cookie()
                    }
                })
                if (response.status >= 400 && response.status <= 451) {
                    let data_fail = await response.json()
                    reject(data_fail)

                } else if (response.status == 500) {
                    const {
                        status,
                        statusText
                    } = response

                    const value = `${status} -> ${statusText}`
                    reject(value)

                } else {
                    let data = await response.json()
                    resolve(data)
                }

            } catch (error) {
                reject(error)
            }
        })
    }

}

export default Connector
