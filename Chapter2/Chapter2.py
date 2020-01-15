# En este paso vamos a hablar sobre los boolean values que solo puede tener dos tipos
# True o False

spam=True
spam

# También se nos muestran los operadores de comparación
42==42
# Nos indicará True 
42==41
# Nos indicará que es falso
2 != 3
# Not equal to !#
7 % 2
# Nos indicará el resto


#Comparaciones <, >, <=, >=


# Los operadores 'and' y 'or' son booleandos binarios


#              AND            #
# el operador and evalúa la expresion a True si ambas expresiones booleanas son True
True and True == True
True and False == False
False and False == False 

#             OR               #
# el operador or evalúa la expresion a True si una de ellas es True
True or True == True
True or False == True
False or False == False

#             NOT              #
# evalúa el booleano contrario al puesto
not True == False
not False == True
not not True == True
not not False == False



# Ejemplo

2+2==4 and not not 5*5==35



# If Else Elif
print('Escribe tu nombre')
nombre=input()
print ('Hola '+nombre)
print('Escribe tu contraseña')
contraseña=input()
if contraseña == '123': 
   print('Bienvenido')
else:
      print('Contraseña incorrecta')


#######################################################
#           ELIF nos da una situación más posible      #

edad=int(input("¿Cuantos años tienes? "))
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad < 18: 
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")

# Hay que prestar atención en el if: Tenemos dos escenarios donde está 
# el and, esto nos indica que el número introducido debe ser true y true 
# si queremos que ejecute la primera, si no en el elif se cumplirá también 
# la primera y solo ejecutará esta


numero = int(input("Escriba un número: "))
if numero % 2 == 0 and numero % 4 != 0:
    print(f"{numero} es múltiplo de dos")
elif numero % 4 == 0:
    print(f"{numero} es múltiplo de cuatro y de dos")
else:
    print(f"{numero} no es múltiplo de dos")

#####################################################################
#####################################################################


    