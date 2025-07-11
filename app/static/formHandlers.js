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
        // Remoção de veículo agora é tratada apenas em setupConfirmacaoRemocao
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
        // Remoção de pessoa agora é tratada apenas em setupConfirmacaoRemocao
    }
}

// campo de upload de arquivos
function setupModernFileUpload(imagemDocId, labelId, labelTextId, previewId) {
    const fileInput = document.getElementById(imagemDocId);
    const label = document.getElementById(labelId);
    const labelText = document.getElementById(labelTextId);
    const preview = document.getElementById(previewId);
    let filesList = [];

    if (fileInput && label) {
        fileInput.addEventListener('change', function(e) {

            const newFiles = Array.from(fileInput.files);
            filesList = filesList.concat(newFiles);

            filesList = filesList.filter((file, idx, arr) =>
                arr.findIndex(f => f.name === file.name && f.size === file.size) === idx
            );

            fileInput.value = '';
            // Atualizar label
            if (filesList.length === 0) {
                labelText.textContent = 'Selecionar arquivos';
                preview.innerHTML = '';
                return;
            }

            if (filesList.length === 1) {
                labelText.textContent = 'Selecionar arquivos (1)';
            } else {
                labelText.textContent = `Selecionar arquivos (${filesList.length})`;
            }
            // Preview list
            preview.innerHTML = '';
            filesList.forEach((file, idx) => {
                const ext = file.name.split('.').pop().toLowerCase();
                let icon = 'fa-file';
                if (["jpg","jpeg","png","gif","bmp","webp"].includes(ext)) {
                    icon = 'fa-file-image';
                    const reader = new FileReader();
                    reader.onload = function(ev) {
                        const item = document.createElement('div');
                        item.className = 'file-preview-item';
                        item.innerHTML = `<img src='${ev.target.result}' class='file-thumb-img' alt='preview'/> <span class='file-name'>${file.name}</span> <button type='button' class='remove-file-btn' data-idx='${idx}' title='Remover'>&times;</button>`;
                        preview.appendChild(item);
                    };
                    reader.readAsDataURL(file);
                    return;
                }
                else if (["pdf"].includes(ext)) icon = 'fa-file-pdf';
                else if (["doc","docx"].includes(ext)) icon = 'fa-file-word';
                else if (["xls","xlsx"].includes(ext)) icon = 'fa-file-excel';
                else if (["zip","rar","7z"].includes(ext)) icon = 'fa-file-archive';
                const item = document.createElement('div');
                item.className = 'file-preview-item';
                item.innerHTML = `<i class=\"fas ${icon}\"></i> <span class=\"file-name\">${file.name}</span> <button type='button' class='remove-file-btn' data-idx='${idx}' title='Remover'>&times;</button>`;
                preview.appendChild(item);
            });
        });
        // Remover arquivo do preview
        preview.addEventListener('click', function(e) {
            if (e.target.classList.contains('remove-file-btn')) {
                const idx = parseInt(e.target.getAttribute('data-idx'));
                filesList.splice(idx, 1);
                // Atualizar preview
                if (filesList.length === 0) {
                    labelText.textContent = 'Selecionar arquivos';
                } else if (filesList.length === 1) {
                    labelText.textContent = 'Selecionar arquivos (1)';
                } else {
                    labelText.textContent = `Selecionar arquivos (${filesList.length})`;
                }

                preview.innerHTML = '';
                filesList.forEach((file, idx) => {
                    const ext = file.name.split('.').pop().toLowerCase();
                    let icon = 'fa-file';
                    if (["jpg","jpeg","png","gif","bmp","webp"].includes(ext)) {
                        icon = 'fa-file-image';
                        const reader = new FileReader();
                        reader.onload = function(ev) {
                            const item = document.createElement('div');
                            item.className = 'file-preview-item';
                            item.innerHTML = `<img src='${ev.target.result}' class='file-thumb-img' alt='preview'/> <span class='file-name'>${file.name}</span> <button type='button' class='remove-file-btn' data-idx='${idx}' title='Remover'>&times;</button>`;
                            preview.appendChild(item);
                        };
                        reader.readAsDataURL(file);
                        return;
                    }
                    else if (["pdf"].includes(ext)) icon = 'fa-file-pdf';
                    else if (["doc","docx"].includes(ext)) icon = 'fa-file-word';
                    else if (["xls","xlsx"].includes(ext)) icon = 'fa-file-excel';
                    else if (["zip","rar","7z"].includes(ext)) icon = 'fa-file-archive';
                    const item = document.createElement('div');
                    item.className = 'file-preview-item';
                    item.innerHTML = `<i class=\"fas ${icon}\"></i> <span class=\"file-name\">${file.name}</span> <button type='button' class='remove-file-btn' data-idx='${idx}' title='Remover'>&times;</button>`;
                    preview.appendChild(item);
                });
            }
        });
        // Antes de enviar o form, criar um DataTransfer para enviar todos os arquivos acumulados
        const form = fileInput.closest('form');
        if (form) {
            form.addEventListener('submit', function(e) {
                if (filesList.length > 0) {
                    const dt = new DataTransfer();
                    filesList.forEach(f => dt.items.add(f));
                    fileInput.files = dt.files;
                }
            });
        }
    }
}

// Confirmação antes de excluir veículos, pessoas ou cards de cotação
function setupConfirmacaoRemocao() {
    // Veículos
    const veiculosList = document.getElementById('veiculos-list');
    if (veiculosList) {
        veiculosList.addEventListener('click', function(e) {
            if (e.target.classList.contains('remove-veiculo')) {
                if (veiculosList.children.length > 1) {
                    e.preventDefault();
                    e.stopPropagation();
                    setTimeout(function() {
                        if (window.confirm('Tem certeza que deseja remover este veículo?')) {
                            e.target.closest('.veiculo-item').remove();
                        }
                    }, 0);
                }
            }
        }, true);
    }
    // Pessoas
    const pessoasList = document.getElementById('pessoas-list');
    if (pessoasList) {
        pessoasList.addEventListener('click', function(e) {
            if (e.target.classList.contains('remove-pessoa')) {
                e.preventDefault();
                e.stopPropagation();
                setTimeout(function() {
                    if (window.confirm('Tem certeza que deseja remover esta pessoa?')) {
                        e.target.closest('.pessoa-item').remove();
                    }
                }, 0);
            }
        }, true);
    }
    // Cards de cotação
    document.body.addEventListener('click', function(e) {
        if (e.target.classList.contains('remove-cotacao')) {
            const btn = e.target;
            const form = btn.closest('form.form-apagar-cotacao');
            if (form) {
                e.preventDefault();
                e.stopPropagation();
                setTimeout(function() {
                    if (window.confirm('Tem certeza que deseja remover esta cotação?')) {
                        form.submit();
                    }
                }, 0);
            } else {
                e.preventDefault();
                e.stopPropagation();
                setTimeout(function() {
                    if (window.confirm('Tem certeza que deseja remover esta cotação?')) {
                        let card = btn.closest('.cotacao-card, .card, .cotacao-item');
                        if (card) {
                            card.remove();
                        }
                    }
                }, 0);
            }
        }
    }, true);
}

// Sincroniza o campo hidden de idioma com o radio global antes do submit dos formulários de preço
function setupIdiomaCotacaoSync() {
    const radios = document.getElementsByName('idioma_cotacao_radio');
    function updateIdiomaHidden() {
        let val = 'pt';
        for (const r of radios) { if (r.checked) val = r.value; }
        const hiddenQuitado = document.getElementById('idioma_cotacao_quitado');
        const hiddenFinanciado = document.getElementById('idioma_cotacao_financiado');
        if (hiddenQuitado) hiddenQuitado.value = val;
        if (hiddenFinanciado) hiddenFinanciado.value = val;
    }
    radios.forEach(r => r.addEventListener('change', updateIdiomaHidden));
    updateIdiomaHidden();
    // Garante atualização do hidden imediatamente antes do submit
    document.querySelectorAll('form.preco-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            updateIdiomaHidden();
        });
    });
}

function setupSeguradoraSync() {
    function updateSeguradoraHidden() {
        const radio = document.querySelector('input[name="seguradora"]:checked');
        const val = radio ? radio.value : '';
        const hiddenQuitado = document.getElementById('seguradora_quitado');
        const hiddenFinanciado = document.getElementById('seguradora_financiado');
        if (hiddenQuitado) hiddenQuitado.value = val;
        if (hiddenFinanciado) hiddenFinanciado.value = val;
    }
    document.querySelectorAll('input[name="seguradora"]').forEach(r => {
        r.addEventListener('change', updateSeguradoraHidden);
    });
    document.querySelectorAll('form.preco-form').forEach(form => {
        form.addEventListener('submit', function() {
            updateSeguradoraHidden();
        });
    });
    updateSeguradoraHidden();
}

// Inicialização
window.addEventListener('DOMContentLoaded', function() {
    setupVeiculosDinamicos();
    setupPessoasDinamicas();
    setupConfirmacaoRemocao();
    setupIdiomaCotacaoSync();
    setupSeguradoraSync();
    const fileInput = document.getElementById('imagem_doc');
    if (fileInput) {
        setupModernFileUpload('imagem_doc', 'imagem-doc-label', 'imagem-doc-label-text', 'imagem-doc-preview');
    }
});