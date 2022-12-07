# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------FUNCIONES MENÚ USUARIO-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
def comprueba_nueva_pass(passwd):
    contador_caracter_especial = 0
    contador_mayusculas = 0
    contador_numeros = 0
    for i in passwd:
        if i in '!@*%':
            contador_caracter_especial += 1
        elif i.isupper():
            contador_mayusculas += 1
        elif i.isdigit():
            contador_numeros += 1
    if len(passwd) >= 9 and contador_numeros >= 2 and contador_mayusculas >= 2 and contador_caracter_especial >= 1:
        return 'Segura'
    else:
        print('La contraseña no es segura. Para mayor seguridad introduzca 2 números, 2 mayúsculas y un '
              'caracter especial [@ * % !].')
        return 'Insegura'

# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------EJERCICIO 3. MENÚ ADMINISTRADOR--------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

import time
continuar = 'Si'
def menu_admin(user = 'administrator'):
    while continuar.startswith('S'):
        # IMPRESIÓN DEL MENÚ
        print('|---------------' + '\x1b[1;32m' + 'MENÚ ADMINISTRADOR' + '\033[;m' + '--------------|', end=time.sleep(0.2))
        print('|    1- Bloquear o desbloquear un usuario.      |', end=time.sleep(0.2))
        print('|    2- Imprimir todas las contraseñas.         |', end=time.sleep(0.2))
        print('|    3- Imprimir contraseñas de un usuario.     |', end=time.sleep(0.2))
        print('|    4- Eliminar un usuario.                    |', end=time.sleep(0.2))
        print('|    ' + '\x1b[1;31m' + '0- SALIR' + '\033[;m' + '                                   |', end=time.sleep(0.2))
        print('|-----------------------------------------------|', end=time.sleep(0.2))

        # INPUT CON VERIFICACIÓN DE ERRORES PARA ELEGIR LA OPCIÓN DEL MENÚ QUE QUEREMOS REALIZAR
        try:
            time.sleep(0.3)
            option = int(input('\nQué operación desea realizar?:\n'))
        except ValueError:
            time.sleep(0.3)
            print('Por favor, escriba el número de la acción que desea realizar.\n')
        else:  # SI LA OPCIÓN ES CORRECTA, ENTRAMOS EN LOS CONDICIONALES DE CADA OPCIÓN DEL MENÚ

            if option == 1:
                admin_bloqueo()

            elif option == 2:
                admin_view_all()

            elif option == 3:
                admin_view_user()

            elif option == 4:
                admin_delete()

            elif option == 0:
                quit()

            else:
                time.sleep(1)
                print('Lo sentimos, la opción elegida no está en el menú, vuelva a intentarlo.\n')

# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------FUNCIONES DEL MENÚ --------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# FUNCIÓN QUE PERMITE AL ADMINISTRADOR BLOQUEAR O DESBLOQUEAR A UN USUARIO. SOLICITARÁ UN NOMBRE DE USUARIO Y PREGUNTA
# SI DESEA DESBLOQUEAR O BLOQUEAR AL USUARIO. SE MODIFICAN LOS CAMBIOS EN LA DD.BB.
# DEVUELVE LA FUNCIÓN SALIR() QUE PREGUNTA AL ADMINISTRADOR SI DESEA CONTINUAR
def admin_bloqueo():
    # Conexión con la base de datos de MySQL
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()
    cur2 = miConexion.cursor()

    # Diccionario de Usuarios y sus bloqueos
    usuarios = {}
    # Guardamos los valores en el diccionario
    cur.execute("""SELECT usuario,bloqueo FROM acceso;""")
    for usuario, bloqueo in cur.fetchall():
        usuarios[usuario] = bloqueo

    # Preguntamos el nombre del usuario
    user = input('Ingrese el nombre del Usuario:\n')

    # Variables con las querys de MySQL
    bloquear = """
                UPDATE acceso 
                    SET bloqueo = True 
                    WHERE usuario = %s
                    """
    desbloquear = """
                    UPDATE acceso 
                        SET bloqueo = False 
                        WHERE usuario = %s
                        """
    # Verificamos que el usuario esté en el llavero
    if user not in usuarios.keys():
        print(f'El usuario {user} no se encuentra en la base de datos.\n')
        return salir()
    else:
        pregunta = input(f'Desea Bloquear o Desbloquear al Usuario {user}?:\n').upper()

        if pregunta == 'B':
            if usuarios[user] == 1:
                print(f'El usuario {user} ya se encuentra bloqueado\n')
                return salir()
            else:
                pregunta2 = input('Está seguro que desea bloquear al usuario?: [S/N]\n').upper()
                if pregunta2.startswith('S') or pregunta2 == 1:
                    cur2.execute(bloquear, (user,))  # Modificamos la columna de bloqueo de la base de datos.
                    miConexion.commit()
                    miConexion.close()
                    print(f'El usuario {user} ha sido bloqueado.')
                    return salir()
                else:
                    return salir()

        elif pregunta == 'D':
            if usuarios[user] == 0:
                print(f'El usuario {user} ya se encuentra desbloqueado\n')
                return salir()
            else:
                pregunta2 = input('Está seguro que desea desbloquear al usuario?: [S/N]\n').upper()
                if pregunta2.startswith('S') or pregunta2 == 1:
                    cur2.execute(desbloquear, (user,))  # Modificamos la columna de bloqueo de la base de datos.
                    miConexion.commit()
                    miConexion.close()
                    print(f'El usuario {user} ha sido desbloqueado.')
                    return salir()
                else:
                    return salir()
        else:
            print('La opción no es correcta.')
            salir()
##### FUNCIONA #####

# Función que solicita un nombre de usuario y muestra sus aplicaciones y contraseñas que tiene guardadas luego de ser
# desencriptadas. Devuelve la función salir para volver al menú principal.
def admin_view_user():
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur1 = miConexion.cursor()
    cur2 = miConexion.cursor()  # Creamos cursores para trabajar en la base de datos

    # Solicitamos el nombre del usuario
    user = input('Ingrese el nombre del Usuario:\n')

    # Variables con las querys de MySQL.
    check_user = """
                SELECT usuario, bloqueo
                    FROM acceso 
            """
    select = """
                SELECT aplicacion, contraseña
                    FROM user_pass 
                    WHERE usuario = %s
                    ORDER BY aplicacion ASC
            """

    # Guardamos los usuarios en un diccionario para acceder a ellos en verificaciones posteriores
    cur1.execute(check_user)
    usuarios = {}
    for usuario, bloqueo in cur1.fetchall():
        usuarios[usuario] = bloqueo

    # Verificamos que el usuario esté en el diccionario
    if user not in usuarios.keys():
        print('El usuario no se encuentra en la base de datos.\n')  # Si no está, vuelve al menú
        return salir()
    else:  # Si está, imprime sus credenciales guardadas.
        cur2.execute(select, (user,))
        print(f'Las aplicaciones y contraseñas del usuario {user} son:\n')
        for aplicacion, contraseña in cur2.fetchall():
            pass_unlocked = encrypting(contraseña)
            print(f'--> \x1b[1;42m\x1b[1;30m{aplicacion}:\033[;m ---- \x1b[1;42m\x1b[1;30m'
                  f'{pass_unlocked}\033[;m', end=time.sleep(0.3))
            miConexion.close()
        return salir()

### FUNCIONA ####

def admin_view_all():
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()  # Creamos cursores para trabajar en la base de datos

    # Variable con las querys de MySQL.
    order_by_select = """
                SELECT usuario, aplicacion, contraseña 
                    FROM user_pass 
                    GROUP BY usuario, aplicacion, contraseña 
                    ORDER BY usuario, aplicacion ASC
                    """

    cur.execute(order_by_select)  # Ordenamos las contraseñas por usuario y las imprimimos
    print(f'Las contraseñas guardadas en el llavero son:\n', end=time.sleep(0.3))
    for usuario, aplicacion, contraseña in cur.fetchall():
        pass_unlocked = encrypting(contraseña)
        print(f'{usuario} --> \x1b[1;42m\x1b[1;30m{aplicacion}:\033[;m ---- \x1b[1;42m\x1b[1;30m'
              f'{pass_unlocked}\033[;m', end=time.sleep(0.3))
    miConexion.close()
    return salir()
###  FUNCIONA ####

def admin_delete():
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero')
    curD = miConexion.cursor()
    curD.execute("SELECT usuario, bloqueo FROM acceso")
    lista_usuarios = []
    for row, index in curD:
        lista_usuarios.append(row)
    print("El listado de usuarios es el siguiente: ", lista_usuarios)

    # Pregunta por usuario que se desea eliminar y eliminación si existe
    eliminacion = str(input("¿Qué usuario de dicho listado desea borrar?: "))
    if eliminacion in lista_usuarios:
        curD.execute("DELETE FROM acceso WHERE usuario = %s", (eliminacion,))
        curD.execute("DELETE FROM user_pass WHERE usuario = %s", (eliminacion,))
        miConexion.commit()
        print(f'El usuario {eliminacion} y sus aplicaciones han sido eliminadas con éxito')
        return salir()
    else:
        print("El usuario introducido no se encuentra en la base de datos")
        return salir()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------FUNCIONES ADICIONALES------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

def salir():
    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()
    if continuar == 'NO' or continuar == 'N':
        return quit()
    else:
        return

# FUNCIÓN QUE ENCRIPTA O DESENCRIPTA EL TEXTO QUE SE LE INTRODUZCA. SE COMPONE DE DOS LISTAS CON LAS CUALES SE
# ENCRIPTARÁ Y UNA VARIABLE VACÍA PARA RELLENAR CON UN BUCLE FOR DE ACUERDO SE QUIERA ENCRIPTAR O DESENCRIPTAR.
# RECIBE UN PARÁMETRO QUE SERÁ UN STRING.
# DEVOLVERÁ EL PARÁMETRO QUE SE LE INTRODUCE LUEGO DE HABERLO ENCRIPTADO O DESENCRIPTADO SEGÚN CORRESPONDA.
def encrypting(frase):
    encrypted = ''
    code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    keyword = ['m', 'u', 'r', 'c', 'i', 'e', 'l', 'a', 'g', 'o']
    for i in frase:
        if i in keyword:
            encrypted += code[keyword.index(i)]
        elif i in code:
            encrypted += keyword[int(i)]
        else:
            encrypted += i
    return encrypted

# FUNCIÓN QUE SE CONECTA A LA BASE DE SQL Y DEVUELVE UNA LISTA CON DOS LISTAS DENTRO CON LOS ELEMENTOS DE LA BASE DE
# DATOS. NO RECIBE NINGÚN PARÁMETRO
def enlistar_elementos(user):
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()
    aplicaciones = []
    passwords = []
    select = """SELECT aplicacion, contraseña FROM user_pass WHERE usuario = %s"""
    cur.execute(select, (user,))
    for aplicacion, contraseña in cur.fetchall():
        aplicaciones.append(aplicacion)
        passwords.append(contraseña)
    miConexion.close()
    return [aplicaciones, passwords]


# FUNCIÓN 4. Solicita el nombre de una aplicación y elimina los valores de la aplicación y de su contraseña. Recibe
# como parámetro el nombre del usuario.
def menu_eliminar_contraseña(user):
    listas_db = enlistar_elementos(user)
    app = input('Cuál es la aplicación que desea eliminar del llavero?:\n').capitalize()
    if app not in listas_db[0]:  # VERIFICAMOS QUE LA APP ESTÉ GUARDADA EN EL LLAVERO PARA ESE USUARIO
        time.sleep(0.3)
        print('la aplicación no está guardada en el llavero.\n')
        return
    else:
        time.sleep(0.3)
        # PREGUNTAMOS SI ESTÁ SEGURO DE CONTINUAR Y LUEGO ELIMINA LOS ELEMENTOS DE LA BASE DE DATOS
        sure = input(f'Está seguro que desea eliminar la contraseña de \x1b[1;42m\x1b[1;30m{app}\033[;m?: '
                     f'[SI/NO]\n').upper()
        if sure == 'SI' or sure == 'S':
            delete_sql(app, user)
            return
        # SI SE ARREPIENTE O SE HA EQUIVOCADO Y NO DESEA ELIMINARLA PREGUNTAMOS SI DESEA REALIZAR OTRA OPERACIÓN
        else:
            return

# FUNCIÓN QUE SE CONECTA A LA BASE DE SQL Y ELIMINA EL ÚLTIMO ELEMENTO QUE SE GUARDÓ EN LA BASE DURANTE LA EJECUCIÓN
# DEL PROGRAMA.
def delete_sql(app, user):
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()
    delete = "DELETE FROM user_pass WHERE aplicacion = %s AND usuario = %s"
    cur.execute(delete, [app, user])
    miConexion.commit()
    miConexion.close()
    print(f'La aplicación \x1b[1;42m\x1b[1;30m{app}\033[;m y su contraseña han sido eliminadas del llavero.\n')
    app = ''
    return app


# -------------------------------------------PRUEBAS-------------------------------------------------------------------
# admin_bloqueo()
# admin_view_all()
# admin_view_user()
# admin_delete()
# menu_admin()
