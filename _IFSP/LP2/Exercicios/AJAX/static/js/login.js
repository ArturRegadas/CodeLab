document.addEventListener("DOMContentLoaded", () => {

    const formLogin = document.getElementById("formLogin");
    const resLogin = document.getElementById("resLogin");

    formLogin.addEventListener("submit", async (e) => {
        e.preventDefault();

        const data = {
            email: document.getElementById("log_email").value.trim(),
            password: document.getElementById("log_password").value.trim()
        };

        if (!data.email || !data.password) {
            resLogin.innerHTML = "Preencha todos os campos.";
            return;
        }

        const req = await fetch("/api/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const json = await req.json();
        resLogin.innerHTML = json.message;

        if (json.status === "success") {
            window.location.href = json.redirect;
        }
    });

});
