simbolos ={"M":1000, "D":500, "C":100,"L":50, "X":10, "V":5,"I":1}

def romano_a_entero(romano):
    if romano in simbolos:
        return simbolos[romano]
    elif insistance(romano,str):
        raise ValueError(f"simbolo {romano}no permitido")
    else:
        raise ValueError (f"parametro {romano} debe se un string")
