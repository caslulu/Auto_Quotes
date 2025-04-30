const toggleButton = document.getElementById('theme-toggle');
const body = document.body;

toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    body.classList.toggle('light-mode');
    toggleButton.textContent = body.classList.contains('dark-mode') ? 'Modo Claro' : 'Modo Escuro';
});