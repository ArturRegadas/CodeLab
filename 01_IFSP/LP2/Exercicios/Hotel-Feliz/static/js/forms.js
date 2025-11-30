
function openModal(id) {
    const m = document.getElementById(id);
    if (m) {
        m.style.display = 'block';
        m.setAttribute('aria-hidden', 'false');
    }
}
function closeModal(id) {
    const m = document.getElementById(id);
    if (m) {
        m.style.display = 'none';
        m.setAttribute('aria-hidden', 'true');
    }
}
async function popularSelectTipos() {
    try {
        const result = await apiGet('/tipos_quarto');
        const tipos = Array.isArray(result) ? result : result.items || [];
        const sel = document.getElementById('id_tipo');
        if (!sel) return;
        sel.innerHTML = '<option value="">-- selecione --</option>';
        tipos.forEach(t => {
            const opt = document.createElement('option');
            opt.value = t.id_tipo;
            opt.textContent = `${t.nome_tipo} (cap: ${t.capacidade_maxima})`;
            sel.appendChild(opt);
        });
    } catch (e) {
        console.error('Erro ao carregar tipos de quarto', e);
    }
}
async function carregarPerfis() {
    const sel = document.getElementById('perfil');
    if (!sel) return;
    sel.innerHTML = '<option>Carregando...</option>';
    try {
        const perfis = await apiGet('/perfis');
        sel.innerHTML = '';
        perfis.forEach(p => {
            const o = document.createElement('option');
            o.value = p.id;
            o.textContent = p.nome_perfil;
            sel.appendChild(o);
        });
    } catch (e) {
        console.error(e);
        sel.innerHTML = '<option>Erro</option>';
    }
}
async function criarServico() {
    const nome = prompt('Nome do serviÃ§o:');
    if (!nome) return;
    const preco = prompt('PreÃ§o do serviÃ§o:');
    if (!preco) return;
    try {
        await apiPost('/servicos', { nome_servico: nome, preco: parseFloat(preco) });
        carregarServicos();
    } catch (e) {
        console.error(e);
        alert('Erro ao criar serviÃ§o');
    }
}
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.modal-close').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const modal = e.target.closest('.modal');
            if (modal) {
                modal.style.display = 'none';
                modal.setAttribute('aria-hidden', 'true');
            }
        });
    });
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
                modal.setAttribute('aria-hidden', 'true');
            }
        });
    });
});
