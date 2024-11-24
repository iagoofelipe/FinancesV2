$(() => {
    let login = new LoginView();
});

function getCookieValue(name) {
    const regex = new RegExp(`(^| )${name}=([^;]+)`)
    const match = document.cookie.match(regex)
    if (match) {
        return match[2]
    }
}


export default class LoginView {
    constructor() {
        $('#btn-acessar').on("click", this.#on_btnAcessar_clicked);
    }

    #on_btnAcessar_clicked() {
        let request = {
            url: 'auth',
            data: {
                username: $('#username').val(),
                password: $('#password').val(),
            },
            headers: {
                'X-CSRFToken': getCookieValue('csrftoken'),
            }
        };

        // $.post(request)
        //     .done(function (data) {
        //         console.log("done", data);
        //     })
        //     .fail(function (data) {
        //         console.log("error", data);
        //     })
        //     .always(function (data) {
        //         console.log("finished", data);
        //     });

        $.post(request)
        .done(() => this.#on_loginSuccess())
        .fail(() => this.#on_loginFail());
    }

    #on_loginSuccess() {
        window.location.href = "home";
    }

    #on_loginFail(response) {
        console.log(response.responseText);
    }
}