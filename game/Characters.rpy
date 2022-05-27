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

    def aasd(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/tick_004.ogg", loop="True", channel ="sound")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")

#characters list
define Robe = Character ("Robeshiri", callback = aasd)
define J = Character("Jack")
define B = Character("Bruno", callback = type_sound)