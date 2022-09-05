
problemas=['1 + 2', '1 - 9380']
def Errores(num1,num2,operator):
# Si contiene letras
    try:
        int(num1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(num2)
    except:
        return "Error: Numbers must only contain digits."
# Mas de 4 digitos 
    try:
        if len(num1)>4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    try:
        if len(num2)>4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
# Multiplicacion y division
    try:
        if operator!="+" and operator!="-":
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return "Sin problemas"
            
def arithmetic_arranger(problemas,valor=False):
    primera_iteracion=True
    linea1=linea2=linea3=linea4=""
    if len(problemas)>5:
        try:
            raise BaseException
        except:
            return "Error: Too many problems."

    for problema in problemas:
        num1=problema.split()[0]
        num2=problema.split()[2]
        operador=problema.split()[1]
        E=Errores(num1,num2,operador)
        if E!="Sin problemas":
            return E
        espacio_necesario=max(len(num1),len(num2))
        if primera_iteracion==True:
            linea1+=num1.rjust(espacio_necesario+2)
            linea2+=operador + ' ' + num2.rjust(espacio_necesario)
            linea3+=("-"*(espacio_necesario+2))
            if operador=="+":
                resultado=int(num1)+int(num2)
            else:
                resultado=int(num1)-int(num2)
            linea4+=str(resultado).rjust(espacio_necesario+2)
            primera_iteracion=False
        else:
            linea1+=num1.rjust(espacio_necesario+6)
            linea2+=operador.rjust(5) + ' ' + num2.rjust(espacio_necesario)
            linea3+=(4*" ")+ "-"*(espacio_necesario+2)
            if operador=="+":
                resultado=int(num1)+int(num2)
            else:
                resultado=int(num1)-int(num2)
            linea4+=(4*" ")+str(resultado).rjust(espacio_necesario+2)
    if valor==True:
        return linea1 +'\n'+linea2+"\n"+linea3+"\n"+linea4
    else:
         return linea1+"\n"+linea2+"\n"+linea3

print(arithmetic_arranger(problemas,True))
