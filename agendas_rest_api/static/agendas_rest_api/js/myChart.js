
var cores = [
    '#1232B', '#B5C334', '#FCCE10', '#E87C25', '#27727B', '#FE8463', '#9BCA63', '#FAD860', '#F3A43B', '#60C0DD', '#D7504B', '#C6E579', '#F4E001',
    '#F0805A', '#26C0C0',
    'rgba(255,201,47,0.8)', 'rgba(117,121,146,0.8)', 'rgba(255,202,149,0.8)', 'rgba(85,261,39,0.8)', 'rgba(255,621,50,0.8)', 'rgba(255,0,0,0.8)',
    'rgba(46,139,87,0.8)', 'rgba(0,0,205,0.8)', 'rgba(0,100,0,1)', 'rgba(0,255,0,1)', 'rgba(255,0,255,1)', 'rgba(255,69,0,1)',
    'rgba(255,255,0,1)', 'rgba((0,255,127,1)', 'rgba(30,144,255,1)', 'rgba(123,104,238,1)', 'rgba(47,79,79,1)', 'rgba(112,128,144,1)',
    'rgba(178,34,34,1)', 'rgba(147,112,219,1)', 'rgba(138,43,226,1)', 'rgba(148,0,211,1)', 'rgba(205,92,92,1)', 'rgba(25,25,112,1)',
    'rgba(0,0,128,1)', 'rgba(124,252,0,1)', 'rgba(85,107,47,1)', 'rgba((0,191,255,1)', 'rgba(70,130,180,1)', 'rgba(0,255,255,1)',
    'rgba(0,139,139,1)', 'rgba(102,205,170,1)', 'rgba(128,0,0,1)', 'rgba(128,128,0,1)', 'rgba(139,69,19,1)', 'rgba(210,105,30,1)',
    'rgba(152,251,152,1)', 'rgba(169,169,169,1)',
];


function chartBar(ctx, labels, data) {
    var chart = new Chart(ctx, {
        type: 'bar',

        data: {
            labels: labels,
            datasets: [
                {
                    data: data,
                    backgroundColor: cores,
                    borderColor: [],
                    borderWidth: 1,
                }
            ]
        },

        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                    },
                }],
                xAxes: [{
                    gridLines: {
                        offsetGridLines: true,
                    },
                    categoryPercentage: 0.7,    // define o espaço do eixo x sobre o qual as barras serão plotadas
                    barPercentage: 0.5,         // define a largura da barra    
                }]
            },
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    botton: 10
                }
            },
            legend:{
                display: true, 
            }
        }
    });
}


function chartPie(ctx, labels, data) {
    var chart = new Chart(ctx, {
        type: 'pie',

        data: {
            labels: labels,
            datasets: [
                {
                    data: data,
                    backgroundColor: cores,
                    borderColor: [],
                    borderWidth: 1,
                }
            ]
        },

        options: {
            scales: {
                yAxes: [{
                    display: false,
                }],
                xAxes: [{
                    display: false,
                }]
            },
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    botton: 10
                }
            }
        }
    });
}


function charthorizontalBar(ctx, labels, data) {
    var chart = new Chart(ctx, {
        type: 'horizontalBar',

        data: {
            labels: labels,
            datasets: [
                {
                    data: data,
                    backgroundColor: cores,
                    borderColor: [],
                    borderWidth: 1,
                }
            ]
        },

        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                    },
                }]
            },
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    botton: 10
                }
            }
        }
    });
}