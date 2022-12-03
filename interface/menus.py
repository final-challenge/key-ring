from administrador import get_user_passwords, stored_user_email, get_pwd_by_user, delete_user
from unblock_option import unblock


# FALTA ESPECIFICAR BIEN LOS PARAMETROS DE LA OPCIONES DEL MENU 
def user_menu():
    print("Bienvenido al gestor de contraseñas.")
    while True:
        act = input("Seleccione la acción a realizar:\n"
                    "1) Ver contraseñas\n"
                    "2) Salir\n")
        if act == "1":
            get_user_passwords()
        elif act == "2":
            break


# FALTA ESPECIFICAR BIEN LOS PARAMETROS DE LA OPCIONES DEL MENU 
def admin_menu():
    print("Bienvenido al gestor de contraseñas.")
    while True:
        act = input("Seleccione la acción a realizar:\n"
                    "1) Bloquear usuario\n"
                    "2) Mostrar todas las aplicaciones y contraseñas\n"
                    "3) Filtrar aplicaciones y contraseñas por usuario\n"
                    "4) Borrar usuarios"
                    "5) Salir"
                    )
        if act == "1":
            usuario = input("Usuario a desbloquear.")
            if stored_user_email(usuario):
                unblock(usuario)            
        
        if act == "2":
            usuario = input("Usuario a consultar.")
            get_user_passwords(usuario)
        
        if act == "3":
            usuario = input("Usuario a consultar.")
            get_pwd_by_user(usuario)
        
        if act == "4":
            usuario = input("Usuario a consultar.")
            delete_user(usuario)
        
        if act == "5":
            break
