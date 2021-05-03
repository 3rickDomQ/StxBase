import { embedDashboard } from 'amazon-quicksight-embedding-sdk';


class DashboardAws {

    constructor(_container, _url) {
        this.options = {
            url: _url,
            container: _container,
            scrolling: "yes",
            height: "AutoFit",
            loadingHeight: '700px',
            width: "100%",
            // loadingWidth: "1000px",
            footerPaddingEnabled: true
        };

        this.init()
    }

    init() {
        const dashboard = embedDashboard(this.options)
    }
}

export default DashboardAws
