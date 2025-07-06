function setupTrelloButton() {
    const trelloButton = document.getElementById('colocar-trello');
    if (!trelloButton) return;
    trelloButton.addEventListener('click', () => {
        trelloButton.classList.toggle('active');
    });
}

/**
 * Torna global a função de submissão do formulário de cotação,
 * preenchendo o campo oculto da seguradora antes de enviar.
 */
function setupCotarFormSubmission() {
    window.submitCotarForm = (cotacaoId) => {
        // Obtenha o valor da seguradora selecionada
        const seguradora = document.querySelector('input[name="seguradora"]:checked');
        if (!seguradora) {
            alert("Por favor, selecione uma seguradora antes de cotar.");
            return;
        }

        // Preencha o campo oculto com o valor da seguradora
        const seguradoraInput = document.getElementById(`seguradora-input-${cotacaoId}`);
        if (seguradoraInput) {
            seguradoraInput.value = seguradora.value;
        }

        // Submeta o formulário
        const form = document.getElementById(`cotar-form-${cotacaoId}`);
        if (form) {
            form.submit();
        }
    };
}

/**
 * Sincroniza o valor do radio de seguradora com os campos hidden dos formulários "quitado" e "financiado".
 */
function syncSeguradoraHiddenFields() {
    document.querySelectorAll('input[name="seguradora"]').forEach(function(radio) {
        radio.addEventListener('change', function() {
            const quitado = document.getElementById('seguradora_quitado');
            const financiado = document.getElementById('seguradora_financiado');
            if (quitado) quitado.value = this.value;
            if (financiado) financiado.value = this.value;
        });
    });
}

/**
 * Sincroniza o select de cotação do topo com os campos hidden dos dois formulários.
 */
function syncCotacaoIdHiddenFields() {
    const selectCotacao = document.getElementById('cotacao_id_topo');
    const hiddenQuitado = document.getElementById('cotacao_id_quitado');
    const hiddenFinanciado = document.getElementById('cotacao_id_financiado');
    if (selectCotacao && hiddenQuitado && hiddenFinanciado) {
        selectCotacao.addEventListener('change', function() {
            hiddenQuitado.value = this.value;
            hiddenFinanciado.value = this.value;
        });
    }
}

/**
 * Mostra ou esconde os campos do cônjuge conforme o estado civil selecionado.
 */
function toggleCamposConjuge() {
    const casado = document.querySelector('input[name="estado_civil"]:checked');
    const div = document.getElementById('campos-conjuge');
    const linha = document.getElementById('linha-conjuge');
    if (div) {
        if (casado && casado.value === 'Casado') {
            div.style.display = '';
            if (linha) linha.style.display = '';
        } else {
            div.style.display = 'none';
            if (linha) linha.style.display = 'none';
            if (document.getElementById('nome_conjuge')) document.getElementById('nome_conjuge').value = '';
            if (document.getElementById('data_nascimento_conjuge')) document.getElementById('data_nascimento_conjuge').value = '';
            if (document.getElementById('documento_conjuge')) document.getElementById('documento_conjuge').value = '';
        }
    }
}

/**
 * Exibe um alerta global no topo da tela para seleção de seguradora.
 */
function mostrarAlertaTopoSeguradora() {
    var alerta = document.getElementById('alert-topo-seguradora');
    if (alerta) {
        alerta.classList.remove('d-none');
        // Some automaticamente após 3s
        clearTimeout(alerta._timeoutId);
        alerta._timeoutId = setTimeout(function() {
            alerta.classList.add('d-none');
        }, 3000);
    }
}

/**
 * Valida se uma seguradora foi selecionada antes de submeter o formulário de preço.
 */
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

/**
 * Valida se uma taxa foi selecionada antes de submeter o formulário de preço.
 */
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

// Atualiza o campo hidden de taxa conforme o radio selecionado
function atualizarTaxaHidden(valor) {
    const quitado = document.getElementById('taxa_cotacao_quitado');
    const financiado = document.getElementById('taxa_cotacao_financiado');
    if (quitado) quitado.value = valor;
    if (financiado) financiado.value = valor;
}

// Adiciona event listener aos radios de taxa
function setupTaxaRadios() {
    const radiosTaxa = document.querySelectorAll('input[name="taxa_cotacao"]');
    radiosTaxa.forEach(radio => {
        radio.addEventListener('change', function() {
            if (this.checked) {
                atualizarTaxaHidden(this.value);
            }
        });
    });
    // Garante valor inicial correto
    const radioInicial = document.querySelector('input[name="taxa_cotacao"]:checked');
    if (radioInicial) atualizarTaxaHidden(radioInicial.value);
}

// Inicialização dos módulos ao carregar o DOM
document.addEventListener('DOMContentLoaded', () => {
    setupTrelloButton();
    setupCotarFormSubmission();
    syncSeguradoraHiddenFields();
    syncCotacaoIdHiddenFields();

    // Adiciona o controle dos campos do cônjuge se existir o campo de estado civil
    const radios = document.querySelectorAll('input[name="estado_civil"]');
    if (radios.length > 0) {
        radios.forEach(r => r.addEventListener('change', toggleCamposConjuge));
        toggleCamposConjuge();
    }

    // Manipulação dinâmica de veículos e pessoas agora está em formHandlers.js

    // Validação de seguradora ao submeter qualquer formulário de preço
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

    setupTaxaRadios();
});