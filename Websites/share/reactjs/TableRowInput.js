import React, { Children } from 'react'
import { uid } from 'react-uid'


const TableRowInput = (props) => {

    const {
        data,
        actions,
        specify_fields
    } = props

    let controls = actions ? actions : []

    const get_Component = (_value, index) => {
        if (typeof _value === "boolean") {
            if (_value) {
                return <div key={uid(index)}>
                    <span className="badge badge-success">Si</span>
                </div>
            } else {
                return <div key={uid(index)}>
                    <span className="badge badge-danger">No</span>
                </div>
            }
        } else {
            return <div key={uid(index)}>{_value}</div>
        }
    }

    const get_Columns = () => {
        let columns = []

        if (specify_fields) {
            if (specify_fields.length > 0) {
                specify_fields.map((value, index) => {
                    // columns.push(<td key={uid(value)}>{get_Component(data[value])}</td>)
                    columns.push(get_Component(data[value], index))
                })
            } else {
                Object.keys(data).map((key, index) => {
                    // columns.push(<td key={uid(key)}>{get_Component(data[key])}</td>)
                    columns.push(get_Component(data[key], index))
                })
            }
        } else {
            Object.keys(data).map((key, index) => {
                // columns.push(<td key={uid(key)}>{get_Component(data[key])}</td>)
                columns.push(get_Component(data[key], index))
            })
        }
        return columns
    }

    return (
        <div className="table-row-input">
            <div className="columns">
                {get_Columns()}
            </div>
            <div key={4521} className="input">
            { controls.map((action, index) => {
                return action
            })}
            </div>
        </div>
    )

}

export default TableRowInput