import React from 'react'

const CardAction = (props) => {

    const {
        title,
        icon,
        btn_icon,
        btn_label,
        handler,
        disabled,
    } = props

    const click_Btn = (e) => {
        e.preventDefault()
        handler()
    }

    return (
        <div className="card">
            <div className="card-body text-center ai-icon text-primary">
                { icon &&
                    <div className="my-2 main-icon">
                        <i className={icon}></i>
                    </div>
                }
                <h4 className="my-2">{title}</h4>
                <button
                onClick={click_Btn}
                type="button"
                disabled={disabled}
                className="btn my-2 btn-primary btn-lg px-4">
                    { btn_icon &&
                        <i className={btn_icon}></i>
                    }
                    {btn_label}
                </button>
            </div>
        </div>
    )
}

export default CardAction