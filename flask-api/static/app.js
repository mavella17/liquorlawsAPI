document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const resultContainer = document.getElementById('resultContainer');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const stateInput = document.getElementById('stateInput');
        const state = stateInput.value;

        // Here: API request to fetch the liquor laws based on the state input

        // Example code to display the results
        resultContainer.innerHTML = `
            <h2>${state}</h2>
            <p>Liquor laws for ${state}:</p>
            <ul>
                <li>Law 1</li>
                <li>Law 2</li>
                <li>Law 3</li>
                <!-- Add more liquor laws -->
            </ul>
        `;
    });
});
