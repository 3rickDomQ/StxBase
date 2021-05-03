import React from 'react'
import moment from 'moment';

const TimeLineItem = (props) => {

    moment.locale('es');

    // types:
    // -> primary
    // -> warning
    // -> dark
    // -> info
    // -> danger

    const {
        type,
        datetime,
        label,
        text,
    } = props

    const get_BadgeClassname = () => {
        return `timeline-badge ${type}`
    }

    const get_TextClassname = () => {
        return `text-${type}`
    }

    const get_FormatDate = () => {
        return moment(datetime).startOf('day').fromNow();
    }

    return (
        <li>
            <div className={get_BadgeClassname()}></div>
            <a className="timeline-panel text-muted" href="#">
                <span>{get_FormatDate()}</span>
                <h6 className="mb-0">
                    {label}
                    <strong className={get_TextClassname()}>{text}</strong>
                </h6>
            </a>
        </li>
    )
}

export default TimeLineItem