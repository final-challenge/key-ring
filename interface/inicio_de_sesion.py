from administrador import is_user_blocked, block_user, stored_user_email, stored_pwd, create_user 
from menus import user_menu, admin_menu
from password_checker import policy 
from unblock_option import unblock
import hashlib


def signup():

    while True:
        user_email = input("Usuario: ")

        # Si el usuario ya existe en la base de datos 
        if stored_user_email(user_email) == user_email:
            print('Este usuario ya existe')
        else:    
            break
    
    while True:
        pwd = input("Contraseña: ")
        conf_pwd = input("Confirmar contraseña: ")

        # Si ambas contraseñas no coinciden  
        if conf_pwd != pwd:
            print("Las contraseñas no son iguales")
        # Si la contraseña no es fuerte
        elif policy.test(pwd) != []:
            print(f'La contraseña debe tener: {policy.test(pwd)}')

            
        else:
            # Hashea la contraseña
            enc_pwd = pwd.encode()
            hashed_pwd = hashlib.sha256(enc_pwd).hexdigest()

            # Crear Usuario  
            create_user(user_email, hashed_pwd)
            print('Su usuario se ha creado con éxito')
            break



def login():
    # Contador de intentos 
    tries = 0
    
    # Mientras el numero de intentos sea menor a 3, itera
    while tries < 3:
        
        user_email = input("Usuario: ")
        pwd = input("Enter password: ")
        
        # Encriptar password 
        auth = pwd.encode()
        auth_hash = hashlib.sha256(auth).hexdigest()
        
        #  Expression for right or user
        right_credentials = user_email == stored_user_email(user_email) and auth_hash == stored_pwd(user_email)

        # Si el usuario no existe en la base de datos 
        if stored_user_email(user_email) != user_email:
            print('Este usuario no existe')

        # Si el usuraio esta bloqueado
        if is_user_blocked(user_email): 
            print("Su usuario está bloqueado.")
            # Opcion de desbloqueo de usuario
            unblock(user_email)

        # Si usuario y password son correctos 
        if right_credentials:
            #  Si el usuario no es admin 
            if user_email != "admin":
                # Despliega el menu para usuarios default
                user_menu()
                # Sal del loop
                break 
            # De lo contrario  
            else:
                # Despliega el menu para usuarios administradores
                admin_menu()
                # Sal del loop
                break

        # Suma un intento
        tries += 1
        print(tries)
            
        # Si el contador llega a 3 intentos, bloquea el usuario 
        if tries == 3:
            block_user(user_email)
            print("Su usuario ha sido bloqueado. \n")
            unblock(user_email)
            break
        


# Menú vía terminal de comandos 
while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")

    option = input("Enter your choice: ")
    if option == "1":
        signup()
    elif option == "2":
        login()
    elif option == "3":
        break
    else:
        print("Choose a valid option")
