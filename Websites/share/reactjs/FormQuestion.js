import React from 'react'

import { Formik } from 'formik'
import FieldTextFormik from './FieldTextFormik'
import FieldNumberFormik from './FieldNumberFormik'
import * as Yup from 'yup'

const data_scheme = Yup.object().shape({
    text:Yup.string().required('No puede dejar este campo vacio'),
    weight:Yup.string().required('No puede dejar este campo vacio')
})

const FormQuestion = (props) => {

    const {
        record,
        submit_handler
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
                text: record ? record.text : "",
                weight: record ? record.weight : ""
            }}
            validationSchema={data_scheme}
            onSubmit={click_BtnSubmit}>
            { props => (
                <div className="form-user">
                    <form onSubmit={props.handleSubmit}>
                        <div className="form-row">
                            <div className="col-md-12">
                                <FieldTextFormik
                                    name="text"
                                    label={"Texto de la pregunta"}
                                    optional={false}
                                    size={12}
                                />
                            </div>
                            <div className="col-md-12">
                                <FieldNumberFormik
                                    name="weight"
                                    label={"Valor"}
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

export default FormQuestion
