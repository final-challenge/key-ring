from administrador import get_question_and_responce, unlock_user

def unblock(usuario):

    # Query para obtener array del tipo [pregunta, respuesta]
    arr = get_question_and_responce()
    
    # Obtener pregunta y respuesta del array 
    question = arr[0]
    right_answer = arr[1]

    print("Por favor responda a su pregunta de seguridad para desbloquearla.")
    
    user_answer = input(f'{question}. (Escribir [exit] para salir): ')

    while True:
        if user_answer != right_answer:
            print("Incorrecto.")
            user_answer = input(f'{question}. (Escribir [exit] para salir): ')
        else:
            print("Su usuario ha sido desbloqueado. \n")
            unlock_user(usuario)
            break

   

