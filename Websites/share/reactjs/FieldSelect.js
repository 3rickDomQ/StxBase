import React from 'react'
import { useField } from 'formik'

const FieldSelect = (props) => {


    return (
        <div className="form-group">
            <label for="exampleFormControlSelect1">Example select</label>
            <select className="form-control" id="exampleFormControlSelect1">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            </select>
        </div>
    )
}

export default FieldSelect