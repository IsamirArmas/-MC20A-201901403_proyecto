
def evaluar_notacion_polaca(expresion):
    pila = []
    operadores = {'+', '-', '*', '/'}
    elementos = expresion.split()
    
    for elemento in elementos:
        if elemento not in operadores:
            pila.append(elemento)
        else:
            operando2 = pila.pop()
            operando1 = pila.pop()
            resultado = eval(f'{operando1} {elemento} {operando2}')
            pila.append(str(resultado))
    
    return float(pila[0])

expresion1 = "3 4 +"
expresion2 = "5 2 * 8 +"
expresion3 = "7 3 / 2 *"

resultado1 = evaluar_notacion_polaca(expresion1)
resultado2 = evaluar_notacion_polaca(expresion2)
resultado3 = evaluar_notacion_polaca(expresion3)

resultado1, resultado2, resultado3