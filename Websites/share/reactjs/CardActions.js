import React from 'react'
import PropTypes from 'prop-types'


const CardActions = (props) => {

    const {
        title,
        btn_handler,
        btn_label
    } = props

    const click_Btn = (e) => {
        e.preventDefault()
        btn_handler()
    }

    return (
        <div className="card">
            <div className="card-header">
                <div className="card-head-row">
                    <div className="card-title">{title}</div>

                    { btn_handler &&
                        <button
                        onClick={click_Btn}
                        className="btn btn-xs btn-primary light">
                            <i className="fa fa-plus-circle"></i>
                            <span className="btn-label">
                                {btn_label}
                            </span>
                        </button>
                    }
                </div>
            </div>
            <div className="card-body">
                <div className="list-action">
                    {props.children}
                </div>
            </div>
        </div>
    )
}

CardActions.propTypes = {
    title: PropTypes.string.isRequired,
    btn_handler: PropTypes.func,
    btn_label: PropTypes.string
}

CardActions.defaultPros = {
    title: null,
    btn_handler: null,
    btn_label: null
}

export default CardActions