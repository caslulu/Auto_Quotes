// Validações customizadas de formulário
// Exemplo: validar se seguradora foi selecionada antes de enviar

function validarSeguradoraAntesDeEnviar(e) {
    var radios = document.querySelectorAll('input[name="seguradora"]');
    var algumSelecionado = false;
    radios.forEach(function(r) { if (r.checked) algumSelecionado = true; });
    if (!algumSelecionado) {
        mostrarAlertaTopoSeguradora();
        e.preventDefault();
        e.stopPropagation();
        return false;
    }
}

function validarTaxaAntesDeEnviar(e) {
    var radios = document.querySelectorAll('input[name="taxa_cotacao"]');
    var algumSelecionado = false;
    radios.forEach(function(r) { if (r.checked) algumSelecionado = true; });
    if (!algumSelecionado) {
        alert('Por favor, selecione uma taxa antes de enviar o formulário.');
        e.preventDefault();
        e.stopPropagation();
        return false;
    }
}

// Inicialização
window.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.preco-form').forEach(function(form) {
        form.addEventListener('submit', validarSeguradoraAntesDeEnviar);
        form.addEventListener('submit', validarTaxaAntesDeEnviar);
    });
    // Esconde alerta ao trocar seguradora
    document.querySelectorAll('input[name="seguradora"]').forEach(function(radio) {
        radio.addEventListener('change', function() {
            var alerta = document.getElementById('alert-topo-seguradora');
            if (alerta) alerta.classList.add('d-none');
        });
    });
});
