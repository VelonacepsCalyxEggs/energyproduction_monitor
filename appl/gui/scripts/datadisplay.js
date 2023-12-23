document.addEventListener('DOMContentLoaded', function() {
    eel.dataAnalysis()().then(function (data) {
        requestedData = JSON.parse(data);
        console.log(requestedData);
        let effectivenessArray = requestedData.effectiveness;
        let effectivenessAnomalyArray = requestedData.effectivenessAnomaly;
        let effectivenessAnomalyLabelArray = requestedData.effectivenessAnomalyLabel;
        let dateformat = requestedData.effectiveness;
        console.log(dateformat.length)
        if (dateformat.length == 12) {
            labels = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
        }
        if (dateformat.length > 25) {
            labels = numbersArray = Array.from({ length: dateformat.length }, (_, index) => index + 1);
        }
        if (dateformat.length == 24) {
            labels = numbersArray = Array.from({ length: dateformat.length }, (_, index) => index + 1);
        }
        if (dateformat.length == 6) {
            labels = numbersArray = Array.from({ length: dateformat.length }, (_, index) => index + 1);
        }
        console.log(effectivenessArray); // This will log the "effectiveness" array to the console
        let dataTable = document.getElementById("dataTable");
        for(let i = 0; i < dateformat.length; i++) {
        let element = effectivenessArray[i];
        let newItem = document.createElement("li");
        if (element > 100) {
            newItem.textContent = `Effectiveness for ${labels[i]} is: ${element}%! [WARNING! OVERPRODUCTION DETECTED.]`;
            newItem.className = "text-danger fw-bold"
            newItem.id = "overProd"
        }
        if (element < 98) {
            newItem.textContent = `Effectiveness for ${labels[i]} is: ${element}%! [WARNING! NOT ENOUGH PRODUCTION DETECTED.]`;
            newItem.className = "text-warning fw-bold"
            newItem.id = "underProd"
        }
        if (element > 98 && element < 101 || element == 98) {
            newItem.textContent = `Effectiveness for ${labels[i]} is: ${element}%`; 
            newItem.className = "text-success fw-bold"
            newItem.id = "goodProd"
        }
        
        dataTable.appendChild(newItem)
        console.log(element)
        }
      });
  });