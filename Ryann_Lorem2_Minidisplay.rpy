
# I didn't make this code, it was done by EvilChaosKnight
# I also pretty much copied what Eval did for TDOMI, so I have no clue how this code works, so don't ask me
# All I did what change variable names to avoid possible conflict

screen ryannextrainfo:

    if ryannextradisplay == 2:
        add "image/ui/ryannextras2.png" at zoom_fade_in

    else:
        pass

    hbox at zoom_fade_in:
        xalign 0.03
        yalign 0.0

        if ryannextradisplay == 2:
#           add "image/ui/ryannextras2.png"
            text _("[ryannDisplayVar1name]{b} [ryannlDisplayVar1]{/b}[ryannDisplayVar1unit]\n[ryannDisplayVar2name] {b}[ryannDisplayVar2]{/b}[ryannDisplayVar2unit]") style "status_text"

        else:
            pass

