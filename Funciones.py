#----------------------------------------CREACIÓN DE FUNCIONES---------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
# FUNCIÓN QUE SE CONECTA A LA BASE DE DATOS E INSERTA UN DATO. RECIBE COMO PARÁMETROS LOS DATOS QUE DESEA INCORPORAR
def insert_sql(dato1, dato2, dato3):
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()
    insert = """INSERT INTO user_pass (aplicacion, contraseña, contraseña_encriptada) VALUES(%s, %s, %s)""" 
    cur.execute(insert, (dato1, dato2, dato3))
    miConexion.commit()
    miConexion.close()
    if dato3 != None:
        print(f'La contraseña \x1b[1;42m\x1b[1;30m{dato3}\033[;m ha sido encriptada y guardada con éxito.\n')
    else:
        print(f'La contraseña \x1b[1;42m\x1b[1;30m{dato2}\033[;m ha sido guardada con éxito.\n')

# FUNCIÓN QUE SE CONECTA A LA BASE DE SQL Y DEVUELVE UNA LISTA CON DOS LISTAS DENTRO CON LOS ELEMENTOS DE LA BASE DE DATOS. NO RECIBE NINGÚN PARÁMETRO
def enlistar_elementos():
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()
    aplicaciones = []
    passwords = []
    passwords_encriptadas = []
    cur.execute("""SELECT aplicacion, contraseña, contraseña_encriptada FROM user_pass""")
    for aplicacion, contraseña, contraseña_encriptada in cur.fetchall():
        aplicaciones.append(aplicacion)
        passwords.append(contraseña)
        passwords_encriptadas.append(contraseña_encriptada)
    miConexion.close()    
    return [aplicaciones, passwords, passwords_encriptadas]

# FUNCIÓN QUE SE CONECTA A LA BASE DE SQL E IMPRIME TODOS LOS ELEMENTOS GUARDADOS EN ESTA. NO RECIBE NINGÚN PARÁMETRO
def imprimir_elementos():
    import mysql.connector
    import time
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()
    cur.execute("""SELECT aplicacion, contraseña, contraseña_encriptada FROM user_pass""")
    for aplicacion, contraseña, contraseña_encriptada in cur.fetchall():
        if contraseña_encriptada != None:
            print(f'La contraseña encriptada de \x1b[1;42m\x1b[1;30m{aplicacion}\033[;m es \x1b[1;42m\x1b[1;30m{contraseña_encriptada}\033[;m', end= time.sleep(0.3))
        else:
            print(f'La contraseña encriptada de \x1b[1;42m\x1b[1;30m{aplicacion}\033[;m es \x1b[1;42m\x1b[1;30m{contraseña}\033[;m', end= time.sleep(0.3))
    miConexion.close()    

# FUNCIÓN QUE SE CONECTA A LA BASE DE SQL Y ELIMINA EL ÚLTIMO ELEMENTO QUE SE GUARDÓ EN LA BASE DURANTE LA EJECUCIÓN DEL PROGRAMA.
def delete_sql(app):
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()
    delete = "DELETE FROM user_pass WHERE aplicacion = %s"
    cur.execute(delete, [app])
    miConexion.commit()
    miConexion.close()
    print(f'La aplicación \x1b[1;42m\x1b[1;30m{app}\033[;m y su contraseña han sido eliminadas del llavero.\n')
    app = ''
    return app

# FUNCIÓN QUE SE CONECTA A LA BASE DE SQL Y MODIFICA UN REGISTRO. USA COMO PARÁMETRO DOS VARIABLE, LA app QUE LE DETERMINA CUÁL ES LA FILA QUE DESEAMOS MODIFICAR Y LA passwd QUE DETERMINA EL NUEVO VALOR.

###### PARA CONSEGUIR MODIFICARLA TENGO QUE CAMBIAR ALGO; JUGAR CON EL INDICE O CON EL ID PERO ALGO SE TIENE QUE CAMBIAR
def modify_sql(app, passwd, lista_passwd1, lista_passwd2):
    import mysql.connector
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                         auth_plugin='mysql_native_password')
    cur = miConexion.cursor()
    modify = "UPDATE user_pass SET contraseña = %s, contraseña_encriptada = %s WHERE aplicacion = %s"
    modify_encrypted = "UPDATE user_pass SET contraseña = %s, contraseña_encriptada = %s WHERE aplicacion = %s"
    if passwd in lista_passwd1:
        cur.execute(modify_encrypted, [None, passwd, app])
        miConexion.commit()
    elif passwd in lista_passwd2:
        cur.execute(modify, [passwd, None, app])
        miConexion.commit()
    miConexion.close()
    print(f'La contraseña de \x1b[1;42m\x1b[1;30m{app}\033[;m ha sido modificada con éxito.')
    
# FUNCIÓN CREADA PARA SALIR DEL PROGRAMA
def salir():
    continuar = input('Desea realizar otra operación?: [SI/NO]\n').upper()
    if continuar == 'NO' or continuar == 'N':
        return quit()

# FUNCIÓN QUE VERIFICA SI LA APLICACION EXISTE EN EL LLAVERO. RECIBE DE PARAMETRO UNA VARIABLE LA LISTA DONDE BUSCAR
# def verificar_app(lista):
#     app = input('Cuál es la aplicación que desea incorporar?:\n').capitalize()
#     if app in lista:  # VERIFICAMOS QUE LA APLICACIÓN NO SE HAYA GUARDADO ANTES
#         print('La aplicación ya se encuentra dentro de su llavero de contraseñas.\n')
#         salir()
#     else:
#         return app

# FUNCIÓN QUE CREA UNA CONTRASEÑA GENÉRICA SELECCIONANDO UNA CANTIDAD PREDETERMINADA DE CARACTERES, LETRAS Y NÚMEROS QUE ESTÁN DEFINIDOS EN UNA STRING UTILIZANDO LA LIBRERÍA RANDOM LA FUNCIÓN CHOICE.
# DEVUELVE UNA VARIABLE CON LA CONTRASEÑA QUE SE HA GENERADO.
def generate_password():
    import random
    valores = '0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ-+¿?!#$%&/=?¡*_'
    genereted_pass = ''.join(random.choices(valores, k=10))
    return genereted_pass

# FUNCIÓN QUE PIDE AL USUARIO QUE INTRODUZCA UNA CONTRASEÑA Y LA REPITA HASTA QUE LA INTRODUCE CORRECTAMENTE 2 VECES.
# RECIBE COMO PARÁMETRO UNA LISTA DONDE VERIFICA QUE LA CONTRASEÑA NO ESTÉ REPETIDA
# DEVUELTE UNA VARIABLE CON LA CONTRASEÑA INTRODUCIDA.
def password(lista1):
    while True:
        new_password = input('Ingrese la password:\n')
        repeat_password = input('Repita la password:\n')
        if new_password != repeat_password:
            print('Lo siento, las passwords no coinciden. Vuelva a intentarlo.\n')
        else:
            if new_password in lista1:  # SI LA CONTRASEÑA ESTÁ EN NUESRTA LISTA LO INTENTAMOS DE NUEVO
                print('La contraseña escogida ya está dentro de su llavero, por su seguridad mejor elija una nueva.\n')
            else:
                break
    return new_password

# FUNCIÓN QUE ENCRIPTA O DESENCRIPTA EL TEXTO QUE SE LE INTRODUZCA. SE COMPONE DE DOS LISTAS CON LAS CUALES SE ENCRIPTARÁ Y UNA VARIABLE VACÍA PARA RELLENAR CON UN BUCLE FOR DE ACUERDO SE QUIERA ENCRIPTAR O DESENCRIPTAR.
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

'''VOLVER A METER AL FINAL BOSS'''


