import React from 'react'


const EmptyMessage = (props) => {

    const {
        text
    } = props

    return (
        <div className="empty-msg">
            {text}
        </div>
    )
}

export default EmptyMessage