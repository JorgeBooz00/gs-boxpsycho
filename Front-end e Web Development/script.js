const form = document.querySelector("#form");
const username = document.querySelector("#username");
const email = document.querySelector("#email");
const mensagem = document.querySelector("#mensagem");

const linkFiap = "https://www.fiap.com.br/"
const ancoraFiap = document.querySelector("#fiap")

const linkJorge = "https://www.github.com/JorgeBooz00"
const ancoraJorge = document.querySelector("#jorge")
const botaoJorge = document.querySelector("#jorge-btn")

const linkMateus = "https://github.com/MateusTibao"
const ancoraMateus = document.querySelector("#mateus")
const botaoMateus = document.querySelector("#mateus-btn")

const linkHapvida = "https://www.hapvida.com.br/site/"
const ancoraHapvida = document.querySelector("#hapvida")

const linkNotredame = "https://www.gndi.com.br/"
const ancoraNotredame = document.querySelector("#notredame")

const esconder = document.querySelector("#esconder-mostrar")
const paragrafo = document.querySelector(".fake")

    esconder.addEventListener('click', ()=>{

        if(paragrafo.style.display=== 'none'){
            paragrafo.style.display = 'inherit'
        }else{
            paragrafo.style.display = 'none'
        }
    })

    // Função que abre um link em uma nova guia
    function openInNewTab(url){
        const janela = window.open(url, '_blank')
        janela.focus()
    }
    // Evento de clique para abrir o link da Fiap e sucessivamente
    ancoraFiap.addEventListener('click', () => {
        openInNewTab(linkFiap)
    })
    ancoraJorge.addEventListener('click', () => {
        openInNewTab(linkJorge)
    })
    botaoJorge.addEventListener('click', () => {
        openInNewTab(linkJorge)
    })
    ancoraMateus.addEventListener('click', () => {
        openInNewTab(linkMateus)
    })
    botaoMateus.addEventListener('click', () => {
        openInNewTab(linkMateus)
    })
    ancoraHapvida.addEventListener('click', () => {
        openInNewTab(linkHapvida)
    })
    ancoraNotredame.addEventListener('click', () => {
        openInNewTab(linkNotredame)
    })

    //Evento de envio do formulário
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        checkForm();
    });

    //Evento de desfoco do campo de nome e sucessivamente
    username.addEventListener("blur", () => {
        checkUsername();
    });

    email.addEventListener("blur", () => {
        checkEmail();
    });

    //Função para checar se o campo de nome está preenchido
    function checkUsername() {
        const usernameValue = username.value;
        if (usernameValue === "") {
            errorInput(username, "Por favor, digite seu nome");
        } else {
            const formItem = username.parentElement;
            formItem.className = "form-content";
        }
    }

    //Função para checar se o campo de e-mail está preenchido
    function checkEmail() {
        const emailValue = email.value;
        if (emailValue === "") {
            errorInput(email, "Por favor, um e-mail válido");
        } else {
            const formItem = email.parentElement;
            formItem.className = "form-content";
        }
    }

    // Função para verificar todo o formulário
    function checkForm(){
        checkUsername();
        checkEmail();

        const formItems = form.querySelectorAll(".form-content");

        const isValid = [...formItems].every((item) => {
            return item.className === "form-content";
        });

        if (isValid) {
            alert("Obrigado pelo feedback");
            clearForm();
        }
    }
    
    // Função para exibir erro em um campo "fake single page"
    function errorInput(input, message) {
        const formItem = input.parentElement;
        const textMessage = formItem.querySelector("a");

        textMessage.innerText = message;

        formItem.className = "form-content error";
    }
    
    //Função para limpar o formulario
    function clearForm() {
        username.value = "";
        email.value = "";
        mensagem.value = "";

        clearError(username);
        clearError(email);
        clearError(mensagem);
    }
    function clearError(input) {
        const formItem = input.parentElement;
        const textMessage = formItem.querySelector("a");

        if (textMessage) {
            textMessage.innerText = "";
        }

        formItem.className = "form-content";
    }