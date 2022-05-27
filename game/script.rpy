# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    Robe '''
    esta es una {b}demo{/b} para {st}{b}testear{/b}{/st} el {b}{i}{Grd=#7a54f7-#582e80}sistema de texto{/Grd}{/i}{/b} que he creado

    tambien con una pequeña parte de la introduccion para testear el mismo sistema.

    el sistema de dia y noche sigue en desarrollo dado que el anterior resulto fallando.

    por lo pronto esto es lo que hay, talvez no sea mucho pero es trabajo de calidad

    {glitch= 50}{st}{b}ademas no es que hagan su trabajo, pinche bola de huevones de mierda{/st}{/glitch}
    '''

    menu Demo:
        "Demo"
        "Introduccion":
            jump introduccion
        "cerrar":
            pass
        
    # This ends the game.
label end: 
    return
