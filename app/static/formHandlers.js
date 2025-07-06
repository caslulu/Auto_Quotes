// Manipulação dinâmica de formulários: veículos e pessoas

// --- Adição dinâmica de veículos (cotacao.html) ---
function setupVeiculosDinamicos() {
    const addBtn = document.getElementById('add-veiculo');
    const veiculosList = document.getElementById('veiculos-list');
    const template = document.getElementById('veiculo-template');

    if (addBtn && veiculosList && template) {
        addBtn.addEventListener('click', function() {
            const total = veiculosList.children.length;
            const html = template.innerHTML.replace(/__index__/g, total);
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = html;
            veiculosList.appendChild(tempDiv.firstElementChild);
        });

        veiculosList.addEventListener('click', function(e) {
            if (e.target.classList.contains('remove-veiculo')) {
                if (veiculosList.children.length > 1) {
                    e.target.closest('.veiculo-item').remove();
                }
            }
        });
    }
}

// --- Adição dinâmica de pessoas (cotacao.html) ---
function setupPessoasDinamicas() {
    const addPessoaBtn = document.getElementById('add-pessoa');
    const pessoasList = document.getElementById('pessoas-list');
    const pessoaTemplate = document.getElementById('pessoa-template');

    if (addPessoaBtn && pessoasList && pessoaTemplate) {
        addPessoaBtn.addEventListener('click', function() {
            const total = pessoasList.children.length;
            const html = pessoaTemplate.innerHTML.replace(/__index__/g, total);
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = html;
            pessoasList.appendChild(tempDiv.firstElementChild);
        });

        pessoasList.addEventListener('click', function(e) {
            if (e.target.classList.contains('remove-pessoa')) {
                e.target.closest('.pessoa-item').remove();
            }
        });
    }
}

// Inicialização
window.addEventListener('DOMContentLoaded', function() {
    setupVeiculosDinamicos();
    setupPessoasDinamicas();
});
