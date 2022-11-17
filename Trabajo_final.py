import mysql.connector

#PRIMERO CREAMOS LA DATABASE Y NOS CONECTAMOS A ELLA.
miConexion = mysql.connector.connect(host='localhost', user='root', passwd='123456789', db='llavero',
                                     auth_plugin='mysql_native_password')

# CREAMOS UNA VARIABLE QUE HARÁ DE CONECTOR PARA REALIZAR OTRAS FUNCIONES
cur = miConexion.cursor()

# CREAMOS LA TABLA. COMO PONEMOS "IF NOT EXISTS" A LA HORA DE CREARLA NO NECESITAMOS COMENTAR EL CÓDIGO O BORRARLO YA QUE NO LO VA A CREAR MÁS VECES
cur.execute('''CREATE TABLE IF NOT EXISTS user_pass (
            id  int(11)  NOT NULL   AUTO_INCREMENT  PRIMARY KEY,
            aplicacion  VARCHAR(50), 
            contraseña  VARCHAR(50) 
            ); ''')
miConexion.commit()

'''# CARGO LOS DATOS UNO POR UNO
cur.execute("INSERT INTO user_pass (aplicacion,contraseña) VALUES("+"'Gmail', '20051206Correo!')")
cur.execute("INSERT INTO user_pass (aplicacion,contraseña) VALUES("+"'Tinder', 'qwerasdf1234#')")
cur.execute("INSERT INTO user_pass (aplicacion,contraseña) VALUES("+"'Twitter', 'Tw2022+LMP')")
cur.execute("INSERT INTO user_pass (aplicacion,contraseña) VALUES("+"'Tiktok', 'Tik2022*VTP')")
cur.execute("INSERT INTO user_pass (aplicacion,contraseña) VALUES("+"'Instagram', 'Ins2022!MFR')")
cur.execute("INSERT INTO user_pass (aplicacion,contraseña) VALUES("+"'Canvas', 'Canvas12385!')")
miConexion.commit()
''' #ESTE CÓDIGO SI QUE LO COMENTO SINO CADA VEZ QUE CORRA EL PROGRAMA VOLVERÁ A CARGAR LOS MISMOS DATOS

# PROBANDO A ELIMINAR UN DATO Y VOLVERLO A AGREGAR
'''cur.execute("DELETE FROM user_pass WHERE aplicacion LIKE '%mail' ; ")
cur.execute("INSERT INTO user_pass (aplicacion,contraseña) VALUES("+"'Gmail', '20051206Correo!')")
miConexion.commit()'''

# PROBANDO FUNCION COUNT
'''cur.execute("SELECT COUNT(aplicacion) FROM user_pass")
for aplicacion in cur.fetchone():
    print(aplicacion)'''

# IMPRIMIR TODOS LOS ELEMENTOS DE LA TABLA

'''cur.execute("SELECT aplicacion, contraseña FROM user_pass")
for aplicacion,contraseña in cur.fetchall():
    print(aplicacion, contraseña)
'''

# CONTANDO CARACTERES DE CADA CONTRASEÑA (intente hacerlo con la función lenght de SQL y me devolvía error)
'''cur.execute("SELECT aplicacion, contraseña FROM user_pass")
for aplicacion,contraseña in cur.fetchall():
    print(aplicacion, len(contraseña))'''

#APLICANDO ENCRIPTAMIENTO CUANDO IMPRIMO LAS CONTRASEÑAS TRAIDAS DESDE LA DB.
'''codigo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
keyword = ['m', 'u', 'r', 'c', 'i', 'e', 'l', 'a', 'g', 'o']
cur.execute("SELECT aplicacion, contraseña FROM user_pass")
for aplicacion, contraseña in cur.fetchall():
    password_locked = ''
    for i in contraseña:
        if i in keyword:
            password_locked += codigo[keyword.index(i)]
        elif i in codigo:
            password_locked += keyword[int(i)]
        else:
            password_locked += i
    print(aplicacion, password_locked)'''