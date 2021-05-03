import React from 'react'

const BreadcrumbItem = (props) => {

    const {
        label,
        url,
        active,
    } = props

    let class_name = active ? 'breadcrumb-item active' : 'breadcrumb-item'

    return (
        <li className={class_name}>
            <a href={url}>{label}</a>
        </li>
    )
}

export default BreadcrumbItem