import { showNotification } from "../tools.js";
import FinancesApi from "../api.js";

$(() => {
    let newAccount = new NewAccountView();
    newAccount.initialize();
});

export default class NewAccountView {
    #api;
    #btnCriarId = '#btn-criar';

    constructor() {
        $(this.#btnCriarId).on("click", () => this.#on_btnCriar_clicked());
    }
    
    async initialize() {
        if(globalThis.financesApi == undefined) {
            let api = new FinancesApi();
            await api.initialize();

            globalThis.financesApi = api;
        }
    
        this.#api = globalThis.financesApi;
    }

    async #on_btnCriar_clicked() {
        let
            inputs = {
                first_name: '#first-name',
                last_name: '#last-name',
                username: '#username',
                email: '#email'
            },
            data = {},
            success = true,
            password = $('#password').val();
        
        if(password != $('#password-confirm').val()) {
            showNotification("as senhas não coincidem!");
            return;
        }

        if(password.length < 4) {
            showNotification("sua senha deve conter, no mínimo, 4 caracteres!");
            return;
        }

        Object.entries(inputs).forEach(([k, v]) => {
            let val = $(v).val();
            if(!val) {
                showNotification("preencha todos os campos!");
                success = false;
                return;
            }

            data[k] = val;
        });

        data.password = password;

        $(this.#btnCriarId).prop('disabled', true);
        success = await this.#api.newUser(data);
        $(this.#btnCriarId).prop('disabled', false);
        
        if(success) {
            window.location.href = "/login";
        }
    }
}