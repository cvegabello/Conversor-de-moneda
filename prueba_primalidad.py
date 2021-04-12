def es_primo(numero):
    es_primo = True
    if numero == 1:
        es_primo = False
    else:
        for i in range(2,numero): #No me interesa evaluar la division entre 1 y el mismo numero
            res = numero % i
            if res == 0:
                es_primo = False # Con solo un numero que sea divisor ya no es numero primo
                break            # No se necesita seguir evaluando.
    return es_primo
    

def run():
    numero = int(input('Escribe un numero: '))
    if numero <= 0:
        print ('El numero debe ser mayor a cero. Intente nuevamente') #Una validación para evitar el ingreso de numeros negativos y el cero.
    elif es_primo(numero):
        print (str(numero) + " SI es un numero primo")
    else:
        print (str(numero) + " NO es un numero primo")


if __name__== '__main__':
    run()