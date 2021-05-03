import MasterIn from '../../../share/vanillajs/MasterIn'

import './backoffice_pass_change_confirm.css'


/* ---------------- GLOBAL  ---------------- */
var page = null
var connector = null


/* ---------------- LOAD  ---------------- */
window.onload = function () {
    page = new Page()
}

/* ---------------- Page Object  ---------------- */

class Page {
    constructor () {
        this.master = new MasterIn("main-wrapper")
        this.init()
    }

    init() {
        this.master.spinner.stop()
    }
}
