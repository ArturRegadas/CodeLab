document.addEventListener("DOMContentLoaded", () => {

    const formCadastro = document.getElementById("formCadastro");
    const resCadastro = document.getElementById("resCadastro");

    formCadastro.addEventListener("submit", async (e) => {
        e.preventDefault();

        const data = {
            username: document.getElementById("cad_username").value.trim(),
            email: document.getElementById("cad_email").value.trim(),
            password: document.getElementById("cad_password").value.trim()
        };

        if (!data.username || !data.email || !data.password) {
            resCadastro.innerHTML = "Preencha todos os campos.";
            return;
        }

        const req = await fetch("/api/register", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const json = await req.json();
        resCadastro.innerHTML = json.message;
    });

});
