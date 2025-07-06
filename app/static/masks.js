function maskDateInput(input) {
    input.addEventListener('input', function(e) {
        let value = input.value.replace(/\D/g, '');
        if (value.length > 8) value = value.slice(0, 8);
        let result = '';
        if (value.length > 4) {
            result = value.slice(0,2) + '/' + value.slice(2,4) + '/' + value.slice(4);
        } else if (value.length > 2) {
            result = value.slice(0,2) + '/' + value.slice(2);
        } else {
            result = value;
        }
        input.value = result;
    });
}

function maskVinInput(input) {
    input.addEventListener('input', function(e) {
        let value = input.value.replace(/[^a-zA-Z0-9]/g, '');
        if (value.length > 17) value = value.slice(0, 17);
        input.value = value.toUpperCase();
    });
}

window.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('input[data-mask="date"]').forEach(maskDateInput);
    document.querySelectorAll('input[data-mask="vin"]').forEach(maskVinInput);
});


