import React from 'react'


const CardContent = (props) => {

    const {
        title,
        title_handler,
        subtitle,
        param,
        btn_handler,
        data_container,
        data_tut,
        btn_label
    } = props

    const click_Btn = (e) => {
        e.preventDefault()
        btn_handler(param)
    }

    const click_BtnTitle = (e) => {
        e.preventDefault()
        title_handler()
    }

    return (
        <div className="card" data_container={data_container}>
            <div className="card-header border-0 pb-0 d-sm-flex d-block">
                <div>
                    <h4 className="card-title">
                        <span className="card-title-text">{title}</span>
                        { title_handler &&
                            <button type="button"
                            className={"card-title-btn"}
                            onClick={click_BtnTitle}>
                                <i className="fa fa-pencil" aria-hidden="true"></i>
                            </button>
                        }
                    </h4>
                    <p className="mb-1">{subtitle}</p>
                </div>
                <div className="card-action">
                    { btn_handler &&
                        <button type="button"
                        btn_class="btn_class"
                        data_tut={data_tut}
                        className="btn btn-primary light"
                        onClick={click_Btn}>
                            <i className="fa fa-plus-circle"></i>
                            <span className="btn-label">
                                {btn_label}
                            </span>
                        </button>
                    }
                </div>
            </div>
            <div className="card-body">
                {props.children}
            </div>
        </div>
    )
}

export default CardContent