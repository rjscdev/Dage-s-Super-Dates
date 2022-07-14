###########################
# Repeating Actions 🔄⚙📦
# Notes📑
# these options are called based on the contents of TimeStamps on the D&NS_config.rpy
# the default values are in the list, if you add more create "label show_yourValue_options:"
##########################

label show_morning_options:
    scene bg "morning"
    with dissolve

    player "muy bien, veamos que tenemos aqui"
    menu:
        "opcion de prueba":
            player "esta es una opcion de prueba"
        "presioname":
            player "vaya, si que eres curioso"
            "estas opciones se estaran repitiendo por todos los dias asi que si quieres salir, elige la tercer opcion"
        "Salir":
            jump Demo

label show_noon_options:
    scene bg "noon"
    with dissolve

    player "Bien que deberia hacer hoy?"
    menu: 
        "Hacerte el pendejo un rato":
            player "No hay nada como perder el tiempo"

        "Salir del ciclo":
            player "Muy bien creo que fue demasiado testeo por hoy"
            "Regresaras al playground de testeo"
    return

label show_evening_options:
    scene bg "evening"
    with dissolve

    player "Bien que deberia hacer hoy?"
    menu: 
        "Hacerte el pendejo un rato":
            player "No hay nada como perder el tiempo"

        "Salir del ciclo":
            player "Muy bien creo que fue demasiado testeo por hoy"
            "Regresaras al playground de testeo"
    return

label show_night_options:
    scene bg "night"
    with dissolve

    player "Bien que deberia hacer hoy?"
    menu: 
        "Hacerte el pendejo un rato":
            player "No hay nada como perder el tiempo"

        "Salir del ciclo":
            player "Muy bien creo que fue demasiado testeo por hoy"
            "Regresaras al playground de testeo"
    return