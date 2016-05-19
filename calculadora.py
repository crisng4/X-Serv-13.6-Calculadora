#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def suma(numero1,numero2):
    return numero1 + numero2

def resta(numero1,numero2):
    return numero1 - numero2

def mult(numero1,numero2):
    return numero1 * numero2

def div(numero1,numero2):
    if numero2 == 0:
        return "Dividir cualquier número entre 0 es una indeterminación"
    return numero1/numero2

if __name__ == "__main__":
    operacion = str(sys.argv[1])

    try:
        operando1 = float(sys.argv[2])
    except ValueError:
        print "Argumento inválido. Sólo se aceptan números\n"
        sys.exit()

    try:
        operando2 = float(sys.argv[3])
    except ValueError:
        print "Argumento inválido. Sólo se aceptan números\n"
        sys.exit()
    
    if operacion == "suma":
        print "Resultado de la suma: ", str(suma(operando1,operando2)), "\n" 
    elif operacion == "resta":
        print "Resultado de la resta: ", str(resta(operando1,operando2)), "\n" 
    elif operacion == "mult":
        print "Resultado de la multiplicación: ", str(mult(operando1,operando2)), "\n" 
    elif operacion == "div":
        print "Resultado de la división: ", str(div(operando1,operando2)), "\n" 
    else:
        print "Operacion inválida\n"
