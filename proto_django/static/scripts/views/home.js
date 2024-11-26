import FinancesApi from "../api.js";
import { showNotification } from "../tools.js";

$(() => {
    let view = new HomeView();
    view.initialize();
});

export default class HomeView {
    #currentTabId = '';

    constructor() {
    }

    async initialize() {
        if(globalThis.financesApi == undefined) {
            let api = new FinancesApi();
            await api.initialize();

            globalThis.financesApi = api;
        }

        // this.#api = globalThis.financesApi;
        
        // configurando eventos
        $('#box-dash').on('click', () => this.#replaceContent('dash'));
        $('#box-reg').on('click', () => this.#replaceContent('reg'));
        $('#box-card').on('click', () => this.#replaceContent('card'));
        $('#box-settings').on('click', () => this.#replaceContent('settings'));

        $('#box-reg').click();
    }

    async #replaceContent(op) {
        let
            old_id = this.#currentTabId,
            new_id = `#box-${op}`;

        this.#currentTabId = new_id;
        
        $(old_id).removeClass('box-element-clickable-focus');
        $(new_id).addClass('box-element-clickable-focus');

        await $.get(`/home/${op}`)
            .done((r) => {
                $('#container-center').remove();
                $(r).appendTo('body .content');
            });
    }

    async newRegistryRequired() {

    }
}