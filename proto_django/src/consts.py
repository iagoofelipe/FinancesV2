TYPE_INOUT_OUT = 0
TYPE_INOUT_IN = 1
TYPES_INOUT = {
    0: "Saída",
    1: "Entrada",
}

# Estruturas
{
    'NEW_REGISTRY': [
        {
            'title': 'Tipo',
            'name': 'inout',
            'description': 'Tipo de registro',
            'required': True,
            'default': 'Entrada',
            'options': [
                'Entrada', 'Saída'
            ]
        }
    ]
}