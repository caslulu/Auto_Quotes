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

// Máscara de moeda em dólar para campos de valor
function setupDollarMaskPreco() {
    if (typeof IMask === 'undefined') return;
    const moneyFields = [
        'entrada_basico', 'mensal_basico', 'valor_total_basico',
        'entrada_completo', 'mensal_completo', 'valor_total_completo'
    ];
    moneyFields.forEach(function(fieldName) {
        document.querySelectorAll('input[name$="' + fieldName + '"]')
            .forEach(function(input) {
                IMask(input, {
                    mask: '$ num',
                    blocks: {
                        num: {
                            mask: Number,
                            thousandsSeparator: ',',
                            radix: '.',
                            scale: 2,
                            padFractionalZeros: true,
                            normalizeZeros: true,
                            min: 0
                        }
                    },
                    lazy: false
                });
            });
    });
}

// Sincroniza campos mascarados com hidden antes do submit
function syncDollarFieldsBeforeSubmit() {
    document.querySelectorAll('form.preco-form').forEach(form => {
        form.addEventListener('submit', function() {
            [
                'entrada_basico', 'mensal_basico', 'valor_total_basico',
                'entrada_completo', 'mensal_completo', 'valor_total_completo'
            ].forEach(function(fieldName) {
                const masked = form.querySelector('input[name="' + fieldName + '_masked"]');
                const hidden = form.querySelector('input[name="' + fieldName + '"]');
                if (masked && hidden) {
                    if (masked.inputMask && masked.inputMask.unmaskedValue !== undefined) {
                        hidden.value = masked.inputMask.unmaskedValue;
                    } else if (masked.IMask && masked.IMask.unmaskedValue !== undefined) {
                        hidden.value = masked.IMask.unmaskedValue;
                    } else {
                        hidden.value = masked.value.replace(/\$/g, '').replace(/ /g, '').replace(/[^0-9.,-]/g, '');
                    }
                }
            });
        }, true);
    });
}

window.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('input[data-mask="date"]').forEach(maskDateInput);
    document.querySelectorAll('input[data-mask="vin"]').forEach(maskVinInput);
    [
        'entrada_basico_masked', 'mensal_basico_masked', 'valor_total_basico_masked',
        'entrada_completo_masked', 'mensal_completo_masked', 'valor_total_completo_masked'
    ].forEach(function(fieldName) {
        document.querySelectorAll('input[name="' + fieldName + '"]').forEach(function(input) {
            IMask(input, {
                mask: '$ num',
                blocks: {
                    num: {
                        mask: Number,
                        thousandsSeparator: '.',
                        radix: ',',
                        scale: 2,
                        padFractionalZeros: true,
                        normalizeZeros: true,
                        min: 0
                    }
                },
                lazy: false
            });
        });
    });
    syncDollarFieldsBeforeSubmit();
});


