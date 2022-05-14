'''
made by Robeshiri ⚙: https://github.com/rjscdev
📦 this archive define every character for the game and thier textsounds
'''

#textsounds functions
init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/B1.ogg", loop="True", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")

#characters list
define a = Character("test", callback=type_sound)
define b = Character("test2")