##########################
# made by Robeshiri ⚙: https://github.com/rjscdev
##########################

###########################
# Repeating Actions 🔄⚙📦
##########################

label dawn_options:
    scene bg "placeanight.jpg"
    with dissolve

    player "muy bien, veamos que tenemos aqui"
    menu:
        "opcion de prueba":
            player "esta es una opcion de prueba"
        "presioname":
            player "vaya, si que eres curioso"
            "estas opciones se estaran repitiendo por todos los dias asi que si quieres salir, elige la tercer opcion"
        "Salir":
            $ stopTimeCycle
            jump Demo
    return
label morning_options:
    scene bg "placeamorning.jpg"
    with dissolve

    player "Bien que deberia hacer hoy?"
    menu: 
        "Hacerte el pendejo un rato":
            player "No hay nada como perder el tiempo"
            $ Energy += 1
        "Salir del ciclo":
            player "Muy bien creo que fue demasiado testeo por hoy"
            "Regresaras al playground de testeo"
    return
label noon_options:
    player "Creo que fue demasiado testeo, dejemoslo por aqui"
    $ stopTimeCycle = True
jump Demo
label evening_options:
label sunset_options:
label night_options:
label midnight_options: