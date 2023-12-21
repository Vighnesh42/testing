document.addEventListener('DOMContentLoaded', function () {
    // ... your existing code ...

    // Add an event listener to the trip type select
    const flightTypeSelect = document.getElementById('flightt_type');
    if (flightTypeSelect) {
        flightTypeSelect.addEventListener('change', toggleReturnDate);
        // Initialize the state of the return date based on the default value
        toggleReturnDate();
    }

    // Get references to the date inputs
    const selectDepartureDate = document.getElementById('departure_date');
    const selectedDepartureDate = document.getElementById('selected_departure_date');
    const returnDateInput = document.getElementById('returnn_date');

    // Disable the Selected Departure Date and Return Date inputs initially
    selectedDepartureDate.disabled = true;
    returnDateInput.disabled = true;

    // Add an event listener to the Select Departure Date input
    selectDepartureDate.addEventListener('change', function () {
        // Enable the Selected Departure Date input when a date is selected
        selectedDepartureDate.disabled = false;
        // Copy the selected date to the Selected Departure Date input
        selectedDepartureDate.value = selectDepartureDate.value;

        // Enable or disable the Return Date input based on the trip type
        toggleReturnDate();
    });

    function toggleReturnDate() {
        const tripTypeSelect = document.getElementById('flightt_type');
        // If the selected trip type is "Round Trip," enable the return date; otherwise, disable it.
        returnDateInput.disabled = tripTypeSelect.value !== 'round_trip';
    }

    // Initialize the state of the return date based on the default value
    toggleReturnDate();
});
