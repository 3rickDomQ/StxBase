import React from 'react'

import { Formik } from 'formik'
import FieldTextFormik from './FieldTextFormik'
import FieldFileFormik from './FieldFileFormik'
import * as Yup from 'yup'

const data_scheme = Yup.object().shape({
    description:Yup.string().required('No puede dejar este campo vacio'),
    file: Yup.string().nullable().required('No puede dejar este campo vacio')
})

const FormFile = (props) => {

    const {
        record,
        submit_handler,
    } = props

    const click_BtnSubmit = (values, actions) => {
        submit_handler(values)
        // actions.resetForm({})
        actions.setSubmitting(false)
    }

    return(
        <Formik
            enableReinitialize
            initialValues={{
                description: record ? record.description : "",
                file: record ? record.file : "",
            }}
            validationSchema={data_scheme}
            onSubmit={click_BtnSubmit}>
            { props => (
                <div className="form-user">
                    <form onSubmit={props.handleSubmit}>
                        <div className="form-row">
                            <div className="col-md-12">
                                <FieldTextFormik
                                    name="description"
                                    label={"Descripción"}
                                    optional={false}
                                    size={12}
                                    preview={false}
                                />
                                <FieldFileFormik
                                    name="file"
                                    label={"Archivo"}
                                    size={12}
                                    change_handler={ (e) => {
                                        props.setFieldValue(
                                            "file",
                                            e.currentTarget.files[0]
                                        )
                                    }}
                                />
                            </div>
                        </div>
                        <div className="form-row">
                            <div className="col-md-12 text-right">
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

export default FormFile
