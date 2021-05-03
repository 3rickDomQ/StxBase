import React from 'react'
import { uid } from 'react-uid'


const Table = (props) => {

    const {
        headers
    } = props

    return (
        <div className="table-responsive">
            <table className="table table-responsive-sm mb-0">
                { headers &&
                    <thead>
                        <tr>
                            { headers.map((item, index) => {
                                return <th key={uid(index)}><strong>{item}</strong></th>
                            })}
                        </tr>
                    </thead>
                }
                <tbody>
                    {props.children}
                </tbody>
            </table>
        </div>
    )
}

export default Table