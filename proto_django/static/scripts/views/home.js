import FinancesApi from "../api.js";
import { showNotification } from "../tools.js";
import { groupFields } from "../consts.js";

/*
TODO: configurar navProps para um conteúdo mais dinâmico
*/

$(() => {
    let view = new HomeView();
    view.initialize();
});

export default class HomeView {
    #api;
    #currentTabId = '';
    #currentContainerId = '';

    constructor() {
    }

    async initialize() {
        if(globalThis.financesApi == undefined) {
            let api = new FinancesApi();
            await api.initialize();

            globalThis.financesApi = api;
        }

        this.#api = globalThis.financesApi;

        // eventos - topbar
        $('#btn-logout').on('click', () => this.#api.logout());
        
        // eventos - navbar
        $('#box-dash').on('click', () => this.#replaceContent('dash'));
        $('#box-reg').on('click', () => this.#replaceContent('reg'));
        $('#box-card').on('click', () => this.#replaceContent('card'));
        $('#box-settings').on('click', () => this.#replaceContent('settings'));

        // alterando para aba principal
        $('#box-reg').click();
    }

    async #replaceContent(op) {
        // navbar
        let
            old_id = this.#currentTabId,
            new_id = `#box-${op}`,
            old_container_id = this.#currentContainerId,
            new_container_id = `#container-${op}`;

        this.#currentTabId = new_id;
        this.#currentContainerId = new_container_id;
        
        $(old_id).removeClass('box-element-clickable-focus');
        $(new_id).addClass('box-element-clickable-focus');

        // conteúdo
        
        await $.get(`/home/${op}`)
        .done((html) => {
                $(old_container_id).remove();
                $(html).appendTo('body .content');
            });

        // eventos
        switch (op) {
            case 'reg':
                this.#configReg();
                break;
        
            default:
                break;
        }
    }

    #configReg() {
        $('#btn-new-limpar').on('click', () => this.resetGroupInputs(groupFields.NEW_REGISTRY));
        $('#btn-new-salvar').on('click', () => this.newRegistryRequired());

        this.resetGroupInputs(groupFields.NEW_REGISTRY);
    }

    async newRegistryRequired() {
        let
            group = groupFields.NEW_REGISTRY,
            data = this.getGroupData(group);

        if(data == undefined) {
            return;
        }

        // removendo marcação de campos obrigatórios
        this.resetGroupInputs(group, true);
        $('#btn-new-salvar').prop('disabled', true);
        $('#btn-new-limpar').prop('disabled', true);

        // enviando requisição
        let result = await this.#api.newRegistry(data);
        if(result.success) {
            showNotification('registro cadastrado com sucesso!');
            this.resetGroupInputs(group);
        }

        $('#btn-new-salvar').prop('disabled', false);
        $('#btn-new-limpar').prop('disabled', false);
    }

    resetGroupInputs(group, keepValue=false) {
        Object.entries(group.fields).forEach(([field, prop]) => {
            let obj = $(`#inp-${group.preffix}-${field}`);
            obj.removeClass('inp-required');

            if(!keepValue)
                obj.val(prop.default?? '');
        });
    }

    getGroupData(group, checkRequired=true) {
        let inp, val,
            any_required = false,
            data = {};

        Object.entries(group.fields).forEach(([field, prop]) => {
            inp = $(`#inp-${group.preffix}-${field}`);
            val = inp.val();

            // verificando campos obrigatórios
            if(!val && checkRequired && prop.required) {
                inp.addClass('inp-required');
                any_required = true;
                return;
            }

            data[field] = val;
        });

        if(!any_required) {
            return data;
        }
        
        showNotification('preencha todos os campos obrigatórios!');
    }

    // getNewRegData(checkRequired=true) {
    //     let inp, val;
    //     let any_required = false;
    //     let data = {};

    //     groupFields.NEW_REGISTRY.forEach((field, prop) => {
    //         inp = $(`#inp-new-${field}`);
    //         val = inp.val();

    //         // verificando campos obrigatórios
    //         if(!val && checkRequired && prop.required) {
    //             inp.addClass('inp-required');
    //             any_required = true;
    //             return;
    //         }

    //         data[field] = val;
    //     });

    //     // this.#inputs_new.forEach(v => {
    //     //     inp = $(`#inp-new-${v}`);
    //     //     val = inp.val();
    //     //     required = this.#inputs_new_requireds.includes(v);

    //     //     // verificando campos obrigatórios
    //     //     if(!val && checkRequired && required) {
    //     //         inp.addClass('inp-required');
    //     //         any_required = true;
    //     //         return;
    //     //     }
            
    //     //     data[v] = val;
    //     // });
        
    //     if(any_required) {
    //         showNotification('preencha todos os campos obrigatórios!');
    //     }
        
    //     return any_required? undefined : data;
    // }
}