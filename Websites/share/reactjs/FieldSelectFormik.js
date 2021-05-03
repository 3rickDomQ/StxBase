import React, { useState } from 'react'
import { useField } from 'formik'
import { uid } from 'react-uid'


const SelectAsignType = {
    KEY: "key",
    NAME: "name"
}

const FieldSelectFormik = (props) => {

    const [field, meta] = useField(props.name)
    const [is_change, set_Change] = useState(false)

    const {
        asing_type,
        label,
        options,
        change_handler
    } = props

    const onchange_Handler = (e) => {
        field.onChange(e)
        set_Change(true)
        if (change_handler) {
            change_handler(e, field)
        }
    }

    const get_Value = () => {
        let value = ""

        if (is_change) {
            if (field.value) {
                value = field.value
            }

        } else {

            if (asing_type === SelectAsignType.KEY) {
                if (field.value) {
                    value = field.value
                }
            }

            if (asing_type === SelectAsignType.NAME) {
                if (field.value) {
                    var item = options.filter((item) => {
                        return item.name === field.value
                    })
                    if (typeof item === "object") {
                        if (item.length > 0) {
                            value = item[0].value
                        }
                    }
                }
            }
        }


        return value
    }

    return (
        <div className="form-group col-md-12">
            <label>
                {label}
            </label>
            <select
            name={field.name}
            value={get_Value()}
            onChange={onchange_Handler}
            className="form-control">
                <option value="" key={1}>
                </option>
                { options.map((item, index) => {
                    return <option key={uid(index)} value={item.value}>
                        {item.label}
                    </option>
                })}
            </select>
        </div>
    )
}

export { FieldSelectFormik, SelectAsignType }