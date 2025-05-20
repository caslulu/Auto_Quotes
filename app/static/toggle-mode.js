/**
 * Alterna entre os modos claro e escuro do site.
 */
function toggleThemeMode() {
    const toggleButton = document.getElementById('theme-toggle');
    const body = document.body;

    // Aplica o modo salvo ao carregar
    const savedMode = localStorage.getItem('theme-mode');
    if (savedMode === 'dark') {
        body.classList.add('dark-mode');
        body.classList.remove('light-mode');
        toggleButton.textContent = 'Modo Claro';
    } else {
        body.classList.add('light-mode');
        body.classList.remove('dark-mode');
        toggleButton.textContent = 'Modo Escuro';
    }

    toggleButton.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        body.classList.toggle('light-mode');
        const isDark = body.classList.contains('dark-mode');
        toggleButton.textContent = isDark ? 'Modo Claro' : 'Modo Escuro';
        localStorage.setItem('theme-mode', isDark ? 'dark' : 'light');
    });
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

// Inicialização dos módulos ao carregar o DOM
document.addEventListener('DOMContentLoaded', () => {
    toggleThemeMode();
    setupTrelloButton();
    setupCotarFormSubmission();
    syncSeguradoraHiddenFields();
});