import os
valor_dolar_colombia = 3650
valor_dolar_argentina =  65
valor_dolar_mexico = 24
os.system ("clear") 
menu = """
        💰 Bienvenido al conversor de monedas. Por favor seleccione la moneda extranjera.

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
        pesos = input("Cuantos pesos colombianos tienes?:")
        pesos = float(pesos)
        dolares = pesos / valor_dolar_colombia
        dolares = round(dolares,2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " dolares")    
    elif (cod_seleccion == 2):
        dolares = input("Cuantos dolares tienes?:")
        dolares = float(dolares)
        pesos = dolares * valor_dolar_colombia
        pesos = round(pesos,2)
        #pesos = str(pesos)
        print(f"Tienes $ {pesos:,.2f}" + " pesos colombianos.")
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
        pesos = input("Cuantos pesos argentinos tienes?:")
        pesos = float(pesos)
        dolares = pesos / valor_dolar_argentina
        dolares = round(dolares,2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " dolares")    
    elif (cod_seleccion == 2):
        dolares = input("Cuantos dolares tienes?:")
        dolares = float(dolares)
        pesos = dolares * valor_dolar_argentina
        pesos = round(pesos,2)
        pesos = str(pesos)
        print("Tienes $" + pesos + " pesos argentinos.")
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
        pesos = input("Cuantos pesos mexicanos tienes?:")
        pesos = float(pesos)
        dolares = pesos / valor_dolar_mexico
        dolares = round(dolares,2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " dolares")    
    elif (cod_seleccion == 2):
        dolares = input("Cuantos dolares tienes?:")
        dolares = float(dolares)
        pesos = dolares * valor_dolar_mexico
        pesos = round(pesos,2)
        pesos = str(pesos)
        print("Tienes $" + pesos + " pesos mexicanos")
    else:
        print("La opción " + str(cod_seleccion) + " no es valida, por favor digite la opción correcta.")

