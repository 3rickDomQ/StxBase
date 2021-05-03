import React from 'react'

import { Formik } from 'formik'
import FieldTextFormik from './FieldTextFormik'
import FieldTextareaFormik from './FieldTextareaFormik'
import FieldFileFormik from './FieldFileFormik'
import FieldNumberFormik from './FieldNumberFormik'
import * as Yup from 'yup'

import get_SrcImageGeneric from '../app/statics'



const data_scheme = Yup.object().shape({
    name:Yup.string().required('No puede dejar este campo vacio'),
    description: Yup.string().required('No puede dejar este campo vacio'),
    twitter_list: Yup.string().nullable(),
    avatar_percentage: Yup.string().nullable(),
    poll_percentage: Yup.string().nullable(),
    public_percentage: Yup.string().nullable(),
    image: Yup.string().nullable().required('No puede dejar este campo vacio')
})

const FormCampaign = (props) => {

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
                twitter_list: record ? record.twitter_list: "",
                avatar_percentage: record ? record.avatar_percentage: "",
                poll_percentage: record ? record.poll_percentage: "",
                public_percentage: record ? record.public_percentage: "",
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
                                />
                                <FieldTextareaFormik
                                    name="description"
                                    label={"Descripción"}
                                    optional={false}
                                    size={12}
                                />
                                <FieldTextFormik
                                    name="twitter_list"
                                    label={"Twitter Lista"}
                                    optional={false}
                                    size={12}
                                />
                                <FieldNumberFormik
                                    name="avatar_percentage"
                                    label="Avatar %"
                                    optional={false}
                                    size={12}
                                />
                                <FieldNumberFormik
                                    name="poll_percentage"
                                    label="Encuesta %"
                                    optional={false}
                                    size={12}
                                />
                                <FieldNumberFormik
                                    name="public_percentage"
                                    label="Votación %"
                                    optional={false}
                                    size={12}
                                />
                            </div>
                            <div className="col-md-4">
                                <FieldFileFormik
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
                        <div className="form-row">
                                <button
                                type="submit"
                                disabled={props.isSubmitting || !props.isValid}
                                className="btn btn-primary">
                                    Guardar
                                </button>
                        </div>
                    </form>
                </div>
            )}
        </Formik>
    )
}

export default FormCampaign
