import random

def run():
    print ('Elige el rango el rango de numeros.')
    numero_minimo = int(input('Elige un numero minimo: '))
    numero_maximo = int(input('Elige un numero maximo: '))
    if numero_minimo >= numero_maximo:
        print ('El numero minimo debe ser menor que el numero maximo. Intente nuevamente') #Una validación para evitar que el numero minimo sea mayor o igual que el numero maximo
    else:
        numero_random = random.randint(numero_minimo,numero_maximo)
        numero_elegido = int(input('Elige un numero del ' + str(numero_minimo) + ' al '+ str(numero_maximo) + ':'))
        while numero_elegido != numero_random:
            if numero_elegido < numero_random:
                print ('Busca un numero mas grande.')
            elif numero_elegido > numero_random:
                print ('Busca un numero mas pequeño.')
            numero_elegido = int(input('Elige otro numero:'))
        print ('!!! GANASTE !!!')

if __name__== '__main__':
    run()