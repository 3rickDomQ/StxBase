import React from 'react'
import { useField } from 'formik'


const FieldTextareaFormik = (props) => {

    const [field, meta] = useField(props)

    const {
        size,
        label,
        placeholder,
        optional,
        helptext,
        is_disabled,
        blur_handler,
        change_handler
    } = props

    let cls_name = size ? `form-group col-md-${size}` : "form-group"

    let show_errors = false
    // let field_class = "form-control"
    if (meta.touched && meta.error) {
        show_errors = true
        cls_name = `${cls_name} input-danger`
    }


    const custom_OnBlur_Handle = (e) => {
        field.onBlur(e)
        if (blur_handler) {
            blur_handler(e, field)
        }
    };

    const custom_OnChange_Handle = (e) => {
        field.onChange(e)
        if (change_handler) {
            change_handler(e, field)
        }
    }

    const get_LabelClassname = () => {
        if (meta.touched && meta.error) {
            return "field-label text-danger"
        } else {
            return "field-label"
        }
    }


    return (
        <div className={cls_name}>
            { label &&
                <label className={get_LabelClassname()}>
                    {label}
                    { optional == true &&
                        <span className="text-label-optional">
                            (opcional)
                        </span>
                    }
                </label>
            }
            <textarea
                disabled={is_disabled}
                className={"form-control"}
                placeholder={placeholder}
                id={field.name}
                rows={"5"}
                onBlur={custom_OnBlur_Handle}
                onChange={custom_OnChange_Handle}
                value={field.value ? field.value : ""}
            />
            { show_errors &&
                <div className="text-errors">
                    <ul className="text-danger">
                        {meta.error}
                    </ul>
                </div>
            }
            { helptext &&
                <div className="form-text">
                    {helptext}
                </div>
            }
        </div>
    )
}

export default FieldTextareaFormik
