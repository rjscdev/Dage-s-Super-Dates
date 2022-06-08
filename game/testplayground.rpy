label testplayground:
    Robe '''
    Bienvenido a la zona de testeo, 
    
    aqui podras porbar diferentes mecanicas que estan implementadas dentro del proyecto.

    recuerda tocar y tratar de romper el juego de ser posible
    
    me ayudaras a detectar fallos y posibles bugs para que sean corregidos (aunque normalmente suelo corregir todo antes de enviar algo)

    asi que suerte testeando todo.
    '''

    menu Demo:
        "Qué deseas hacer?"
        "Cambio de nombre":
            jump namechange
        "Sistema de dia y noche":
            jump DNStest
        "salir":
            jump end

label namechange:
    player '''
    Hola mi nombre actual es {b}[PlayerName]{/b}

    pero lo puedes cambiar si deseas 
    '''
    menu cn:
        "{b}Qué deseas hacer?{/b}"
        "Cambiar el nombre":
            $ PlayerName = renpy.input("Cual es mi nuevo nombre?", default ="Jack")
            $ PlayerName = PlayerName.strip()
            if PlayerName == "":
                $ PlayerName = "Jack"

            player "Genial ahora mi nombre es [PlayerName]"

            Robe '''
            Este sistema puede ser utilizado para renombrar cualquier string de una variable dentro del juego 
            
            ya sea el nombre de un personaje, un objeto o un lugar.
            '''


            jump Demo
        "Nada":
            jump Demo

label DNStest:
    jump end