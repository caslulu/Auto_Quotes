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

document.addEventListener('DOMContentLoaded', () => {
    // Tema claro/escuro com ícone dinâmico
    const saved = localStorage.getItem('theme-mode') || 'light-mode';
    setTheme(saved);

    const btn = document.getElementById('theme-toggle');
    if (btn) btn.addEventListener('click', toggleThemeMode);
});