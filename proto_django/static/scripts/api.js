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
            showNotification(
                [400, 405, 406].includes(r.status)? r.responseJSON.msg : "um erro inesperado ocorreu durante a autenticação"
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
            showNotification(
                ([400, 401].includes(r.status))? r.responseJSON.msg : 'um erro ocorreu durante o cadastro do novo registro'
            );
        }

        return { success: success, response: response }
    }

    async newUser(data) {
        let
            success = false,
            request = {
                url: '/api/auth/newUser',
                data: data,
                headers: {
                    'X-CSRFToken': this.#token
                }
            };

        try {
            await $.post(request)
                .done(() => {
                    success = true;
                });

        } catch (r) {
            showNotification(
                ([400, 422, 405].includes(r.status))? r.responseJSON.msg : 'um erro ocorreu durante o cadastro do novo registro'
            );
        }

        return success;
    }
}