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
    return res.json();
}

async function apiPut(path, body) {
    const res = await fetch(path, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
        credentials: 'same-origin'
    });
    return res.json();
}

async function apiDelete(path) {
    const res = await fetch(path, { method: 'DELETE', credentials: 'same-origin' });
    return res.json();
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
        const users = await apiGet('/usuarios');
        const tbody = document.querySelector('#table-usuarios tbody');
        if (!tbody) return;

        tbody.innerHTML = '';
        users.forEach(u => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${u.id}</td>
                <td>${u.nome_completo}</td>
                <td>${u.email}</td>
                <td>${u.perfil ? u.perfil.nome_perfil : ''}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (e) {
        console.error(e);
    }
}


async function carregarTiposQuarto() {
    try {
        const tipos = await apiGet('/tipos_quarto');
        const tbody = document.querySelector('#table-tipos-quarto tbody');
        if (!tbody) return;

        tbody.innerHTML = '';
        tipos.forEach(t => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${t.id_tipo}</td>
                <td>${t.nome_tipo}</td>
                <td>${t.capacidade_maxima}</td>
                <td>${t.preco_diaria_base}</td>
                <td>${t.descricao || ''}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (e) {
        console.error(e);
    }
}


async function carregarQuartos() {
    try {
        const quartos = await apiGet('/quartos');
        const tbody = document.querySelector('#table-quartos tbody');
        if (!tbody) return;

        tbody.innerHTML = '';
        quartos.forEach(q => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${q.numero_quarto}</td>
                <td>${q.tipo?.nome_tipo || ''}</td>
                <td>${q.status_limpeza}</td>
                <td>${q.localizacao || ''}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (e) {
        console.error(e);
    }
}


async function carregarHospedes() {
    try {
        const hs = await apiGet('/hospedes');
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
    } catch (e) {
        console.error(e);
    }
}


async function carregarReservas() {
    try {
        const reservas = await apiGet('/reservas');
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
                <td>${r.valor_total}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (e) {
        console.error(e);
    }
}

async function carregarServicos() {
    try {
        const serv = await apiGet('/servicos');
        const tbody = document.querySelector('#table-servicos tbody');
        if (!tbody) return;

        tbody.innerHTML = '';
        serv.forEach(s => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${s.id_servico}</td>
                <td>${s.nome_servico}</td>
                <td>${s.preco}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (e) {
        console.error(e);
    }
}


async function carregarFaturas() {
    try {
        const fs = await apiGet('/faturas');
        const tbody = document.querySelector('#table-faturas tbody');
        if (!tbody) return;

        tbody.innerHTML = '';
        fs.forEach(f => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${f.id_fatura}</td>
                <td>${f.id_reserva}</td>
                <td>${f.valor_diarias}</td>
                <td>${f.valor_servicos}</td>
                <td>${f.status_pagamento}</td>
                <td><a href="/fatura_page/${f.id_fatura}">Ver</a></td>
            `;
            tbody.appendChild(tr);
        });
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
