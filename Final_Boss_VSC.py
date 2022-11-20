import mysql.connector
import time
from Funciones import generate_password, password, encrypting, salir, insert_sql, enlistar_elementos, imprimir_elementos, delete_sql, modify_sql

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------CONEXIÓN CON MySQL-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# NOS CONECTAMOS A MySQL
miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789')

# CREAMOS UNA VARIABLE QUE HARÁ DE CONECTOR PARA REALIZAR OTRAS FUNCIONES
cur = miConexion.cursor()

# CREAMOS LA BASE DE DATOS
cur.execute("CREATE DATABASE IF NOT EXISTS llavero")
miConexion.commit()

# ELEGIMOS LA BASE DE DATOS llavero PARA TRABAJAR SOBRE ELLA
cur.execute("USE llavero")
miConexion.commit()

# CREAMOS LA TABLA
cur.execute('''CREATE TABLE IF NOT EXISTS user_pass (
           id  int(11)  NOT NULL   AUTO_INCREMENT  PRIMARY KEY,
           aplicacion   VARCHAR(50),
           contraseña   VARCHAR(50),
           contraseña_encriptada    VARCHAR(50)
           ); ''')
miConexion.commit()

# CARGAMOS LOS DATOS INICIALES 
insert = """INSERT INTO user_pass (aplicacion,contraseña, contraseña_encriptada) VALUES(%s, %s, %s)"""

# ESTE CÓDIGO LO COMENTO SINO CADA VEZ QUE CORRA EL PROGRAMA VOLVERÁ A CARGAR LOS MISMOS DATOS
# cur.executemany(insert, (('Gmail', '20051206Correo!', None), 
#                          ('Tinder', 'qwerasdf1234#', None),
#                          ('Twitter', 'Tw2022+LMP', None),
#                          ('Tiktok', 'Tik2022*VTP', None),
#                          ('Instagram', 'Ins2022!MFR', None),
#                          ('Canvas', 'Canvas12385!', None)))
# miConexion.commit()  
miConexion.close()

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------INICIO DEL EJERCICIO---------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# VARIABLES QUE REPRESENTAN LAS FUNCIONES DE MySQL
delete_app = """DELETE FROM user_pass WHERE aplicacion = (%s)"""
delete_passwd = """DELETE FROM user_pass WHERE contraseña = (%s)"""
modify = """UPDATE user_pass SET contraseña = (%s) WHERE aplicacion = (%s)"""

# VARIABLES PARA UTILIZAR EN EL PROGRAMA
new_app = ''
new_password = ''
continuar = 'SI'

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------MENÚ PRINCIPAL --------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------


while continuar == 'SI' or continuar == 'S':

    # IMPRESIÓN DEL MENÚ
    print('|-------------'+'\x1b[1;32m'+'LLAVERO DE CONTRASEÑAS'+'\033[;m'+'------------|', end=time.sleep(0.2))
    print('|    1- Agregar una nueva contraseña.           |', end=time.sleep(0.2))
    print('|    2- Buscar una contraseña ya registrada.    |', end=time.sleep(0.2))
    print('|    3- Eliminar la última contraseña agendada. |', end=time.sleep(0.2))
    print('|    4- Modificar una contraseña.               |', end=time.sleep(0.2))
    print('|    5- Imprimir todo el llavero.               |', end=time.sleep(0.2))
    print('|    '+'\x1b[1;31m'+'0- SALIR'+'\033[;m'+'                                   |', end=time.sleep(0.2))
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
            time.sleep(0.3)
            # SE PREGUNTA AL USUARIO LA APLICACIÓN
            listas_db = enlistar_elementos()  # ENLISTAMOS LOS ELEMENTOS DE LA BASE DE DATOS
            new_app = input('Cuál es la aplicación que desea incorporar?:\n').capitalize()
            if new_app in listas_db[0]:  # VERIFICAMOS QUE LA APLICACIÓN NO SE HAYA GUARDADO ANTES
                time.sleep(0.3)
                print('La aplicación ya se encuentra dentro de su llavero de contraseñas.\n')
                salir() 
            else:
                # PREGUNTAMOS POR LA POSIBILIDAD DE AUTOGENERAR LA CONTRASEÑA
                generar_password = input('Desea que generemos la contraseña automáticamente? : [SI/NO]\n').upper()
                if generar_password == 'S' or generar_password == 'SI':
                    new_password = generate_password()
                else:
                    new_password = password(listas_db[1])
                    
                # LE OFRECEMOS LA POSIBILIDAD DE ENCRIPTAR SU CONTRASEÑA CON EL ENCRIPTAMIENTO "MURCIÉLAGO"
                encriptar = input('Desea encriptar su nueva contraseña?: [SI/NO]\n').upper()
                if encriptar == 'S' or encriptar == 'SI':
                    password_locked = encrypting(new_password) # ENCRIPTAMOS LA CONTRASEÑA
                    insert_sql(new_app, None , password_locked) # INSERTAMOS EN LA TABLA DE SQL LA CONTRASEÑA ENCRIPTADA
                    time.sleep(0.3)
                    salir()
                else:
                    insert_sql(new_app, new_password, None) # INSERTAMOS EN LA TABLA SQL LA CONTRASEÑA SIN ENCRIPTAR
                    time.sleep(0.3)
                    salir()

        elif option == 2:
            time.sleep(0.3)
            find_app = input('Ingrese el nombre de la aplicación que desea conocer su contraseña:\n').capitalize()
            listas_db = enlistar_elementos()
            if find_app not in listas_db[0]:
                time.sleep(0.3)
                print('Lo sentimos, la aplicación elegida no está dentro de sus contraseñas.\n')
                salir()

            else:
                 # VERIFICA SI LA CONTRASEÑA ESTÁ ENCRIPTADA Y OFRECE DESENCRIPTARLA O DEVOLVERLA ENCRIPTADA
                if listas_db[1][listas_db[0].index(find_app)] == None:
                    desencriptar = input('La contraseña que está buscando está encriptada. Desea desencriptarla?: [SI/NO]\n').upper()
                    if desencriptar.startswith('S'):  # DEVUELVE LA CONTRASEÑA DESENCRIPTADA
                        password_unlocked = encrypting(listas_db[2][listas_db[0].index(find_app)])
                        print(f'La contraseña desencriptada de \x1b[1;42m\x1b[1;30m{find_app}\033[;m es \x1b[1;42m\x1b[1;30m{password_unlocked}\033[;m\n')
                        salir()
                    else:  # DEVUELVE LA CONTRASEÑA ENCRIPTADA
                        print(f'La contraseña encriptada de \x1b[1;42m\x1b[1;30m{find_app}\033[;m es \x1b[1;42m\x1b[1;30m{listas_db[2][listas_db[0].index(find_app)]}\033[;m\n')
                        salir()
                     
                else:  # SI NO ESTÁ ENCRIPTADA LA DEVUELVE DIRECTAMENTE SEGÚN FUE GUARDADA
                    time.sleep(0.3)
                    print(f'La contraseña de \x1b[1;42m\x1b[1;30m{find_app}\033[;m es \x1b[1;42m\x1b[1;30m{listas_db[1][listas_db[0].index(find_app)]}\033[;m.\n')
                    salir()

        # ELIMINAMOS LA ÚLTIMA CONTRASEÑA QUE SE GUARDÓ DURANTE LA EJECUCIÓN DEL PROGRAMA
        elif option == 3:

            listas_db = enlistar_elementos()
            if new_app not in listas_db[0]:  # VERIFICAMOS QUE SE HAYA INCORPORADO UNA APP DURANTE LA EJECUCIÓN
                time.sleep(0.3)
                print('No se ha podido eliminar ya que durante la ejecución del programa no se ha guardado ninguna contraseña o porque la aplicación no está en el llavero.\n')
                salir()
            else:
                time.sleep(0.3)
                # PREGUNTAMOS SI ESTÁ SEGURO DE CONTINUAR Y LUEGO ELIMINA LOS ELEMENTOS DE LA BASE DE DATOS
                sure = input(f'Está seguro que desea eliminar la contraseña de \x1b[1;42m\x1b[1;30m{new_app}\033[;m?: [SI/NO]\n').upper()
                if sure == 'SI' or sure == 'S':
                    delete_sql(new_app)
                    salir()
                # SI SE ARREPIENTE O SE HA EQUIVOCADO Y NO DESEA ELIMINARLA PREGUNTAMOS SI DESEA REALIZAR OTRA OPERACIÓN
                else:
                    salir()

        # MODIFICAMOS LA CONTRASEÑA DE UNA APP EN NUESTRA BASE DE DATOS
        elif option == 4:
            time.sleep(0.3)
            # PREGUNTAMOS LA APLICACIÓN QUE DESEA MODIFICAR
            modify_app = input('Cuál es la aplicación que desea modificar su contraseña?:\n').capitalize()

            listas_db = enlistar_elementos()  # ENLISTAMOS LOS ELEMENTOS PARA BUSCAR Y MODIFICAR LOS VALORES
            if modify_app not in listas_db[0]:  # VERIFICAMOS QUE ESTE EN LA BASE DE DATOS 
                print('Lo sentimos, la aplicación elegida no está dentro de sus contraseñas.\n')
                salir()
            else:
                time.sleep(0.3)
                # PREGUNTAMOS POR LA POSIBILIDAD DE AUTOGENERAR LA CONTRASEÑA
                generar_password = input('Desea que generemos la contraseña automáticamente? : [SI/NO]\n').upper()
                if generar_password == 'S' or generar_password == 'SI':
                    change_password = generate_password()
                else:
                    change_password = password(listas_db[1])

                # LE OFRECEMOS LA POSIBILIDAD DE ENCRIPTAR
                encriptar = input('Desea encriptar su nueva contraseña?: [SI/NO]\n').upper()
                if encriptar == 'S' or encriptar == 'SI':
                    password_locked = encrypting(change_password)  # ENCRIPTAMOS LA CONTRASEÑA MODIFICADA
                    modify_sql(modify_app, password_locked, listas_db[1], listas_db[2])
                    salir()
                else:
                    modify_sql(modify_app, change_password, listas_db[1], listas_db[2])
                    salir()

       # OPCIÓN QUE IMPRIME TODOS LOS VALORES DE LAS LISTAS DE APLICACIONES Y PASSWORDS
        elif option == 5:
            imprimir_elementos()
            salir()

        # OPCIÓN PARA FINALIZAR EL PROGRAMA
        elif option == 0:
            break

        # CONDICIONAL QUE NOS EVITA UN ERROR Y VUELVE AL MENÚ PRINCIPAL SI LA OPCIÓN ELEGIDA NO ESTÁ EN LAS OPCIONES
        else:
            time.sleep(1)
            print('Lo sentimos, la opción elegida no está en el menú, vuelva a intentarlo.\n')