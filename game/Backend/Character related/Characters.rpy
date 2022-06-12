##########################
# made by Robeshiri ⚙: https://github.com/rjscdev
##########################

##########################
#Characters 👥📦
##########################

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
define player = Character("[PlayerName]")
define B = Character("Bruno", callback = type_sound)

