import React from 'react'

import { Formik } from 'formik'
import FieldTextFormik from './FieldTextFormik'
import * as Yup from 'yup'


const data_scheme = Yup.object().shape({
    name:Yup.string().required('No puede dejar este campo vacio'),
    email: Yup.string().required('No puede dejar este campo vacio'),
})

const FormUser = (props) => {

    const {
        title,
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
                email: record ? record.email : "",
            }}
            validationSchema={data_scheme}
            onSubmit={click_BtnSubmit}>
            { props => (
                <div className="form-user">
                    <div className="form-user-header">
                        {title}
                    </div>
                    <form onSubmit={props.handleSubmit}>
                        <div className="form-row">
                            <FieldTextFormik
                                name="email"
                                label={"Correo"}
                                optional={false}
                                size={12}
                            />
                        </div>
                        <div className="form-row">
                            <FieldTextFormik
                                name="name"
                                label={"Nombre"}
                                optional={false}
                                size={12}
                            />
                        </div>
                        <div className="form-row">
                            <div className="col-md-12 text-right">
                                <button
                                type="submit"
                                disabled={props.isSubmitting || !props.isValid}
                                className="btn btn-primary">
                                    Crear
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            )}
        </Formik>
    )
}

export default FormUser
