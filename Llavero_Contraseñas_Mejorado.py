# ------------------------------------------------RETO PASSWORDS-------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
#-------------------------------------COMIENZO DEL EJERCICIO-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
# IMPORTO LIBRERÍAS Y FUNCIONES
import time
from Funciones import generate_password, password, encrypting
# LISTAS Y VARIABLES PREDEFINIDAS
aplicaciones = ["Gmail", "Tinder", "Twitter", "Tiktok", "Instagram"]
passwords = ["20051206Correo!", "qwerasdf1234#", "Tw2022+LMP", "Tik2022*VTP", "Ins2022!MFR"]
passwords_encriptadas = []
new_app = ''
new_password = ''
continuar = 'SI'

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------MENÚ PRINCIPAL --------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

while continuar.startswith('S'):
    time.sleep(1)
    print(
        '|-------------'+'\x1b[1;32m'+'LLAVERO DE CONTRASEÑAS'+'\033[;m'+'------------|\n|    1- Agregar una nueva contraseña.           |\n|    2- Buscar una contraseña ya registrada.    |\n|    3- Eliminar la última contraseña agendada. |\n|    4- Modificar una contraseña.               |\n|    5- Imprimir todo el llavero.               |\n|    '+'\x1b[1;31m'+'0- SALIR'+'\033[;m'+'                                   |\n|-----------------------------------------------|\n')

    # INPUT CON VERIFICACIÓN DE ERRORES PARA ELEGIR LA OPCIÓN DEL MENÚ QUE QUEREMOS REALIZAR
    try:
        time.sleep(0.3)
        option = int(input('\nQué operación desea realizar?:\n'))
    except ValueError:
        time.sleep(0.3)
        print('Por favor, escriba el número de la acción que desea realizar.\n')
    else:
        # SI LA OPCIÓN ES CORRECTA, ENTRAMOS EN LOS CONDICIONALES DE CADA OPCIÓN DEL MENÚ
        if option == 1:
            time.sleep(0.3)
            # SE PREGUNTA AL USUARIO LA APLICACIÓN
            new_app = input('Cuál es la aplicación que desea incorporar?:\n').capitalize()

            # BUSCAMOS SI YA ESTÁ ENLISTADA, DE LO CONTRARIO PREGUNTAMOS LA PASSWORD
            if new_app in aplicaciones:
                time.sleep(0.3)
                print('La aplicación ya se encuentra dentro de su llavero de contraseñas.\n')
                continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()

            else:
                # PREGUNTAMOS POR LA POSIBILIDAD DE AUTOGENERAR LA CONTRASEÑA
                generar_password = input('Desea que generemos la contraseña automáticamente? : [SI/NO]\n').upper()
                if generar_password == 'S' or generar_password == 'SI':
                    new_password = generate_password()
                else:
                    while True:
                        new_password = password()
                        if new_password in passwords:  # SI LA CONTRASEÑA ESTÁ REPETIDA LO INTENTAMOS DE NUEVO
                            print('La contraseña escogida ya está dentro de su llavero, por su seguridad mejor elija una nueva.\n')
                        else:
                            break

                # LE OFRECEMOS LA POSIBILIDAD DE ENCRIPTAR SU password CON EL ENCRIPTAMIENTO "MURCIÉLAGO"
                encriptar = input('Desea encriptar su nueva contraseña?: [SI/NO]\n').upper()
                if encriptar == 'S' or encriptar == 'SI':
                    encrypting(new_password)
                    # GUARDAMOS LA CONTRASEÑA ENCRIPTADA EN LA LISTA DE CONTRASEÑAS Y DE CONTRASEÑAS ENCRIPTADAS.
                    aplicaciones.append(new_app)
                    passwords.append(new_password)
                    passwords_encriptadas.append(new_password)
                    time.sleep(0.3)
                    print(f'La contraseña \x1b[1;42m\x1b[1;30m{new_password}\033[;m ha sido encriptada y guardada con éxito.\n')
                    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()
                else:
                    # GUARDAMOS LA CONTRASEÑA Y LA APLICACIÓN EN SUS RESPECTIVAS LISTAS.
                    aplicaciones.append(new_app)
                    passwords.append(new_password)
                    time.sleep(0.3)
                    print(f'La contraseña \x1b[1;42m\x1b[1;30m{new_password}\033[;m ha sido guardada con éxito.\n')
                    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()

        # BUSCAMOS Y DEVOLVEMOS LA CONTRASEÑA QUE SOLICITE EL USUARIO
        elif option == 2:
            time.sleep(0.3)
            find_app = input('Ingrese el nombre de la aplicación que desea conocer su contraseña:\n').capitalize()
            if find_app not in aplicaciones:
                time.sleep(0.3)
                print('Lo sentimos, la aplicación elegida no está dentro de sus contraseñas.\n')
                continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()

            else:
                # VERIFICA SI LA CONTRASEÑA ESTÁ ENCRIPTADA Y OFRECE DESENCRIPTARLA O DEVOLVERLA ENCRIPTADA
                if passwords[aplicaciones.index(find_app)] in passwords_encriptadas:
                    desencriptar = input(
                        'La contraseña que está buscando está encriptada. Desea desencriptarla?: [SI/NO]\n').upper()
                    if desencriptar.startswith('S'):
                        password_unlocked = encrypting(passwords[aplicaciones.index(find_app)])
                        print(f'La contraseña desencriptada de \x1b[1;42m\x1b[1;30m{find_app}\033[;m  es \x1b[1;42m\x1b[1;30m{password_unlocked}\033[;m\n')
                        continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()
                    else: # DEVUELVE LA CONTRASEÑA ENCRIPTADA, SIN DESENCRIPTAR
                        print(f'La contraseña encriptada de \x1b[1;42m\x1b[1;30m{find_app}\033[;m es \x1b[1;42m\x1b[1;30m{passwords[aplicaciones.index(find_app)]}\033[;m\n')
                        continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()

                else:  # SI NO ESTÁ ENCRIPTADA LA DEVUELVE DIRECTAMENTE SEGÚN FUE GUARDADA
                    time.sleep(0.3)
                    print(f'La contraseña de \x1b[1;42m\x1b[1;30m\x1b[1;30m{find_app}\033[;m es \x1b[1;42m\x1b[1;30m{passwords[aplicaciones.index(find_app)]}\033[;m.\n')
                    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()

        # ELIMINAMOS LA ÚLTIMA CONTRASEÑA QUE SE GUARDÓ DURANTE LA EJECUCIÓN DEL PROGRAMA
        elif option == 3:

            # SI LA APLICACIÓN NO ESTÁ GUARDADA EN APLICACIONES DEVUELVE UN PRINT PARA EVITAR EL ERROR
            if new_app not in aplicaciones:
                time.sleep(0.3)
                print(
                    'No se ha podido eliminar ya que durante la ejecución del programa no se ha guardado ninguna contraseña o porque la aplicación no está en el llavero.\n')
                continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()

            else:
                time.sleep(0.3)
                # PREGUNTAMOS SI ESTÁ SEGURO DE CONTINUAR Y LUEGO ELIMINA LA CONTRASEÑA
                sure = input(f'Está seguro que desea eliminar la contraseña de \x1b[1;42m\x1b[1;30m{new_app}\033[;m?: [SI/NO]\n').upper()

                if sure == 'SI' or sure == 'S':
                    time.sleep(0.3)
                    print(
                        f'La contraseña \x1b[1;42m\x1b[1;30m{passwords[aplicaciones.index(new_app)]}\033[;m y la aplicación \x1b[1;42m\x1b[1;30m{new_app}\033[;m han sido eliminadas del llavero.\n')

                    # MIRAMOS EN passwords_encriptadas SI ESTA GUARDADA TAMBIÉN PARA ELIMINARLA
                    if passwords[aplicaciones.index(new_app)] in passwords_encriptadas:
                        passwords_encriptadas.remove(passwords[aplicaciones.index(new_app)])
                    else:
                        continue
                    # ELIMINAMOS LA APP Y LA PASSWORD DE SUS RESPECTIVAS LISTAS
                    del (passwords[aplicaciones.index(new_app)])
                    aplicaciones.remove(new_app)
                    new_app = ''  # DEJAMOS LA VARIABLE NEW_APP VACÍA
                    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()

                # SI SE ARREPIENTE O SE HA EQUIVOCADO Y NO DESEA ELIMINARLA PREGUNTAMOS SI DESEA REALIZAR OTRA OPERACIÓN
                else:
                    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()

        # MODIFICAMOS LA PASSWORD
        elif option == 4:
            time.sleep(0.3)
            # PREGUNTAMOS LA APLICACIÓN QUE DESEA MODIFICAR
            modify_app = input('Cuál es la aplicación que desea modificar su contraseña?:\n').capitalize()

            # CONDICIONAL PARA BUSCAR LA APP y TRAER EL ÍNDICE PARA CONSEGUIR LA CONTRASEÑA A MODIFICAR
            if modify_app not in aplicaciones:
                print('Lo sentimos, la aplicación elegida no está dentro de sus contraseñas.\n')
                continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()
            else:
                time.sleep(0.3)
                # PREGUNTAMOS POR LA POSIBILIDAD DE AUTOGENERAR LA CONTRASEÑA
                generar_password = input('Desea que generemos la contraseña automáticamente? : [SI/NO]\n').upper()
                if generar_password == 'S' or generar_password == 'SI':
                    change_password = generate_password()
                else:
                    while True:  # SOLICITAMOS LA CONTRASEÑA AL USUARIO Y VERIFICAMOS QUE NO ESTE REPETIDA
                        change_password = password()
                        if change_password in passwords:
                            print('La contraseña seleccionada ya está dentro de su llavero, por su seguridad mejor elija una nueva.')
                        else:
                            break

                # CONTROLAMOS QUE NO ESTE EN LA LISTA DE ENCRIPTADAS, SINO LA ELIMINAMOS PARA GENERAR LA NUEVA
                if passwords[aplicaciones.index(modify_app)] in passwords_encriptadas:
                    passwords_encriptadas.remove(passwords[aplicaciones.index(modify_app)])
                else:
                    continue

                # LE OFRECEMOS LA POSIBILIDAD DE ENCRIPTAR
                encriptar = input('Desea encriptar su nueva contraseña?: [SI/NO]\n').upper()
                if encriptar == 'S' or encriptar == 'SI':
                    change_password = encrypting(change_password)
                    # GUARDAMOS LOS NUEVOS VALORES EN SUS RESPECTIVAS LISTAS
                    passwords.insert(aplicaciones.index(modify_app), change_password)
                    del (passwords[aplicaciones.index(modify_app) + 1])
                    passwords_encriptadas.append(change_password)
                    time.sleep(0.3)
                    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()
                else:
                    # GUARDAMOS LOS NUEVOS VALORES EN SUS RESPECTIVAS LISTAS
                    passwords.insert(aplicaciones.index(modify_app), change_password)
                    del (passwords[aplicaciones.index(modify_app) + 1])
                    time.sleep(0.3)
                    print(f'La contraseña de \x1b[1;42m\x1b[1;30m{modify_app}\033[;m ha sido modificada con éxito.')
                    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()


# OPCIÓN QUE IMPRIME TODOS LOS VALORES DE LAS LISTAS DE APLICACIONES Y PASSWORDS
        elif option == 5:
            for i in range(len(aplicaciones)):
                print(f'La contraseña de \x1b[1;42m\x1b[1;30m{aplicaciones[i]}\033[;m es \x1b[1;42m\x1b[1;30m{passwords[i]}\033[;m')
            continuar = input('\nDesea realizar otra operación?: [SI/NO]\n').upper()

        # OPCIÓN PARA FINALIZAR EL PROGRAMA
        elif option == 0:
            break

        # CONDICIONAL QUE NOS EVITA UN ERROR Y VUELVE AL MENÚ PRINCIPAL SI LA OPCIÓN ELEGIDA NO ESTÁ EN LAS OPCIONES
        else:
            print('Lo sentimos, la opción elegida no está en el menú, vuelva a intentarlo.')
