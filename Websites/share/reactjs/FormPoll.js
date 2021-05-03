import React from 'react'

import { Formik } from 'formik'
import FieldTextFormik from './FieldTextFormik'
import FieldTextareaFormik from './FieldTextareaFormik'
import * as Yup from 'yup'

const data_scheme = Yup.object().shape({
    name:Yup.string().required('No puede dejar este campo vacio'),
    description: Yup.string().required('No puede dejar este campo vacio')
})

const FormPoll = (props) => {

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
                name: record ? record.name : "",
                description: record ? record.description : "",
                image: record ? record.image : "",
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
                                <FieldTextareaFormik
                                    name="description"
                                    label={"Descripción"}
                                    optional={false}
                                    size={12}
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

export default FormPoll
