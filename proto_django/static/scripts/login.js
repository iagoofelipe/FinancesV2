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
            },
            success: (data) => {
                console.log(data);
            }
        };

        $.post(request)
            .done(function (data) {
                console.log("done", data);
            })
            .fail(function (data) {
                console.log("error", data);
            })
            .always(function (data) {
                console.log("finished", data);
            });

        // console.log(data);
        // let result = await $.post('/auth', data);
        // console.log(result);
    }
}