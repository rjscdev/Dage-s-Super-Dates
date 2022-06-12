screen Game_hud():
    style_prefix "Game_hud"
    text "Day {} ({}, {})".format(DayCount, WD[WDindex], TimeStamps[TimeIndex])

style Game_hudText:
    size 24 
    outlines [(absolute(3), "#222222", absolute(0), absolute(0))]


label DayScreen:
    show bg "sexo.png"
    centered "Day [DayCount]" with Dissolve(1.0)
    hide bg sexo
    return

style centered_text:
    size 50
    outlines [(absolute(3), "#222222", absolute(0), absolute(0))]