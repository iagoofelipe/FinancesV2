$(() => {
    let view = new HomeView();
    view.initialize();
});

export default class HomeView {
    constructor() {

    }

    async initialize() {
        console.log('initialization finished');
    }
}