document.getElementById('date').oninput = function (){
  date = document.getElementById('date').value;
  console.log(date);
}
document.getElementById('buttonYear').onclick = function () {
  console.log(date)
  date = document.getElementById('date').value;
  console.log(typeof date)
  if (date == []) {
    date = '2023-01-01'
    }
    else {
      console.log('input recieved.')
    }
    eel.dataRequestYear(date)().then(function (requestedData) {
      console.log(requestedData)
      requestedData = JSON.parse(requestedData);
      console.log('Requesting data from SQL...')
      requestedData = requestedData.join('-').split('-');
      dateSplit = date.split('-')
        new Chart(document.getElementById("line-chart"), {
          type: 'line',
          data: {
            labels: ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
            datasets: [{ 
                data: requestedData,
                label: "Использование питания",
                borderColor: "#3e95cd",
                fill: false
              }
            ]
          },
          options: {
            title: {
              display: true,
              text: `Потребление за ${dateSplit[0]} год`
            }
          }
        });     
      console.log(requestedData)         
    }).catch(function (error) {
      console.error(error);
    });
  };

  document.getElementById('buttonMonth').onclick = function () {
    console.log(date)
    date = document.getElementById('date').value;
    console.log(typeof date)
    if (date == []) {
      date = '2023-01-01'
      }
      else {
        console.log('input recieved.')
      }
      eel.dataRequestMonth(date)().then(function (requestedData) {
        console.log(requestedData)
        requestedData = JSON.parse(requestedData);
        console.log('Requesting data from SQL...')
        requestedData = requestedData.join('-').split('-');
        console.log(requestedData)
        dateSplit = date.split('-')
        daysInMonth = Date(dateSplit[0], dateSplit[1], 0)
        console.log(daysInMonth)
        daysInMonthList = Array.from(Array(requestedData.length).keys()).map((num) => num + 1);

          new Chart(document.getElementById("line-chart"), {
            type: 'line',
            data: {
              labels: daysInMonthList,
              datasets: [{ 
                  data: requestedData,
                  label: "Использование питания",
                  borderColor: "#3e95cd",
                  fill: false
                }
              ]
            },
            options: {
              title: {
                display: true,
                text: `Потребление за ${dateSplit[1]} месяц`
              }
            }
          });     
        console.log(requestedData)         
      }).catch(function (error) {
        console.error(error);
      });
    };