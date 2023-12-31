document.getElementById('date').oninput = function (){
    date = document.getElementById('date').value;
    console.log(date);
  }
  document.getElementById('buttonPeriod').onclick = function () {
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

      eel.dataRequestYearPeriodProduction(measure)().then(function (data) {
        requestedData2 = data;
        console.log(requestedData2);
      });
      eel.dataRequestYearPeriod(measure)().then(function (requestedData, Years) {
        console.log(requestedData)
        requestedData = JSON.parse(requestedData);
        requestedData2 = JSON.parse(requestedData2);
        console.log('Requesting data from SQL...')
        requestedData = requestedData.join('-').split('-');
        console.log(requestedData)
        dateSplit = date.split('-')
        labels = [2019,2020,2021,2022,2023]
          new Chart(document.getElementById("line-chart"), {
            type: 'line',
            data: {
              labels: [2019,2020,2021,2022,2023],
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
                text: `Все данные потребления`
              }
            }
          });     
        eel.saveDataForAnalysis(requestedData,requestedData2,labels) 
        console.log(requestedData)         
      }).catch(function (error) {
        console.error(error);
      });
    };