from .._consts  import WINDOW_HEIGHT, WINDOW_WIDTH

style_settings = {
    'page-width': WINDOW_WIDTH,
    'page-height': WINDOW_HEIGHT,
    'border-radius': 5,
    'fill-background': '#1D1D1D',
    'fill-primary': '#292929',
    'fill-secondary': '#3E3E3E',
    'fill-secondary-highlight': '#4d4c4c',
    'fill-text-primary': '#FFFFFF',
    'fill-text-secondary': '#B7B7B7',
    'fill-button': '#535977',
    'fill-button-highlight': '#8390D1',
    'fill-pago': '#6FC043',
    'fill-pendente': '#C6C148',
    'fill-atrasado': '#BC604A',
    'fill-line': '#5A5A5A',
    'box': ' border: none; border-radius: %(border-radius)s; padding: 10; background-color: %(fill-primary)s; ',
    'box-secondary': ' %(box)s background-color: %(fill-secondary)s; ',
    'button': ' %(box)s background-color: %(fill-button)s; padding: 5 10; ',
    'button-icon': ' padding: 0; ',
    'button-hover': ' background-color: %(fill-button-highlight)s; ',
}

def parserStyle(style:str) -> str:
    while '%(' in style:
        style = style % style_settings
    
    return style

style_global = parserStyle("""

QLineEdit, QComboBox, QDoubleSpinBox { %(box-secondary)s }
                           
QComboBox::drop-down {
    image: url(:/root/icons/Chevron down.png);
    subcontrol-origin: padding;
    subcontrol-position: center right;
    margin-right: 2.5px;
}

QDoubleSpinBox {
    padding-left: 0;
}

QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
    subcontrol-origin: border;

    margin-right: 10px;
    border: none;
}

QDoubleSpinBox::up-button {
    subcontrol-position: top right;
}

QDoubleSpinBox::down-button {
    subcontrol-position: bottom right;
}
                           
/* QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover { background-color: red; } */
                           
QDoubleSpinBox::up-arrow {
    image: url(:/root/icons/Chevron up.png);                 
}

QDoubleSpinBox::down-arrow {
    image: url(:/root/icons/Chevron down.png);                 
}

QLineEdit::hover, QLineEdit::focus { background-color: %(fill-secondary-highlight)s; }

QPushButton { %(button-icon)s }
""")
