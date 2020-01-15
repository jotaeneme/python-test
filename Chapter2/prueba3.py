numero = int(input("Escriba un número: "))
if numero % 2 == 0 and numero % 4 != 0:
    print(f"{numero} es múltiplo de dos")
elif numero % 4 == 0:
    print(f"{numero} es múltiplo de cuatro y de dos")
else:
    print(f"{numero} no es múltiplo de dos")

#####################################################################
#####################################################################

#  Hay que prestar atención en el if: Tenemos dos escenarios donde está el and, esto nos indica que el número introducido debe ser true y true si queremos que ejecute la primera, si no en el elif se cumplirá también la primera y solo ejecutará esta



#####