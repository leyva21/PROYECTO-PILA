import tkinter as tk
from tkinter import scrolledtext
import re

gramar_for_var = {
    "U": r"\b(UwU-int|UwU-string|UwU-float)\b",
    "DU": r"[a-z][a-z]*",
    "II": r"=",
}

def automata_pila_for_var(variables):
    var = variables.split()
    steps = []
    
    tipo_dato = re.match(gramar_for_var["U"], var[0])
    if tipo_dato is None or tipo_dato.group() != 'UwU-int' and tipo_dato.group() != 'UwU-string' and tipo_dato.group() != 'UwU-float':
        return False, steps

    if tipo_dato.group() == 'UwU-int':
        gramar_for_var["Int"] = r"\b[0-9]+\b"
    elif tipo_dato.group() == 'UwU-string':
        gramar_for_var["String"] = r"\"[a-zA-Z]+\""
    elif tipo_dato.group() == 'UwU-float':
        gramar_for_var["Float"] = r"[0-9]+\.[0-9]+"
    else:
        return False, steps
    
    pila = list(gramar_for_var.keys()) 
    steps.append(pila.copy()) 
    print(pila)

    while pila and var:
        x_p = pila[0]
        x_v = var[0]

        if re.match(gramar_for_var[x_p], x_v):
            pila.pop(0)
            var.pop(0)
            if pila:
                steps.append(pila.copy())
            
            print(f"Pila después de hacer pop: {pila}")
        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    if tipo_dato == 'UwU-int':
        gramar_for_var.pop("Int")
    elif tipo_dato == 'UwU-string':
        gramar_for_var.pop("String")
    elif tipo_dato == 'UwU-float':
        gramar_for_var.pop("Float")
    return True, steps

gramar_for_if = {
    "U": r"\b(UwU-if)\b",
    "COV": r"[a-z][a-z]*",
    "SG": r"==|!=|<|>|<=|>=",
    "NU": r"[0-9]+|\"[a-zA-Z]+\"",
    "DS": r":",
    "R": r"c",
    "EL": r"\b(UwU-else)\b",
    "DS2": r":",
    "R2": r"c",
}

def automata_pila_for_if(cadena):
    cadena = cadena.split()
    steps = []

    pila = list(gramar_for_if.keys())
    steps.append(pila.copy())
    print(pila)

    while pila and cadena:
        x_p = pila[0]
        x_v = cadena[0]

        if re.match(gramar_for_if[x_p], x_v):
            pila.pop(0)
            cadena.pop(0)
            if pila:
                steps.append(pila.copy())
            print(f"Pila después de hacer pop: {pila}")
        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

gramar_for_for = {
    "U": r"\b(UwU-for)\b",
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
    print(pila)

    while pila:
        x_p = pila[0]
        print(x_p)
        x_v = cadena[0]
        print(x_v)

        if re.match(gramar_for_for[x_p], x_v):
            print(gramar_for_for[x_p], x_v)
            pila.pop(0)
            cadena.pop(0)
            if pila:
                steps.append(pila.copy())
            print(f"Pila después de hacer pop: {pila}")
        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

gramar_for_print = {
    "U": r"\b(UwU-print)\b",
    "II": r"=",
    "N": r"[a-z]+|\"[a-zA-Z]+\"",
}

def automata_pila_for_print(cadena):
    cadena = cadena.split()
    steps = []

    pila = list(gramar_for_print.keys())
    steps.append(pila.copy())
    print(pila)

    while pila and cadena:
        x_p = pila[0]
        x_v = cadena[0]

        if re.match(gramar_for_print[x_p], x_v):
            pila.pop(0)
            cadena.pop(0)
            if pila:
                steps.append(pila.copy())
            print(f"Pila después de hacer pop: {pila}")
        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

gramar_for_def = {
    "U": r"\b(UwU-def)\b",
    "FU": r"[a-z][a-z]*",
    "PA": r"\(\)",
}

def automata_pila_for_def(cadena):
    cadena = cadena.split()
    steps = []

    pila = list(gramar_for_def.keys())
    steps.append(pila.copy())
    print(pila)

    while pila and cadena:
        x_p = pila[0]
        x_v = cadena[0]

        if re.match(gramar_for_def[x_p], x_v):
            pila.pop(0)
            cadena.pop(0)
            if pila:
                steps.append(pila.copy())
            print(f"Pila después de hacer pop: {pila}")
        else:
            return False, steps

    if not pila:
        steps.append(pila.copy())

    return True, steps

def evaluar_tipo_cadena(cadena):
    palabraReservada = cadena.split()[0]

    if palabraReservada == "UwU-int":
        #tipo_cadena = "Variable"
        resultado, steps = automata_pila_for_var(cadena)
    elif palabraReservada == "UwU-string":
        #tipo_cadena = "Variable"
        resultado, steps = automata_pila_for_var(cadena)
    elif palabraReservada == "UwU-float":
        #tipo_cadena = "Variable"
        resultado, steps = automata_pila_for_var(cadena)
    elif palabraReservada  == "UwU-def":
        #tipo_cadena = "Función"
        resultado, steps = automata_pila_for_def(cadena)
    elif palabraReservada  == "UwU-print":
        #tipo_cadena = "Imprimir"
        resultado, steps = automata_pila_for_print(cadena)
    elif palabraReservada  == "UwU-for":
        #tipo_cadena = "Ciclo"
        resultado, steps = automata_pila_for_for(cadena)
    elif palabraReservada  == "UwU-if":
        #tipo_cadena = "Condicional"
        resultado, steps = automata_pila_for_if(cadena)
    else:
        print ("Cadena inválida")
        return False, []
    
    return resultado, steps


def verificar_cadena():
    cadena = entrada.get("1.0", "end-1c")
    resultado, steps = evaluar_tipo_cadena(cadena)


    if resultado:
        resultado_text.config(text="La cadena es válida", fg="green")
    else:
        resultado_text.config(text="La cadena es inválida", fg="red")

    # Mostrar el procedimiento de la pila en el cuadro de texto
    procedimiento_text.config(state="normal")
    procedimiento_text.delete("1.0", "end")

    for step in steps:
        procedimiento_text.insert("end", " ".join(step) + "\n")

        if len(step) > 0:
            recorrido_pila = "Recorrido de la Pila: Pop '{}'".format(step[0])
            procedimiento_text.insert("end", recorrido_pila + "\n")

    procedimiento_text.config(state="disabled")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificador de Cadenas")

# Crear elementos de la interfaz
etiqueta = tk.Label(ventana, text="Ingrese la cadena:")
etiqueta.pack(pady=5)

entrada = scrolledtext.ScrolledText(ventana, width=50, height=3, wrap=tk.WORD)
entrada.pack(pady=10)

verificar_boton = tk.Button(ventana, text="Verificar", command=verificar_cadena)
verificar_boton.pack(pady=5)

resultado_text = tk.Label(ventana, text="", fg="black")
resultado_text.pack(pady=5)

procedimiento_text = scrolledtext.ScrolledText(ventana, width=50, height=10, wrap=tk.WORD, state="disabled")
procedimiento_text.pack(pady=10)

ventana.mainloop()
