import random
import string
from ahorcado_diagramas import vidas_diccionario_visual
from palabras import palabras


def obtener_palabra_valida(palabras):
    #seleccionamos una palabra al azar
    palabra = random.choice(palabras)
    
    while "-" in palabras or " " in palabras:
        palabra = random.choice(palabras)
        
    return palabra.upper()

def ahorcado():
    palabra = obtener_palabra_valida(palabras)
    
    #para que no hayan letras repetidas se convierten en un conjunto
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    
    vidas = 7 
    
    print("====================================")
    print(" ¡Bienvenido al juego del ahorcado! ")
    print("====================================")
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"te quedan {vidas} vidas) y has usado estas letras: {' '.join(letras_adivinadas)}")
        
        #mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        
        #mostrar estado de la horca
        print(vidas_diccionario_visual[vidas])
        #mostrar letras separadas por espacio
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escoge una letra: ").upper()
        
        #A abecedario se le restan los valores que esten en letras_adivinadas y si la letra ingresada esta en el resultantes es que no habia sido ingresada
        #por lo cual se ingresa en la lista
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            #Si la letra esta en la palabra, quita la letra por adivinar, si no quita una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("")
            else:
                vidas = vidas - 1
                print(f"\n Tu letra, {letra_usuario} no esta en la palabra")
                
        #Si la letra escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esta letra. Por favor escoge otra")
        
        else:
            print("El caracter ingresado no es valido")
            
    #cuando llegan todas las tetras de la palabra
    #o el jugador se queda sin vida
    #el juego llega hasta aqui
    
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Perdiste. Lo lamento, la palabra era: {palabra}")
    else:
        print("¡felicidades! has adivinado la palabra")

ahorcado()