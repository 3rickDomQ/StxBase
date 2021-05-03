import React, { Children } from 'react'
import { uid } from 'react-uid'


const TableRow = (props) => {

    const {
        data,
        actions,
        specify_fields
    } = props

    let controls = actions ? actions : []

    const get_Component = (_value, index) => {
        if (typeof _value === "boolean") {
            if (_value) {
                return <td key={uid(index)}>
                    <span className="badge badge-success">Si</span>
                </td>
            } else {
                return <td key={uid(index)}>
                    <span className="badge badge-danger">No</span>
                </td>
            }
        } else {
            if (typeof _value === "string") {
                if (_value.includes("://")) {
                    console.log(_value)
                    return <td key={uid(index)}>
                        <a className="btn btn-sm btn-primary light"
                        target="_blank"
                        href={_value}>
                            Descargar
                        </a>
                    </td>
                }
            }

            return <td key={uid(index)}>{_value}</td>
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
        <tr>
            {get_Columns()}
            <td key={4521} className="colum-actions">
            { controls.map((action, index) => {
                return action
            })}
            </td>
        </tr>
    )

}

export default TableRow