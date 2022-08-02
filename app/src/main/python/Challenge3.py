"""
 Reto #3
 ¿ES UN NÚMERO PRIMO?
 Fecha publicación enunciado: 17/01/22
 Fecha publicación resolución: 24/01/22
 Dificultad: MEDIA
 
 Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
 
 Información adicional:
 - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""

def main():
    print(createPrime(100))
    

def createPrime(length):
    result = []
    for i in range(length):
        if isPrime(i):
            result.append(i)
    return result

def isPrime(number):
    if number < 2:
        return False

    i = 2
    for i in reversed(range(2, number - 1)):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()