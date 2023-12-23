document.getElementById('filterbut').onclick = function () {
        filter = document.getElementById('filter').value;
        console.log('filter applied.')
        if (filter == 'all') {
            elements = document.querySelectorAll("#" + 'goodProd');
            elements.forEach(function(element) {
                console.log('balls')
                element.style.display = "block";
            })
            elements = document.querySelectorAll("#" + 'underProd');
            elements.forEach(function(element) {
                console.log('balls')
                element.style.display = "block";
            })
            elements = document.querySelectorAll("#" + 'overProd');
            elements.forEach(function(element) {
                console.log('balls')
                element.style.display = "block";
            })
            console.log('hee hee hee ha!')
        }
        if (filter == 'undr') {
            console.log('balls')
            elements = document.querySelectorAll("#" + 'underProd');
            elements.forEach(function(element) {
                console.log('balls')
                element.style.display = "none";
            });
        }
        if (filter == 'over') {
            elements = document.querySelectorAll("#" + 'overProd');
            elements.forEach(function(element) {
                element.style.display = "none";;
            });
        }
        if (filter == 'good') {
            elements = document.querySelectorAll("#" + 'goodProd');
            elements.forEach(function(element) {
                element.style.display = "none";
            });
        }
    }
