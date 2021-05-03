
const DomainEndpoints = `${window.location.origin}/`

const DomainStatics = () => {
    if (PRODUCTION) {
        // return `${window.location.origin}/`
        return 'https://xxxxx.s3.amazonaws.com/'
    } else {
        return 'http://127.0.0.1:9001/'
    }
}

export {
    DomainEndpoints,
    DomainStatics
}