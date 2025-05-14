/// Modo Claro/Escuro
const toggleButton = document.getElementById('theme-toggle');
const body = document.body;

toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    body.classList.toggle('light-mode');
    toggleButton.textContent = body.classList.contains('dark-mode') ? 'Modo Claro' : 'Modo Escuro';
});

/// Botão "Colocar Trello"
document.addEventListener('DOMContentLoaded', () => {
    const trelloButton = document.getElementById('colocar-trello');

    trelloButton.addEventListener('click', () => {
        trelloButton.classList.toggle('active');
    });



    /// Botão "Cotar"
const submitCotarForm = (cotacaoId) => {
        // Obtenha o valor da seguradora selecionada
        const seguradora = document.querySelector('input[name="seguradora"]:checked');
        if (!seguradora) {
            alert("Por favor, selecione uma seguradora antes de cotar.");
            return;
        }

        // Preencha o campo oculto com o valor da seguradora
        const seguradoraInput = document.getElementById(`seguradora-input-${cotacaoId}`);
        seguradoraInput.value = seguradora.value;

        // Submeta o formulário
        const form = document.getElementById(`cotar-form-${cotacaoId}`);
        form.submit();
    };

    // Torne a função global para ser chamada no HTML
    window.submitCotarForm = submitCotarForm;
});

