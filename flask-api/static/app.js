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
            resultContainer.innerHTML = `
            <pre style="white-space: pre-wrap; font-family: monospace; padding: 1em; background-color: #f4f4f4;">
            ${JSON.stringify(response, null, 2)}
            </pre>
            `;
            console.log("HERE",lawChoice,state)
            //resultContainer.innerHTML = JSON.stringify(response,null, 4);
        }).catch(function(error) {
            console.log("Error in async", error);
        });
    });
});