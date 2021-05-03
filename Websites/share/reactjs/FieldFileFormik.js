import React from 'react'
import { useField } from 'formik'

const FieldFileFormik = (props) => {
    const [field, meta] = useField(props)

    const {
        size,
        label,
        default_src,
        optional,
        is_disabled,
        change_handler,
        preview
    } = props

    const has_Errors = () => {
        if (meta.touched && meta.error) {
            return true
        } else {
            return false
        }
    }

    const get_ImageUrl = () => {
        if (field.value) {

            if (typeof field.value == "string") {
                return field.value

            } else {
                const objectURL = URL.createObjectURL(field.value)
                return objectURL
            }

        } else {
            return default_src
        }
    }

    return (
        <React.Fragment>
            { preview &&
                <img
                    src={get_ImageUrl()}
                    className="card-img-top img-fluid"
                />
            }

            { !is_disabled &&
            <div className="input-group mb-3">
                <div className="input-group-prepend">
                    <span className="input-group-text">Upload</span>
                </div>
                <div className="custom-file">
                        <input
                        id={field.name}
                        name={field.name}
                        type="file"
                        onChange={change_handler}
                        className="custom-file-input" />

                    { has_Errors() &&
                        <div className="text-errors">
                            <ul className="text-danger">
                                {meta.error}
                            </ul>
                        </div>
                    }

                    { label &&
                        <label className="custom-file-label">
                            {label}
                            { optional == true &&
                                <span className="text-label-optional">
                                    (opcional)
                                </span>
                            }
                        </label>
                    }
                </div>
            </div>
            }
        </React.Fragment>
    )
}

export default FieldFileFormik