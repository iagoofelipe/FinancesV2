import { getCookieValue, showNotification } from "./tools.js";

export default class FinancesApi {
    #token = '';

    async initialize() {
        await $.get('/api/token')
            .done(() => {
                this.#token = getCookieValue('csrftoken');
            });
    }

    async authenticate(username, password) {
        let request = {
            url: '/api/auth',
            data: {
                username: username,
                password: password,
            },
            headers: {
                'X-CSRFToken': this.#token,
            }
        };
        
        let response = {
            success: true,
            server: {
                message: "",
            },
        };

        try {
            await $.post(request)
                .done((r) => {
                    response.server = r;
                });

        } catch (r) {
            response.success = false;

            switch (r.status) {
                case 403:
                    response.server.message = "senha ou usuário incorretos";
                    break;
            
                default:
                    response.server.message = `serverMessage: ${r.responseText}`;
                    break;
            }
        }

        return response;
    }

    async logout() {
        try {
            await $.get('/api/logout');
            window.location.href = '/login';
            return true;

        } catch (r) {
            showNotification('um erro ocorreu durante o log out');
            return false;
        }
    }
}