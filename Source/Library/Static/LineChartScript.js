var config = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Current Dataset',
            backgroundColor: window.chartColors.red,
            borderColor: window.chartColors.red,
            data: [],
            fill: false,
        }]
    },
    options: {
        responsive: true,
        legend: {
            labels: {
                fontColor: '#FFFFFF'
            }
        },
        title: {
            display: true,
            text: '',
            fontColor: '#FFFFFF'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Time',
                    fontColor: '#FFFFFF'
                },
                gridLines: {
                    display: true,
                    color: "#FFFFFF"
                },
                ticks: {
                    fontColor: '#FFFFFF'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Value',
                    fontColor: '#FFFFFF'
                },
                gridLines: {
                    display: true,
                    color: "#FFFFFF"
                },
                ticks: {
                    beginAtZero:true,
                    fontColor: '#FFFFFF'
                }
            }]
        }
    }
};

var myChart;


function createChart() {
    var ctx = document.getElementById('canvas').getContext('2d');
    myChart = new Chart(ctx, config);
}

function addChartData(dataLabel, dataValue) {
    config.data.labels.push(dataLabel);
    matchedDataset = selectDataset("Current Dataset");
    matchedDataset.push(dataValue);
    myChart.update();
}

function selectDataset(dataset) {
    config.data.datasets.forEach(function(dataset) {
        match = dataset.data
    });
    return match
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
url='http://104.230.28.139:5002/networkserver/api';

async function getJson() {
    var runFlag = true
    // while (runFlag) {
        const Http = new XMLHttpRequest();
        Http.open("GET", url);
        Http.send();
        Http.onerror = function(e){
            runFlag = false
        };
        Http.onreadystatechange = function() {
            if(Http.readyState === 4 && Http.status === 200) {
                var newJson = (Http.responseText).replace(/\\/g,"")
                // console.log(newJson)
                newJson = JSON.parse(newJson)
                updateChartData(newJson)
                // console.log(typeof newJson)
            }
        }
        await sleep(1000);
    // }
}

function updateChartData(jsonData) {
    updateLabel = jsonData["Generic Information"]["Time"]
    updateValue = jsonData["Specific Information"]["Port"]
    addChartData(updateLabel, updateValue)
}

createChart()
getJson()