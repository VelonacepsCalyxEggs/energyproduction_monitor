document.getElementById('date').oninput = function (){
    date = document.getElementById('date').value;
    console.log(date);
  }
  document.getElementById('buttonYear').onclick = function () {
    var iframes = document.querySelectorAll('iframe');
  
    iframes.forEach((iframe) => {
      iframe.remove();
    })
    var canvases = document.querySelectorAll('canvas');
  
    canvases.forEach((canvas) => {
      canvas.remove();
    })
    var parentElement = document.getElementById("line-chart-container");
    var htmlContent = '<canvas id="line-chart" width="800" height="400"></canvas>';
    parentElement.insertAdjacentHTML("beforeend", htmlContent);
    console.log(date)
    date = document.getElementById('date').value;
    console.log(typeof date)
    if (date == []) {
      date = '2023-01-01'
      }
      else {
        console.log('input recieved.')
      }
      measure = document.getElementById('measure').value;
      console.log(measure)
      let requestedData2;
  
      eel.dataRequestYearProduction(date, measure)().then(function (data) {
        requestedData2 = data;
        console.log(requestedData2);
      });
      eel.dataRequestYear(date,measure)().then(function (requestedData) {
        console.log(requestedData)
        requestedData = JSON.parse(requestedData);
        requestedData2 = JSON.parse(requestedData2);
        console.log('Requesting data from SQL...')
        requestedData = requestedData.join('-').split('-');
        requestedData2 = requestedData2.join('-').split('-');
        dateSplit = date.split('-')
        labels = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
          new Chart(document.getElementById("line-chart"), {
            type: 'line',
            data: {
              labels: ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
              datasets: [{ 
                  data: requestedData,
                  label: "Использование питания",
                  borderColor: "#3e95cd",
                  fill: false
                },
                {
                  data: requestedData2,
                  label: "Производство питания",
                  borderColor: "#FF0000",
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
          eel.saveDataForAnalysis(requestedData,requestedData2,labels) 
        console.log(requestedData)         
      }).catch(function (error) {
        console.error(error);
      });
    }