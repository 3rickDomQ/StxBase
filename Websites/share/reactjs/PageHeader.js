import React from 'react'

const PageHeader = (props) => {

    const {
        title
    } = props

    return (
        <div className="row page-titles mx-0">
            <div className="col-sm-6 p-md-0">
                <div className="welcome-text">
                    <h4 className="brand-main-color">{title}</h4>
                </div>
            </div>
            <div className="col-sm-6 p-md-0 justify-content-sm-end mt-2 mt-sm-0 d-flex">
                <ol className="breadcrumb">
                {props.children}
                </ol>
            </div>
        </div>
    )
}

export default PageHeader