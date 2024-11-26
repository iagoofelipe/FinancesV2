export const groupFields = {
    NEW_REGISTRY: {
        preffix: 'new-reg',
        fields: {
            inout: {
                required: true,
                default: 0
            },
            title: {
                required: true,
                default: 'novo registro'
            },
            value: {
                required: true,
                default: 0.01
            },
            description: {
                required: false
            }
        }
    }
};

export const navProps = {
    REGISTRIES: {
        boxNavId: 'box-reg',
        containerId: 'container-reg'
    },
    DASHBOARDS: {
        boxNavId: 'box-dash',
        containerId: 'container-dash'
    }
};