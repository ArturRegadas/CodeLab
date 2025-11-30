
async function apiGet(path) {
    const res = await fetch(path, { credentials: 'same-origin' });
    if (!res.ok) throw new Error((await res.json()).error || 'Erro');
    return res.json();
}
async function apiPost(path, body) {
    const res = await fetch(path, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
        credentials: 'same-origin'
    });
    if (!res.ok) throw new Error((await res.json()).error || 'Erro');
    return res.json();
}
async function apiPut(path, body) {
    const res = await fetch(path, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
        credentials: 'same-origin'
    });
    if (!res.ok) throw new Error((await res.json()).error || 'Erro');
    return res.json();
}
async function apiDelete(path) {
    const res = await fetch(path, { method: 'DELETE', credentials: 'same-origin' });
    if (!res.ok) throw new Error((await res.json()).error || 'Erro');
    return res.json();
}
if (!window.__paginationState) window.__paginationState = {};
function buildQuery(path, page, per_page) {
    const url = new URL(path, window.location.origin);
    if (page) url.searchParams.set('page', page);
    if (per_page) url.searchParams.set('per_page', per_page);
    return url.pathname + url.search;
}
async function fetchPaginated(path, page = 1, per_page = 10) {
    const full = buildQuery(path, page, per_page);
    const res = await apiGet(full);
    if (Array.isArray(res)) return { items: res, meta: null };
    return { items: res.items || [], meta: { page: res.page, per_page: res.per_page, total: res.total, pages: res.pages } };
}
function renderPaginationControls(containerId, meta, onPage) {
    if (!meta) return null;
    let container = document.getElementById(containerId);
    if (!container) {
        container = document.createElement('div');
        container.id = containerId;
    }
    container.className = 'pagination-controls';
    container.innerHTML = '';
    const prev = document.createElement('button');
    prev.textContent = '‹ Anterior';
    prev.className = 'btn btn-sm';
    prev.disabled = meta.page <= 1;
    prev.addEventListener('click', () => onPage(meta.page - 1));
    const info = document.createElement('span');
    info.className = 'pagination-info';
    info.textContent = ` Página ${meta.page} de ${meta.pages} (total: ${meta.total}) `;
    const next = document.createElement('button');
    next.textContent = 'Próximo ›';
    next.className = 'btn btn-sm';
    next.disabled = meta.page >= meta.pages;
    next.addEventListener('click', () => onPage(meta.page + 1));
    container.appendChild(prev);
    container.appendChild(info);
    container.appendChild(next);
    return container;
}
function attachPaginationToTable(tableId, paginationId, meta, reloadFunc) {
    const table = document.getElementById(tableId);
    if (!table) return;
    let pag = renderPaginationControls(paginationId, meta, reloadFunc);
    if (pag) table.parentNode.insertBefore(pag, table.nextSibling);
}
async function carregarPerfis() {
    try {
        const perfis = await apiGet('/perfis');
        const ul = document.getElementById('lista-perfis');
        if (!ul) return;
        ul.innerHTML = '';
        perfis.forEach(p => {
            const li = document.createElement('li');
            li.textContent = `${p.id}: ${p.nome_perfil}`;
            ul.appendChild(li);
        });
    } catch (e) {
        console.error(e);
    }
}
async function carregarUsuarios() {
    try {
        const stateKey = 'usuarios';
        const current = window.__paginationState[stateKey] || 1;
        const { items: users, meta } = await fetchPaginated('/usuarios', current, 10);
        const tbody = document.querySelector('#table-usuarios tbody');
        if (!tbody) return;
        tbody.innerHTML = '';
        users.forEach(u => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${u.id}</td>
                <td>${u.nome_completo}</td>
                <td>${u.email}</td>
                <td>${u.perfil ? u.perfil : ''}</td>
            `;
            tbody.appendChild(tr);
        });
        attachPaginationToTable('table-usuarios', 'pagination-usuarios', meta, 
            (p) => { window.__paginationState[stateKey] = p; carregarUsuarios(); });
    } catch (e) {
        console.error(e);
    }
}
async function carregarTiposQuarto() {
    try {
        const stateKey = 'tipos_quarto';
        const current = window.__paginationState[stateKey] || 1;
        const { items: tipos, meta } = await fetchPaginated('/tipos_quarto', current, 10);
        const tbody = document.querySelector('#table-tipos-quarto tbody');
        if (!tbody) return;
        tbody.innerHTML = '';
        tipos.forEach(t => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${t.id_tipo}</td>
                <td>${t.nome_tipo}</td>
                <td>${t.capacidade_maxima}</td>
                <td>R$ ${t.preco_diaria_base}</td>
                <td>${t.descricao || ''}</td>
            `;
            tbody.appendChild(tr);
        });
        attachPaginationToTable('table-tipos-quarto', 'pagination-tipos-quarto', meta,
            (p) => { window.__paginationState[stateKey] = p; carregarTiposQuarto(); });
    } catch (e) {
        console.error(e);
    }
}
async function carregarQuartos() {
    try {
        const stateKey = 'quartos';
        const current = window.__paginationState[stateKey] || 1;
        const { items: quartos, meta } = await fetchPaginated('/quartos', current, 10);
        const tbody = document.querySelector('#table-quartos tbody');
        if (!tbody) return;
        tbody.innerHTML = '';
        quartos.forEach(q => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${q.numero_quarto}</td>
                <td>${q.tipo}</td>
                <td>${q.status_limpeza}</td>
                <td>${q.localizacao || ''}</td>
            `;
            tbody.appendChild(tr);
        });
        attachPaginationToTable('table-quartos', 'pagination-quartos', meta,
            (p) => { window.__paginationState[stateKey] = p; carregarQuartos(); });
    } catch (e) {
        console.error(e);
    }
}
async function carregarHospedes() {
    try {
        const stateKey = 'hospedes';
        const current = window.__paginationState[stateKey] || 1;
        const { items: hs, meta } = await fetchPaginated('/hospedes', current, 10);
        const tbody = document.querySelector('#table-hospedes tbody');
        if (!tbody) return;
        tbody.innerHTML = '';
        hs.forEach(h => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${h.id_hospede}</td>
                <td>${h.nome_completo}</td>
                <td>${h.documento}</td>
                <td>${h.telefone || ''}</td>
                <td>${h.email || ''}</td>
            `;
            tbody.appendChild(tr);
        });
        attachPaginationToTable('table-hospedes', 'pagination-hospedes', meta,
            (p) => { window.__paginationState[stateKey] = p; carregarHospedes(); });
    } catch (e) {
        console.error(e);
    }
}
async function carregarReservas() {
    try {
        const stateKey = 'reservas';
        const current = window.__paginationState[stateKey] || 1;
        const { items: reservas, meta } = await fetchPaginated('/reservas', current, 10);
        const tbody = document.querySelector('#table-reservas tbody');
        if (!tbody) return;
        tbody.innerHTML = '';
        reservas.forEach(r => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${r.id_reserva}</td>
                <td>${r.hospede ? r.hospede.nome_completo : ''}</td>
                <td>${r.numero_quarto || '—'}</td>
                <td>${r.data_checkin}</td>
                <td>${r.data_checkout}</td>
                <td>${r.status_reserva}</td>
                <td>R$ ${r.valor_total}</td>
            `;
            tbody.appendChild(tr);
        });
        attachPaginationToTable('table-reservas', 'pagination-reservas', meta,
            (p) => { window.__paginationState[stateKey] = p; carregarReservas(); });
    } catch (e) {
        console.error(e);
    }
}
async function carregarServicos() {
    try {
        const stateKey = 'servicos';
        const current = window.__paginationState[stateKey] || 1;
        const { items: serv, meta } = await fetchPaginated('/servicos', current, 10);
        const tbody = document.querySelector('#table-servicos tbody');
        if (!tbody) return;
        tbody.innerHTML = '';
        serv.forEach(s => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${s.id_servico}</td>
                <td>${s.nome_servico}</td>
                <td>R$ ${s.preco}</td>
            `;
            tbody.appendChild(tr);
        });
        attachPaginationToTable('table-servicos', 'pagination-servicos', meta,
            (p) => { window.__paginationState[stateKey] = p; carregarServicos(); });
    } catch (e) {
        console.error(e);
    }
}
async function carregarFaturas() {
    try {
        const stateKey = 'faturas';
        const current = window.__paginationState[stateKey] || 1;
        const { items: fs, meta } = await fetchPaginated('/faturas', current, 10);
        const tbody = document.querySelector('#table-faturas tbody');
        if (!tbody) return;
        tbody.innerHTML = '';
        fs.forEach(f => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${f.id_fatura}</td>
                <td>${f.id_reserva}</td>
                <td>R$ ${f.valor_diarias}</td>
                <td>R$ ${f.valor_servicos}</td>
                <td>${f.status_pagamento}</td>
                <td><a href="/fatura_page/${f.id_fatura}">Ver</a></td>
            `;
            tbody.appendChild(tr);
        });
        attachPaginationToTable('table-faturas', 'pagination-faturas', meta,
            (p) => { window.__paginationState[stateKey] = p; carregarFaturas(); });
    } catch (e) {
        console.error(e);
    }
}
async function carregarFaturaDetalhe(id) {
    try {
        const f = await apiGet(`/faturas/${id}`);
        const container = document.getElementById('fatura-detalhe');
        if (!container) return;
        container.innerHTML = `
            <h3>Fatura #${f.id_fatura}</h3>
            <p>Reserva: ${f.id_reserva}</p>
            <p>Valor diárias: R$ ${f.valor_diarias}</p>
            <p>Valor serviços: R$ ${f.valor_servicos}</p>
            <p>Total: R$ ${Number(f.valor_diarias) + Number(f.valor_servicos)}</p>
        `;
    } catch (e) {
        console.error(e);
    }
}
window.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('lista-perfis'))
        carregarPerfis();
    if (document.getElementById('table-usuarios'))
        carregarUsuarios();
    if (document.getElementById('table-tipos-quarto'))
        carregarTiposQuarto();
    if (document.getElementById('table-quartos'))
        carregarQuartos();
    if (document.getElementById('table-hospedes'))
        carregarHospedes();
    if (document.getElementById('table-reservas'))
        carregarReservas();
    if (document.getElementById('table-servicos'))
        carregarServicos();
    if (document.getElementById('table-faturas'))
        carregarFaturas();
    const faturaContainer = document.getElementById('fatura-detalhe');
    if (faturaContainer) {
        const id = faturaContainer.getAttribute('data-id');
        carregarFaturaDetalhe(id);
    }
});
