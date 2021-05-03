import './public_campaigns_candidate.scss'

import PublicMaster from '../../../share/vanillajs/PublicMaster'
import BackofficeApiUrls from '../../../share/app/BackofficeApiUrls'
import Connector from '../../../share/utils/Connector'


/* ---------------- GLOBAL  ---------------- */
var page = null


/* ---------------- LOAD  ---------------- */
window.onload = function () {
    page = new Page()
}

/* ---------------- Page Object  ---------------- */

class Page extends PublicMaster {
    constructor() {
        super("main-wrapper")
        this.campaing_id = document.getElementById('campaign_input').value
        this.candidate_id = document.getElementById('candidate_input').value
        this.ctx = document.getElementById('myChart').getContext('2d');

        this.init()
    }

    async init() {
        try {
            let server = new Connector()
            let response = await server.get(
                BackofficeApiUrls.kpi_data(
                    this.campaing_id,
                    this.candidate_id
                )
            )
            data = response.data[0]

            var values = []
            data.kpi_name.forEach((kpi, index) => {
                let value = 0
                data.values.map((item, index) => {
                    if (item.kpi_name == kpi) {
                        value += item.score
                    }
                })
                values.push(value)
            })

            if (values.length == 0) {
                document.getElementById('myChart').setAttribute("style", "display: none;");
            }
            var data = {
                labels: data.kpi_name,
                datasets: [{
                    label: "KPI",
                    backgroundColor: "rgba(200,0,0,0.2)",
                    data: values
                }]
            }
            var myRadarChart = new Chart(this.ctx, {
                type: 'radar',
                data: data,
                options: {
                    legend: {
                        display: false
                    },
                    tooltips: {
                        enabled: true,
                        callbacks: {
                            label: function(tooltipItem, data) {
                                return data.datasets[tooltipItem.datasetIndex].label + ' : ' + data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
                            }
                        }
                    }
                }
            });
            myRadarChart.canvas.parentNode.style.height = '500px';
            myRadarChart.canvas.parentNode.style.width = '500px';
            this.spinner.stop()

        } catch (error) {
            this.spinner.stop()
            alert(error)
        }
    }
}