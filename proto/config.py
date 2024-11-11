WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 670

style_settings = {
    'page-width': WINDOW_WIDTH,
    'page-height': WINDOW_HEIGHT,
    'border-radius': 5,
    'fill-background': '#1D1D1D',
    'fill-primary': '#292929',
    'fill-secondary': '#3E3E3E',
    'fill-text-primary': '#FFFFFF',
    'fill-text-secondary': '#B7B7B7',
    'fill-button': '#535977',
    'fill-button-highlight': '#8390D1',
    'fill-pago': '#6FC043',
    'fill-pendente': '#C6C148',
    'fill-atrasado': '#BC604A',
    'fill-line': '#5A5A5A',
}

style_widget = """

QLineEdit, QPushButton {
    border: none;
    border-radius: %(border-radius)s;
    padding: 10;
}

QLineEdit {
    background-color: %(fill-primary)s;
}

QPushButton {
    background-color: %(fill-button)s;
}

QPushButton::hover {
    background-color: %(fill-button-highlight)s;
}

#Login {
    background-color: %(fill-background)s;
}

""" % style_settings