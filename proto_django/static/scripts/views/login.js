import { getCookieValue } from "../tools.js";

$(() => {
    let login = new LoginView();
    login.initialize();
});

export default class LoginView {
    #token = '';

    constructor() {
        $('#btn-acessar').on("click", () => this.#on_btnAcessar_clicked());
    }
    
    initialize() {
        $.get('/auth/token')
            .done(() => {
                this.#token = getCookieValue('csrftoken');
            });
    }

    #on_btnAcessar_clicked() {
        let request = {
            url: '/auth/auth',
            data: {
                username: $('#username').val(),
                password: $('#password').val(),
            },
            headers: {
                'X-CSRFToken': this.#token,
            }
        };

        $.post(request)
            .done(() => this.#on_loginSuccess())
            .fail((r) => this.#on_loginFail(r));
    }

    #on_loginSuccess() {
        window.location.href = "/home";
    }

    #on_loginFail(response) {
        console.log(response.responseText);
    }
}