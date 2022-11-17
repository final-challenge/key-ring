import time
import random

# PARA ACCEDER AL MENU PRINCIPAL DEL LLAVERO, SE DEBE INTRODUCIR LA CLAVE DE ACCESO
clave_acceso = 'contraseña_123'
# Si se falla 3 veces finaliza el programa

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------- DEFINICIÓN DE FUNCIONES EMPLEADAS EN LA EJECUCION DEL BLOQUE PRINCIPAL -----------------------
# ----------------------------------------------------------------------------------------------------------------------

# FUNCION PARA ENCRIPTAR - DESENCRIPTAR
# Cada caracter de la cadena de entrada, lo cambia por su simétrico (respecto a la posición) en las cadenas de
# sustitución: 'cadena_sust' y 'numero_sust'. Si el caracter no se encuentra en ninguna de las dos, lo deja intacto.
# <cadena> es el mensaje que se desea tratar. Debe ir entrecomillado
# <opcion> define la acción a realizar. Será [0] para encriptar y [1] para desencriptar


def encriptar(cadena):
    cadena_sust = 'aáAÁbBcCdDeéEÉfFgGhHiíIÍjJkKlLmMnNñÑoóOÓpPqQrRsStTuüúUÜÚvVwWxXyYzZ'
    numero_sust = '0123456789'
    cadena_salida = ''
    for caracter in cadena:  # recorre los caracteres de cadena
        if (caracter not in cadena_sust) and (caracter not in numero_sust):
            caracter = caracter
        elif caracter in cadena_sust:
            pos = cadena_sust.find(caracter)
            caracter = cadena_sust[len(cadena_sust)-pos - 1]
        elif caracter in numero_sust:
            pos = numero_sust.find(caracter)
            caracter = numero_sust[len(numero_sust) - pos - 1]
        cadena_salida += caracter  # construye la cadena de salida con los caracteres sustituidos
    return cadena_salida  # devuelve la cadena tratada

# FUNCIÓN PARA GENERAR CONTRASEÑAS
# <long> es la longitud de la contraseña deseada. Si no se incluye, se toma 8 por defecto.
# <caracteres> es la cadena con carateres que han de emplearse en la generación de la contraseña.
#              Si no se encluye, se usa una cadena por defecto


def new_password_2(long=8, caracteres='abcdefghijklmnopqrstuvwxyz0123456789.-_@#'):
    password = ''
    for i in range(0, long-1):
        caracter = random.choice(caracteres)
        tipo = random.choice('lu')
        if tipo == 'l':
            password += caracter.lower()
        elif tipo == 'u':
            password += caracter.upper()
    return password


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- CONTRASEÑAS DEL ENUNCIADO ----------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Se define el diccionario de partida a partir de los datos del enunciado

aplicaciones = ["Gmail", "Tinder", "Twitter", "Tiktok", "Instagram"]
contrasenas = ["20051206Correo!", "qwerasdf1234#", "Tw2022+LMP", "Tik2022*VTP", "Ins2022!MFR"]

llavero = {}  # diccionario vacio donde se almacenarán las contraseñas
for j in range(len(aplicaciones)):
    llavero[aplicaciones[j].upper()] = encriptar(contrasenas[j])


# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- BLOQUE PRINCIPAL --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Mensaje de bienvenida al iniciar el programa
print('-----------------------------------------------', end=time.sleep(0.5))
print('----------- LLAVERO DE CONTRASEÑAS ------------', end=time.sleep(0.5))
print('-----------------------------------------------', end=time.sleep(0.5))
print('\n')
time.sleep(1)

entrada = input('Por favor, introduzca su clave de acceso para\ncontinuar: ')
intento = 3  # contador de intentos. Mas de tres finaliza el programa
while entrada != clave_acceso:
    if intento == 1:
        print('\n')
        print('-----------------------------------------------', end=time.sleep(0.5))
        print('-------------- ACCESO BLOQUEADO ---------------', end=time.sleep(0.5))
        print('-----------------------------------------------', end=time.sleep(0.5))
        quit()
    intento -= 1
    print('\x1b[1;31m'+'La clave introducida no es correcta. ')
    print('\033[;m'+'Tiene', intento, 'intentos más antes de que se\nbloquee el acceso al llavero.')
    entrada = input('Por favor, introduzca su clave de acceso para\ncontinuar: ')

# Contraseña correcta
time.sleep(1)
print('\x1b[1;32m'+'La clave introducida es correcta.'+'\033[;m')
print('\n')
time.sleep(1)

# Bucle para repetir la ejecución tantas veces como se desee:
while True:

    # Menu de la aplicación
    print('-------------- MENU DE PRINCIPAL --------------', end=time.sleep(0.3))
    print('-   [1] -> Guardar una nueva contraseña       -', end=time.sleep(0.3))
    print('-   [2] -> Modificar una contraseña existente -', end=time.sleep(0.3))
    print('-   [3] -> Eliminar una contraseña existente  -', end=time.sleep(0.3))
    print('-   [4] -> Buscar una contraseña almacenada   -', end=time.sleep(0.3))
    print('-   [5] -> Listar contraseñas existentes      -', end=time.sleep(0.3))
    print('-   [6] -> Salir de la aplicación             -', end=time.sleep(0.3))
    print('-----------------------------------------------', end=time.sleep(0.3))
    print('\n')
    # Pedir acción y repetir pregunta si el formato no es correcto
    while True:
        accion = input('Seleccione la acción que desea realizar: ')
        if accion in '1234567' and len(accion) == 1:
            break
        else:
            print('La acción introducida no existe.')
    print('\n')

    # Guardar contraseña
    if accion == '1':
        time.sleep(1)
        # # palabra clave del diccionario. repite la pregunta si la clave ya existe
        while True:
            nombre = input('Introduzca el nombre con el que desea guardar\nla nueva contraseña: ').upper()
            if nombre not in llavero:
                break
            else:
                print('El nombre introducido ya se encuentra asociado a una contraseña almacenada.')
        # cadena asociada a la clave
        while True:
            generar = input('Desea generar una contraseña aleatoria? [Si] o [No]: ').lower()
            if generar == 'si':
                item = new_password_2()
                print('\nContraseña: ', '\x1b[1;34m' + item + '\033[;m')
                break
            elif generar == 'no':
                item = input('Introduzca la nueva contraseña: ')
                break
            else:
                print('Respuesta incorrecta.')
        # encripta la cadena antes de guardarla en el diccionario
        item_encriptado = encriptar(item)
        llavero[nombre] = item_encriptado
        time.sleep(0.5)
        print('Guardando', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('\nLa contraseña', nombre, 'se ha guardado con exito.\n')
        time.sleep(2)
        # pregunta sobre otra acción
        while True:
            otra_accion = input('Desea realizar otra acción? [Si] o [No]: ').lower()
            if otra_accion == 'si':
                print('\n')
                break
            elif otra_accion == 'no':
                quit()
            else:
                print('Respuesta incorrecta.')

    # Modificar contraseña
    elif accion == '2':
        time.sleep(1)
        # palabra clave del diccionario. repite la pregunta si la clave no existe
        while True:
            nombre = input('Introduzca el nombre de la contraseña que desea\nmodificar: ').upper()
            if nombre in llavero:
                break
            else:
                print('El nombre introducido no se corresponde con\nninguna contraseña almacenada.')
        # cadena asociada a la clave
        while True:
            generar = input('Desea generar una contraseña aleatoria? [Si] o [No]: ').lower()
            if generar == 'si':
                item = new_password_2()
                print('\nContraseña: ', '\x1b[1;34m' + item + '\033[;m')
                break
            elif generar == 'no':
                item = input('Introduzca la nueva contraseña: ')
                break
            else:
                print('Respuesta incorrecta.')
        # encripta la cadena antes de guardarla en el diccionario
        item_encriptado = encriptar(item)
        llavero[nombre] = item_encriptado
        time.sleep(0.5)
        print('Modificando', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('\nLa contraseña', nombre, 'se ha modificado con exito.\n')
        time.sleep(2)
        # pregunta sobre otra acción
        while True:
            otra_accion = input('Desea realizar otra acción? [Si] o [No]: ').lower()
            if otra_accion == 'si':
                print('\n')
                break
            elif otra_accion == 'no':
                quit()
            else:
                print('Respuesta incorrecta.')

    # Eliminar contraseña
    elif accion == '3':
        time.sleep(1)
        # palabra clave del diccionario. repite la pregunta si la clave no existe
        while True:
            nombre = input('Introduzca el nombre de la contraseña que desea\neliminar: ').upper()
            if nombre in llavero:
                break
            else:
                print('El nombre introducido no se corresponde con\nninguna contraseña almacenada.')
        del(llavero[nombre])
        time.sleep(0.5)
        print('Eliminando', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('\nLa contraseña', nombre, 'se ha eliminado con exito.\n')
        time.sleep(2)
        # pregunta sobre otra acción
        while True:
            otra_accion = input('Desea realizar otra acción? [Si] o [No]: ').lower()
            if otra_accion == 'si':
                print('\n')
                break
            elif otra_accion == 'no':
                quit()
            else:
                print('Respuesta incorrecta.')

    # Buscar contraseña
    elif accion == '4':
        time.sleep(1)
        # palabra clave del diccionario. repite la pregunta si la clave no existe
        while True:
            nombre = input('Introduzca el nombre de la contraseña que desea\nbuscar: ').upper()
            if nombre in llavero:
                break
            else:
                print('El nombre introducido no se corresponde con\nninguna contraseña almacenada.')
        time.sleep(0.5)
        print('Buscando', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        # desencripta la cadena y la muestra
        item_encriptado = llavero[nombre]
        item = encriptar(item_encriptado)
        print('\nLa contraseña', '\x1b[1;34m'+nombre+'\033[;m', 'es: ', '\x1b[1;34m'+item+'\033[;m')
        print('\n')
        time.sleep(2)
        # pregunta sobre otra acción
        while True:
            otra_accion = input('Desea realizar otra acción? [Si] o [No]: ').lower()
            if otra_accion == 'si':
                print('\n')
                break
            elif otra_accion == 'no':
                quit()
            else:
                print('Respuesta incorrecta.')

    # Listar contraseñas existentes
    elif accion == '5':
        time.sleep(1)
        if len(llavero) == 0:
            print('El llavero aun no contiene ninguna contraseña almacenada.')
        else:
            print('El llavero contiene las siguientes contraseñas almacenadas:')
            for nombre in llavero:
                print(nombre)
        print('\n')
        time.sleep(2)
        # pregunta sobre otra acción
        while True:
            otra_accion = input('Desea realizar otra acción? [Si] o [No]: ').lower()
            if otra_accion == 'si':
                print('\n')
                break
            elif otra_accion == 'no':
                quit()
            else:
                print('Respuesta incorrecta.')

    # Salir
    elif accion == '6':
        time.sleep(1)
        break
