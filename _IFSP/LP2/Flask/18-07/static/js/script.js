function validEmail(email) {
    // Expressão regular mais robusta para validar e-mails comuns
    let regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

let forms = document.getElementById("forms");
let error = document.getElementById("error");

forms.addEventListener("submit", function(event){

    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    
    event.preventDefault();
    error.innerHTML="";

    let errors = [];

    username = username.trim();
    email = email.trim();
    password = password.trim();

    if(username === "")
        errors.push("campo username é obrigatorio");

    if(password === "")
        errors.push("campo password é obrigatorio")

    if(email === "")
        errors.push("campo email é obrigatorio");
    else if(!validEmail(email))
        errors.push("formato invalido para email");

    if(errors.length > 0){
        error.innerHTML = errors.join("<br>");
    }
    else{
        forms.submit();
    }

})