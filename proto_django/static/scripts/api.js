import { getCookieValue, showNotification } from "./tools.js";

export default class FinancesApi {
    #token;

    async initialize() {
        console.log('api initializing');
        await $.get('/api/auth/token')
            .done(() => {
                this.#token = getCookieValue('csrftoken');
            });
    }

    async authenticate(username, password) {
        let
            success = true,
            request = {
            url: '/api/auth/login',
            data: {
                username: username,
                password: password,
            },
            headers: {
                'X-CSRFToken': this.#token
            }
        };

        try {
            await $.post(request);
        } catch (r) {
            success = false;
            let
                s = r.status,
                result = (s == 200 || s == 400 || s == 405 || s == 406);

            showNotification(
                result? r.responseJSON.msg : "um erro inesperado ocorreu durante a autenticação"
            );
        }

        return success;
    }

    async logout() {
        try {
            await $.get('/api/auth/logout');
            window.location.href = '/login';
            return true;

        } catch (r) {
            showNotification('um erro ocorreu durante o log out');
            return false;
        }
    }

    async newRegistry(data) {
        let
            response = undefined,
            success = false,
            request = {
                url: '/api/reg/new',
                data: data,
                headers: {
                    'X-CSRFToken': this.#token
                }
            };

        try {
            await $.post(request)
                .done((r) => {
                    response = r;
                    success = true;
                });

        } catch (r) {
            let s = r.status;

            showNotification(
                (s == 400 || s == 401)? r.responseJSON.msg : 'um erro ocorreu durante o cadastro do novo registro'
            );
        }

        return { success: success, response: response }
    }
}