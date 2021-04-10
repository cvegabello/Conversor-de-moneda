import os
valor_dolar_colombia = 3650
valor_dolar_argentina =  65
valor_dolar_mexico = 24
os.system ("clear") 

def calculo_pesos_to_dolar(valor_dolar_pais, from_pais):
    pesos = input("Cuantos pesos " + from_pais + " tienes?:")
    pesos = float(pesos)
    dolares = pesos / valor_dolar_pais
    dolares = round(dolares,2)
    print(f"Tienes $ {dolares:,.2f}" + " dolares")    

def calculo_dolar_to_pesos(valor_dolar_pais, from_pais):
    dolares = input("Cuantos dolares tienes?:")
    dolares = float(dolares)
    pesos = dolares * valor_dolar_pais
    pesos = round(pesos,2)
    print(f"Tienes $ {pesos:,.2f}" + " pesos " + from_pais + ".")


menu = """
        💰 Bienvenido al conversor de monedas, super FANTASTICO. Por favor seleccione la moneda extranjera.

         1 - Pesos colombianos.
         2 - Pesos argentinos.
         3 - Pesos mexicanos.

         Elige una opción:  """

cod_seleccion = int(input(menu))
if (cod_seleccion == 1):
    os.system ("clear") 
    menu = """
        Conversor pesos colombianos.
        
         1 - Pesos colombianos a Dolares americanos.
         2 - Dolares americanos a pesos colombianos. 

         Elige una opción:  """
    
    cod_seleccion = int(input(menu))
    
    if (cod_seleccion == 1):
        calculo_pesos_to_dolar(valor_dolar_colombia, "colombianos")

    elif (cod_seleccion == 2):
        calculo_dolar_to_pesos(valor_dolar_colombia, "colombianos")
    else:
        print("La opción " + str(cod_seleccion) + " no es valida, por favor digite la opción correcta.")

elif (cod_seleccion == 2):
    os.system ("clear")
    menu = """
        Conversor pesos argentinos.
        
         1 - Pesos argentinos a Dolares americanos.
         2 - Dolares americanos a pesos argentinos. 

         Elige una opción:   """
    
    cod_seleccion = int(input(menu))
    if (cod_seleccion == 1):
        calculo_pesos_to_dolar(valor_dolar_argentina, "argentinos")
    elif (cod_seleccion == 2):
        calculo_dolar_to_pesos(valor_dolar_argentina, "argentinos")
    else:
        print("La opción " + str(cod_seleccion) + " no es valida, por favor digite la opción correcta.")

elif (cod_seleccion == 3):
    os.system ("clear")
    menu = """
         Conversor pesos mexicanos.
        
         1 - Pesos mexicanos a Dolares americanos.
         2 - Dolares americanos a pesos mexicanos. 

         Elige una opción:  """
    
    cod_seleccion = int(input(menu))
    if (cod_seleccion == 1):
        calculo_pesos_to_dolar(valor_dolar_mexico, "mexicanos")
    elif (cod_seleccion == 2):
        calculo_dolar_to_pesos(valor_dolar_mexico, "mexicanos")
    else:
        print("La opción " + str(cod_seleccion) + " no es valida, por favor digite la opción correcta.")

