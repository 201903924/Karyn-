num=int(input("Ingrese un numero"))
def es_primo(num):

    contador=0
    resultado=True

    for i in range(1, num+1):
        if num % i ==0:
            contador += 1
         if (contador >2):
             
            resultado=False
            break
            return resultado
    if (es_primo(num)==True):
        print("el numero es primo")
    else :
        primo("el numero es par")
