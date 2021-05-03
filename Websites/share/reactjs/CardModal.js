import React from 'react'

const CardModal = (props) => {

    const {
        title,
        acept_handler,
        cancel_handler,
        close_handler
    } = props

    const click_BtnAcept = (e) => {
        e.preventDefault()
        acept_handler()
    }

    const click_BtnCancel = (e) => {
        e.preventDefault()
        cancel_handler()
    }

    const click_BtnClose = (e) => {
        e.preventDefault()
        close_handler()
    }

    return (
        <div className="modal fade bd-example-modal-lg show" tabIndex="-1" role="dialog" arial-modal="true">
            <div className="modal-dialog modal-lg">
                <div className="modal-content">
                <div className="modal-header">
                    <h5 className="modal-title">{title}</h5>
                    <button
                    onClick={click_BtnClose}
                    type="button"
                    className="close"
                    data-dismiss="modal">
                        <span>×</span>
                    </button>
                </div>
                <div className="modal-body">
                    {props.children}
                </div>
                { acept_handler || cancel_handler &&
                    <div className="modal-footer">
                        { acept_handler &&
                            <button type="button"
                            onClick={click_BtnAcept}
                            className="btn btn-primary">
                                Aceptar
                            </button>
                        }
                        { cancel_handler &&
                            <button type="button"
                            onClick={click_BtnCancel}
                            className="btn btn-secondary">
                                Cancelar
                            </button>
                        }
                    </div>
                }
                </div>
            </div>
        </div>
    )
}


export default CardModal




