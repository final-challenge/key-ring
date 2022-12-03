# tipo del valor que retorna una funcion : -> 
# -> void : No retorna nada
import hashlib


# Pregunta a la DB si un usuario está bloqueado -> boolean
def is_user_blocked(user):
    pass 

# Bloquea un usuario -> void 
def block_user(user):
    pass 

# Pregunta a la DB por la password de un usuario dado -> string
def stored_pwd(user):
    pwd = '123'
    enc_pwd = pwd.encode()
    hashed_pwd = hashlib.sha256(enc_pwd).hexdigest()
    return hashed_pwd

# Crea un usuario en la DB -> void
def create_user(user, password):
    pass 

# Mostrar todas las apps y passwords del usuario -> dict
def get_user_passwords(user):
    pass 

# Buscar un usuario dado en la DB y retornarlo si existe -> string | none
def stored_user_email(user):
    return 'user0' 

# Obtener todas las passwords de un usuario -> dict
def get_pwd_by_user(user):
    pass 

# Borrar un usario -> void
def delete_user(user):
    pass 

# Desbloquear un usuario -> void
def unlock_user(user):
    pass 

# Obtener la pregunta de seguridad y la respuesta -> list
def get_question_and_responce():
    return ['This is','a test']



