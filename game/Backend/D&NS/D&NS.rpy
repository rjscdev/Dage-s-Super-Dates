##########################
# made by Robeshiri ⚙: https://github.com/rjscdev
# 📦this are the text effects for the dialogs
##########################

###########################
# Day & Time System 📆⏳📦
##########################
default stopTimeCycle = False
init python:
    def AdvTime(periods=1):
        global TimeIndex, WDindex, DayCount
        TimeIndex += periods

        #when a day has passed this function resets the TimeIndex to its default value
        # ad increases time variables such as WDindex and Daycount
        while TimeIndex >= len(TimeStamps):
            TimeIndex -= len(TimeStamps)
            WDindex += 1
            DayCount += 1

        #when a day has passed, resets WDindex to its defaul value
        while WDindex >= len(WD):
            WDindex -= len(WD)
label DNSLoop:
    if (TimeIndex == 0):
        call DayScreen
    
    if [DayCount, TimeIndex] in Events: #this function calls an event[Day]_[Time] if exist in the Events.rpy file
        $ labelName ="event"+str(DayCount)+"_"+str(TimeIndex)
        call expression labelName
        
    # this makes the game end if the time cycle is stoped 
    if stopTimeCycle == True:
        return

    #this makes the time advances everytime when we return to the DNSloop
    call DNS_CycleChange
    $ AdvTime()
    
label DNS_CycleChange:
    $ CycleIndex = 0
    while CycleIndex < len(TimeStamps):
        if CycleIndex == TimeIndex:
            $ CurrentTime = TimeStamps[CycleIndex].lower()
            $ labelName= CurrentTime+"_Options"
            call expression labelName
        $ CycleIndex += 1
        return