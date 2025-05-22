/**
 * Alterna entre os modos claro e escuro do site com transição suave e ícone dinâmico.
 */
function setTheme(mode) {
    document.body.classList.remove('light-mode', 'dark-mode');
    document.body.classList.add(mode);
    localStorage.setItem('theme-mode', mode);
    // Atualiza o ícone
    const icon = document.getElementById('theme-icon');
    if (icon) icon.textContent = mode === 'dark-mode' ? '☀️' : '🌙';
}

function toggleThemeMode() {
    const current = document.body.classList.contains('dark-mode') ? 'dark-mode' : 'light-mode';
    setTheme(current === 'dark-mode' ? 'light-mode' : 'dark-mode');
}

/**
 * Adiciona o comportamento de ativação visual ao botão "Colocar Trello".
 */
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

// Inicialização dos módulos ao carregar o DOM
document.addEventListener('DOMContentLoaded', () => {
    // Tema claro/escuro com ícone dinâmico
    const saved = localStorage.getItem('theme-mode') || 'light-mode';
    setTheme(saved);

    const btn = document.getElementById('theme-toggle');
    if (btn) btn.addEventListener('click', toggleThemeMode);

    setupTrelloButton();
    setupCotarFormSubmission();
    syncSeguradoraHiddenFields();
    syncCotacaoIdHiddenFields();
});