document.addEventListener('DOMContentLoaded', function () {
    // Add your JavaScript code here
    console.log('Flight Web App Initialized');

    // Example: Fetch data from the server using Fetch API

});


function validateForm() {
    var selectedDate = document.getElementById('select_departure_date').value;

    if (!selectedDate) {
        alert('Please select a departure date.');
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}


//extra-part

function toggleReturnDate() {
    var tripType = document.getElementById('flight_type').value;
    var returnDateInput = document.getElementById('return_date');

    // If the selected trip type is "Round Trip," enable and show the return date input; otherwise, disable and hide it
    if (tripType === 'round_trip') {
        returnDateInput.removeAttribute('disabled');
        returnDateInput.style.display = 'block';
    } else {
        returnDateInput.setAttribute('disabled', 'disabled');
        returnDateInput.style.display = 'none';
    }
}
