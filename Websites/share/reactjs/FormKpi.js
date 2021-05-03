import React from 'react'

import { Formik } from 'formik'
import FieldTextFormik from './FieldTextFormik'
import { FieldSelectFormik, SelectAsignType } from './FieldSelectFormik'
import * as Yup from 'yup'

const data_scheme = Yup.object().shape({
    name:Yup.string().required('No puede dejar este campo vacio'),
    avatar_id:Yup.string().nullable()
})

const FormKpi = (props) => {

    const {
        record,
        avatars,
        submit_handler,
        disabled_handler
    } = props

    const click_BtnSubmit = (values, actions) => {
        console.log(values)
        submit_handler(values)
        // actions.resetForm({})
        actions.setSubmitting(false)
    }

    const click_BtnDisable = () => {
        disabled_handler(values)
    }

    const build_Options = (data) => {
        let options = data.map((item, index, array) => {
            let new_item = {}
            new_item.value = item.id
            new_item.name = item.name
            new_item.label = `${item.name}: ${item.description}`
            return new_item
        })

        return options
    }

    return(
        <Formik
            enableReinitialize
            initialValues={{
                name: record ? record.name : "",
                avatar_id: record ? record.avatar_id : "",
            }}
            validationSchema={data_scheme}
            onSubmit={click_BtnSubmit}>
            { props => (
                <div className="form-user">
                    <form onSubmit={props.handleSubmit}>
                        <div className="form-row">
                            <div className="col-md-12">
                                <FieldTextFormik
                                    name="name"
                                    label={"Nombre"}
                                    optional={false}
                                    size={12}
                                />
                            </div>
                        </div>
                        <div className="form-row">
                            <div className="col-md-12">
                                <FieldSelectFormik
                                    name="avatar_id"
                                    asing_type={SelectAsignType.NAME}
                                    label={"Avatar ID"}
                                    optional={false}
                                    options={build_Options(avatars)}
                                />
                            </div>
                        </div>
                        <div className="form-row">
                            <div className="col-md-12 d-flex justify-content-between">
                                { disabled_handler &&
                                    <button type="button"
                                    onClick={click_BtnDisable}
                                    className="btn btn-danger">
                                        Deshabilitar
                                    </button>
                                }

                                <button
                                type="submit"
                                disabled={props.isSubmitting || !props.isValid}
                                className="btn btn-primary">
                                    Guardar
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            )}
        </Formik>
    )
}

export default FormKpi
