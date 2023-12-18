new Chart(document.getElementById("line-chart"), {
    type: 'line',
    data: {
      labels: ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
      datasets: [{ 
          data: [5,6,10,40,55,34,22,123,256,7],
          label: "Использование питания",
          borderColor: "#3e95cd",
          fill: false
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Потребление за год'
      }
    }
  });