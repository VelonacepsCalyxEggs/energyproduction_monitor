document.addEventListener('DOMContentLoaded', function() {
    eel.dataAnalysis()().then(function (data) {
        requestedData = JSON.parse(data);
        console.log(requestedData);
        let effectivenessArray = requestedData.effectiveness;
        let effectivenessAnomalyArray = requestedData.effectivenessAnomaly;
        let effectivenessAnomalyLabelArray = requestedData.effectivenessAnomalyLabel;
        let dateformat = requestedData.effectiveness;
        console.log(dateformat.length)
        let dataTable = document.getElementById("dataTable");
        let dataList = document.getElementById("dataList");
        let dataDateList = document.getElementById("dataDateList");
        if (dateformat.length == 12) {
            labels = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
            for(let i = 0; i < dateformat.length; i++) {
                dataDateList.innerHTML = dataDateList.innerHTML + `<th class='fs-6'>${labels[i]} month</th>`
                //let dataListElement = document.getElementById(`${i}hr`);
            }
            for(let i = 0; i < dateformat.length; i++) { 
                let element = effectivenessArray[i];
                if (element > 100) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-danger fw-bold">${element}%</td>`
                }
                if (element < 98) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-warning fw-bold">${element}%</td>`
                }
                if (element > 98 && element < 101 || element == 98) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-success fw-bold">${element}%</td>`
                }
            }
        }
        if (dateformat.length > 25) {
            i2 = 1
            labels = numbersArray = Array.from({ length: dateformat.length }, (_, index) => index + 1);
            for(let i = 0; i < dateformat.length; i++) {
                dataDateList.innerHTML = dataDateList.innerHTML + `<th class='fs-6'>${i2} day</th>`
                //let dataListElement = document.getElementById(`${i}hr`);
                i2 = i2 + 1
            }
            for(let i = 0; i < dateformat.length; i++) { 
                let element = effectivenessArray[i];
                if (element > 100) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-danger fw-bold">${element}%</td>`
                }
                if (element < 98) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-warning fw-bold">${element}%</td>`
                }
                if (element > 98 && element < 101 || element == 98) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-success fw-bold">${element}%</td>`
                }
            }
            
        }
        if (dateformat.length == 24) {
            i2 = 1
            labels = numbersArray = Array.from({ length: dateformat.length }, (_, index) => index + 1);
            for(let i = 0; i < dateformat.length; i++) {
                dataDateList.innerHTML = dataDateList.innerHTML + `<th class='fs-6'>${i2} hour</th>`
                //let dataListElement = document.getElementById(`${i}hr`);
                i2 = i2 + 1
            }
            for(let i = 0; i < dateformat.length; i++) { 
                let element = effectivenessArray[i];
                if (element > 100) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-danger fw-bold">${element}%</td>`
                }
                if (element < 98) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-warning fw-bold">${element}%</td>`
                }
                if (element > 98 && element < 101 || element == 98) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-success fw-bold">${element}%</td>`
                }
            }
           
        }
        if (dateformat.length == 6) {
            labels = numbersArray = Array.from({ length: dateformat.length }, (_, index) => index + 1);
            i2 = 0
            years = [2019,2020,2021,2022,2023,2024]
            for(let i = 0; i < dateformat.length; i++) {
                dataDateList.innerHTML = dataDateList.innerHTML + `<th class='fs-6'>${years[i]} year</th>`
                //let dataListElement = document.getElementById(`${i}hr`);
                i2 = i2 + 1
            }
            for(let i = 0; i < dateformat.length; i++) { 
                let element = effectivenessArray[i];
                if (element > 100) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-danger fw-bold">${element}%</td>`
                }
                if (element < 98) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-warning fw-bold">${element}%</td>`
                }
                if (element > 98 && element < 101 || element == 98) {
                    dataList.innerHTML = dataList.innerHTML + `<td class="text-success fw-bold">${element}%</td>`
                }
            }
        }
        console.log(effectivenessArray); // This will log the "effectiveness" array to the console
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