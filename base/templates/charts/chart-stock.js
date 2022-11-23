const config = {
    type: 'bar',
    data: {
        datasets:[{
            data:{{ data_stock|safe }},
            backgroundColor: ['rgba(255, 99, 132, 0.2)','rgba(255, 159, 64, 0.2)','rgba(255, 205, 86, 0.2)','rgba(75, 192, 192, 0.2)','rgba(54, 162, 235, 0.2)'],
            borderColor: ['rgb(255, 99, 132)','rgb(255, 159, 64)','rgb(255, 205, 86)','rgb(75, 192, 192)','rgb(54, 162, 235)'],
            label:'Productos',
            borderWidth:1
        }],
        labels: {{ labels_stock|safe }}
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],
        },
        responsive: true,
       
    },
  };
  var stockChart= new Chart($('#stock-chart-canvas'),config)
  