$(() => {
    let login = new LoginView();
});


export default class LoginView {
    constructor() {
        $('#btn-acessar').on("click", this.#on_btnAcessar_clicked);
    }

    #on_btnAcessar_clicked() {
        let data = {
            username: $('#username').val(),
            password: $('#password').val(),
        };

        console.log(data);
    }
}