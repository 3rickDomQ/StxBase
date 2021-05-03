import React from 'react'
import DataField from './DataFile'

import { Formik } from 'formik'
import FieldTextFormik from './FieldTextFormik'
import FieldTextareaFormik from './FieldTextareaFormik'
import FieldFileFormik from './FieldFileFormik'
import * as Yup from 'yup'

import get_SrcImageGeneric from '../app/statics'


const data_scheme = Yup.object().shape({
    name:Yup.string().required('No puede dejar este campo vacio'),
    description: Yup.string().required('No puede dejar este campo vacio'),
    image: Yup.string().nullable().required('No puede dejar este campo vacio')
})


const CardCampaign = (props) => {

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
                <div className="basic-form">
                    <form onSubmit={props.handleSubmit}>
                        <div className="form-row">
                            <div className="col-md-8">
                                <FieldTextFormik
                                    name="name"
                                    label={"Nombre"}
                                    optional={false}
                                    size={12}
                                    is_disabled={true}
                                />
                                <FieldTextareaFormik
                                    name="description"
                                    label={"Descripción"}
                                    optional={false}
                                    size={12}
                                    is_disabled={true}
                                />
                            </div>
                            <div className="col-md-4">
                                <FieldFileFormik
                                    is_disabled={true}
                                    name="image"
                                    default_src={get_SrcImageGeneric('person.jpg')}
                                    label={"Imagen"}
                                    size={12}
                                    preview={true}
                                    change_handler={ (e) => {
                                        props.setFieldValue(
                                            "image",
                                            e.currentTarget.files[0]
                                        )
                                    }}
                                />
                            </div>
                        </div>
                    </form>
                </div>
            )}
        </Formik>
    )
}

export default CardCampaign

