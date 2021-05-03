import React from 'react'

const BreadcrumbIcon = (props) => {

    const {
        url,
        icon
    } = props

    return (
        <li className="breadcrumb-item">
            <a href={url}
            className="breadcrumb-icon">
                <i className={icon}></i>
            </a>
        </li>
    )
}

export default BreadcrumbIcon