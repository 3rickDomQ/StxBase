import React from 'react'

const CardAudit = (props) => {

    const {
        title
    } = props

    return (
        <div className="card">
            <div className="card-header border-0 pb-0">
                <h4 className="card-title">{title}</h4>
            </div>
            <div className="card-body">
                <div className="widget-timeline dz-scroll ps ps--active-y">
                    <ul className="timeline">
                        {props.children}
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default CardAudit



// <li>
// <div className="timeline-badge primary"></div>
// <a className="timeline-panel text-muted" href="#">
//     <span>10 minutes ago</span>
//     <h6 className="mb-0">Youtube, a video-sharing website, goes live <strong className="text-primary">$500</strong>.</h6>
// </a>
// </li>

// <li>
// <div className="timeline-badge info">
// </div>
// <a className="timeline-panel text-muted" href="#">
//     <span>20 minutes ago</span>
//     <h6 className="mb-0">New order placed <strong className="text-info">#XF-2356.</strong></h6>
//     <p className="mb-0">Quisque a consequat ante Sit amet magna at volutapt...</p>
// </a>
// </li>
// <li>
// <div className="timeline-badge danger">
// </div>
// <a className="timeline-panel text-muted" href="#">
//     <span>30 minutes ago</span>
//     <h6 className="mb-0">john just buy your product <strong className="text-warning">Sell $250</strong></h6>
// </a>
// </li>
// <li>
// <div className="timeline-badge success">
// </div>
// <a className="timeline-panel text-muted" href="#">
//     <span>15 minutes ago</span>
//     <h6 className="mb-0">StumbleUpon is acquired by eBay. </h6>
// </a>
// </li>
// <li>
// <div className="timeline-badge warning">
// </div>
// <a className="timeline-panel text-muted" href="#">
//     <span>20 minutes ago</span>
//     <h6 className="mb-0">Mashable, a news website and blog, goes live.</h6>
// </a>
// </li>
// <li>
// <div className="timeline-badge dark">
// </div>
// <a className="timeline-panel text-muted" href="#">
//     <span>20 minutes ago</span>
//     <h6 className="mb-0">Mashable, a news website and blog, goes live.</h6>
// </a>
// </li>