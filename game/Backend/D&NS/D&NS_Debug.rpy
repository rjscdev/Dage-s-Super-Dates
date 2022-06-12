##########################
# made by Robeshiri ⚙: https://github.com/rjscdev
##########################

###########################
# D&NS debug ⚙📝
##########################
default DNSDebug = "Testing value"
screen DebugWindow:
    text "[DNSDebugtxt]":
        xalign 1.0
        color "#ffff"
        outlines [(absolute(2), "#2b2b2bff", absolute(0), absolute(0))]
        size 24

label UptDebugText:
    if DNSDebug_enable == True:
        $ DNSDebugtxt = "Debug Mode: Day is:" + str(DayCount) + ", Time is:" + str(TimeIndex)
        return 