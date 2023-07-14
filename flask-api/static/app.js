document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const resultContainer = document.getElementById('resultContainer');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        console.log("reached 1")
        let lawChoice = document.querySelector("select[name=lawoptions]").value;
        let state = document.querySelector("select[name=state]").value;
        
        api = "/laws" + lawChoice;
        if (state != ""){
            api+= "/" + state + ".json";
        }
        if (lawChoice == "") {
            api = '/laws';
        }
        console.log("Fetching: ", api)
        fetch(api).then(function(response) {
            
            console.log("reached 2")
            return response.json();
        }).then(function(response) {
            console.log("Successful async: ", JSON.stringify(response));
            const propertyNames = Object.keys(response[0]);

        resultContainer.innerHTML = `
    <table style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr>
                ${propertyNames.map(propertyName => `<th>${propertyName}</th>`).join('')}
            </tr>
        </thead>
        <tbody>
            ${response.map(item => `
                <tr>
                    ${propertyNames.map(propertyName => `<td style="padding: 8px; text-align: center;">${item[propertyName]}</td>`).join('')}
                </tr>
            `).join('')}
        </tbody>
    </table>
`;
            console.log("HERE",lawChoice,state)
            //resultContainer.innerHTML = JSON.stringify(response,null, 4);
        }).catch(function(error) {
            console.log("Error in async", error);
        });
    });
});