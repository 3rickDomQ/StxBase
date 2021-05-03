import './public_campaign_retrieve.scss'

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

        this.ctx = document.getElementById('myChart').getContext('2d');
        this.campaing_id = document.getElementById('campaign_input').value

        this.init()
    }

    async init() {
        // var data = {
        //     labels: [
        //         "VIALIDAD",
        //         "RECOLECCIÓN DE BASURA",
        //         "INSEGURIDAD",
        //         "DESEMPLEO"
        //     ],
        //     datasets: [{
        //         label: "No. Votos",
        //         backgroundColor: "rgba(200,0,0,0.2)",
        //         data: [ 23, 21, 20, 24 ]
        //     }]
        // }
        // var myRadarChart = new Chart(this.ctx, {
        //     type: 'radar',
        //     data: data,
        //     options: {
        //         legend: {
        //             display: false
        //         },
        //         tooltips: {
        //             enabled: true,
        //             callbacks: {
        //                 label: function(tooltipItem, data) {
        //                     return data.datasets[tooltipItem.datasetIndex].label + ' : ' + data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
        //                 }
        //             }
        //         }
        //     }
        // });
        // myRadarChart.canvas.parentNode.style.height = '500px';
        // myRadarChart.canvas.parentNode.style.width = '500px';
        try {
            this.spinner.start()
            let server = new Connector()
            let response = await server.get(
                BackofficeApiUrls.campaing_kpi_data(
                    this.campaing_id
                )
            )
            console.log(response.data)

            var kpi_names = []
            var kpi_values = []

            response.data.forEach((kpi, index) => {
                console.log(kpi)
                kpi_names.push(Object.keys(kpi)[0])
                kpi_values.push(kpi[Object.keys(kpi)[0]])
            })

            if (kpi_values.length == 0) {
                document.getElementById('myChart').setAttribute("style", "display: none;");
            }
            var data = {
                labels: kpi_names,
                datasets: [{
                    label: "KPI",
                    backgroundColor: "rgba(200,0,0,0.2)",
                    data: kpi_values
                }]
            }
            console.log(data)
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
                                return 'Total' + ' : ' + data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
                            }
                        }
                    }
                }
            });
            // myRadarChart.canvas.parentNode.style.height = '500px';
            myRadarChart.canvas.parentNode.style.width = '500px';
            this.spinner.stop()

        } catch (error) {
            this.spinner.stop()
            alert(error)
        }
    }
}