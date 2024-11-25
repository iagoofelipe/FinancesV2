import FinancesApi from "../api.js";

$(() => {
    let view = new HomeView();
    view.initialize();
});

export default class HomeView {
    #api;

    constructor() {
    }

    async initialize() {
        if(globalThis.financesApi == undefined) {
            let api = new FinancesApi();
            await api.initialize();

            globalThis.financesApi = api;
        }

        this.#api = globalThis.financesApi;

        $('#btn-logout').on('click', () => this.#api.logout());
        console.log('initialization finished');
    }
}