import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
import re

gramar_for_var = {
    "U": r"UwU-int|UwU-string|UwU-float",
    "DU": r"[a-z][a-z]*",
    "II": r"=",
}

def automata_pila_for_var(variables):
    variables = variables.split()
    steps = []

    tipo_dato = re.match(gramar_for_var["U"], variables[0])
    if tipo_dato and tipo_dato.group() == 'UwU-int':
        gramar_for_var["Int"] = r"[0-9]+"
    elif tipo_dato and tipo_dato.group() == 'UwU-string':
        gramar_for_var["String"] = r"[a-zA-Z]+"
    elif tipo_dato and tipo_dato.group() == 'UwU-float':
        gramar_for_var["Float"] = r"[0-9]+\.[0-9]+"
    else:
        return False, steps

    pila = list(gramar_for_var.keys()) 
    steps.append(pila.copy()) 

    while pila and variables:
        x_p = pila[0]
        x_v = variables[0]

        if re.match(gramar_for_var[x_p], x_v):
            pila.pop(0)
            variables.pop(0)
            if pila:
                steps.append(pila.copy())

        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

gramar_for_if = {
    "U": r"UwU-if",
    "COV": r"[a-z][a-z]*",
    "SG": r"==|!=|<|>|<=|>=",
    "NU": r"[0-9]+|\"[a-zA-Z]+\"",
    "DS": r":",
    "R": r"c",
    "EL": r"UwU-else",
    "DS2": r":",
    "R2": r"c",
}

def automata_pila_for_if(cadena):
    cadena = cadena.split()
    steps = []

    pila = list(gramar_for_if.keys())
    steps.append(pila.copy())

    while pila and cadena:
        x_p = pila[0]
        x_v = cadena[0]

        if re.match(gramar_for_if[x_p], x_v):
            pila.pop(0)
            cadena.pop(0)
            if pila:
                steps.append(pila.copy())

        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

gramar_for_for = {
    "U": r"UwU-for",
    "COV": r"[a-z][a-z]*",
    "II": r"=",
    "N": r"[0-9]+|[a-z]+",
    "PC": r";",
    "COV2": r"[a-z][a-z]*",
    "SIG": r"==|!=|<|>|<=|>=",
    "N2": r"[0-9]+|[a-z]+",
    "PC2": r";",
    "COV3": r"[a-z][a-z]*",
    "OP": r"\+\+|--",
    "DS": r":",
    "R": r"c",
}

def automata_pila_for_for(cadena):
    cadena = cadena.split()
    steps = []

    pila = list(gramar_for_for.keys())
    steps.append(pila.copy())

    while pila and cadena:
        x_p = pila[0]
        x_v = cadena[0]

        if re.match(gramar_for_for[x_p], x_v):
            pila.pop(0)
            cadena.pop(0)
            if pila:
                steps.append(pila.copy())

        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

gramar_for_print = {
    "U": r"UwU-print",
    "II": r"=",
    "N": r"[a-z]+|\"[a-zA-Z]+\"",
}

def automata_pila_for_print(cadena):
    cadena = cadena.split()
    steps = []

    pila = list(gramar_for_print.keys())
    steps.append(pila.copy())

    while pila and cadena:
        x_p = pila[0]
        x_v = cadena[0]

        if re.match(gramar_for_print[x_p], x_v):
            pila.pop(0)
            cadena.pop(0)
            if pila:
                steps.append(pila.copy())

        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

gramar_for_def = {
    "U": r"UwU-def",
    "FU": r"[a-z][a-z]*",
    "PA": r"\(\)",
}

def automata_pila_for_def(cadena):
    cadena = cadena.split()
    steps = []

    pila = list(gramar_for_def.keys())
    steps.append(pila.copy())

    while pila and cadena:
        x_p = pila[0]
        x_v = cadena[0]

        if re.match(gramar_for_def[x_p], x_v):
            pila.pop(0)
            cadena.pop(0)
            if pila:
                steps.append(pila.copy())

        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

class GrammarParserApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Gramatica verificador')
        self.setGeometry(50, 50, 600, 400)

        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText("Ingresa aqui")

        self.result_label = QLabel(self)
        self.steps_text = QTextEdit(self)
        self.steps_text.setReadOnly(True)

        self.parse_button = QPushButton('Verificar', self)
        self.parse_button.clicked.connect(self.parse_input)

        layout = QVBoxLayout()
        layout.addWidget(self.input_text)
        layout.addWidget(self.result_label)
        layout.addWidget(self.steps_text)
        layout.addWidget(self.parse_button)

        self.setLayout(layout)

    def parse_input(self):
        input_string = self.input_text.toPlainText()
        result, steps = self.parse_input_string(input_string)

        self.result_label.setText(f"Resutados: {result}")
        self.steps_text.setPlainText(f"Pasos:\n{', '.join(map(str, steps))}")

    def parse_input_string(self, input_string):
        if input_string.startswith("UwU-int") or input_string.startswith("UwU-string") or input_string.startswith("UwU-float"):
            return automata_pila_for_var(input_string)
        elif input_string.startswith("UwU-if"):
            return automata_pila_for_if(input_string)
        elif input_string.startswith("UwU-for"):
            return automata_pila_for_for(input_string)
        elif input_string.startswith("UwU-print"):
            return automata_pila_for_print(input_string)
        elif input_string.startswith("UwU-def"):
            return automata_pila_for_def(input_string)
        else:
            return False, []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    parser_app = GrammarParserApp()
    parser_app.show()
    sys.exit(app.exec_())
