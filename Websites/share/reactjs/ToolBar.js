import React from 'react'

const ToolBar = (props) => {

    return  (
        <div className="toolbar">
            {props.children}
        </div>
    )
}

export default ToolBar