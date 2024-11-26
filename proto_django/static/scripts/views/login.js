import { showNotification } from "../tools.js";
import FinancesApi from "../api.js";

$(() => {
    let login = new LoginView();
    login.initialize();
});

export default class LoginView {
    #api;

    constructor() {
        $('#btn-acessar').on("click", () => this.#on_btnAcessar_clicked());
    }
    
    async initialize() {
        if(globalThis.financesApi == undefined) {
            let api = new FinancesApi();
            await api.initialize();

            globalThis.financesApi = api;
        }
    
        this.#api = globalThis.financesApi;
    }

    async #on_btnAcessar_clicked() {
        let username = $('#username').val();
        let password = $('#password').val();

        if(!username || !password) {
            showNotification("preencha todos os campos!");
            return;
        }

        if(await this.#api.authenticate($('#username').val(), $('#password').val())) {
            window.location.href = "/home";
        }
    }
}