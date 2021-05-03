import MasterIn from '../../../share/vanillajs/MasterIn'
import "./backoffice_home.scss"

/* ---------------- GLOBAL  ---------------- */
var page = null


/* ---------------- LOAD  ---------------- */
window.onload = function () {
    page = new Page()
}


/* ---------------- Page Object  ---------------- */
class Page extends MasterIn {
    constructor () {
        super("main-wrapper")

        this.enjoyhint_instance = new EnjoyHint({});
        this.init()
    }

    init () {
        this.spinner.stop()

        var enjoyhint_script_steps = [
            {
                'next .first-step': 'Click aquí para crear una Campaña',
                'nextButton': {className: "next-btn" , text: 'Siguiente'},
                "skipButton" : {className: "exit-btn", text: "Cerrar ayuda"},
            }, {
                'next .second-step': 'Click aquí para registrar un Usuario',
                'nextButton': {className: "next-btn" , text: 'Siguiente'},
                "skipButton" : {className: "exit-btn", text: "Cerrar ayuda"},
            }, {
                'next .menu-opt-1': 'Aquí podrás ver los Usuarios de la plataforma',
                'nextButton': {className: "next-btn" , text: 'Siguiente'},
                "skipButton" : {className: "exit-btn", text: "Cerrar ayuda"},
            }, {
                'next .menu-opt-2': 'Aquí las Campañas creadas',
                'nextButton': {className: "next-btn" , text: 'Siguiente'},
                "skipButton" : {className: "exit-btn", text: "Cerrar ayuda"},
            }, {
                'next .menu-opt-3': 'Y aquí las entrevistas de Avatar',
                "skipButton" : {className: "exit-btn", text: "Cerrar ayuda"},
            }
        ];

        this.enjoyhint_instance.set(enjoyhint_script_steps);

        if (this.user_data.firstLogin == "si") {
            this.enjoyhint_instance.run();
        }
    }
}
