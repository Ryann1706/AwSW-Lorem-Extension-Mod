
label ryann_lorem2_rezaconfrontation:


$ renpy.pause (2.0)
m "None of us said anything in respone, or even moved."
m "I suddenly remember what Lorem said about the Ixomen Sphere."
play sound "fx/snarl.ogg"
show maverick rage flip with dissolve
m "All of a sudden Maverick charged, followed by Lorem, and I took out the Ixomen Sphere and prepared to throw it."
play sound "fx/rev.ogg"
$ renpy.pause (0.3)
play sound "fx/gunshot.wav"
show reza gunpoint with dissolve
m  "Reza was quick with his aim, shooting Maverick in the leg, causing him to stumble."
play sound "fx/flap1.ogg"
show lorem at right with move
show reza angry with dissolve
play sound "fx/loremkick.ogg"
hide lorem with dissolve
m "He also doged Lorem's charge, hitting them with a well-placed kick knocking him into a wall, which they then fell to the ground."
show loremwounded at Pan((1080, 0), (500, 350), 6) with fade
$ renpy.pause (4.5)
show reza gunself with dissolve
hide loremwounded with fade
play sound "fx/glassimpact.ogg"
m "I hurled the Ixomen Sphere in Reza's direction, which moved with supprising speed, hitting Reza right between the eyes, causing him to stagger back, dazed, and involuntarily toss his gun towards me."
show reza angry with dissolve
m "I picked it up, not wanting to take any chances, and unsure how to properly weild a gun, I just wildly fired in his direction."
play sound "fx/gunshots3.ogg"
$ renpy.pause (1.7)
play sound "fx/impact.wav"
m "Surprisingly, I hit every shot, and Reza slumped lifelessly against the wall."
show rezashotsixtimes at Pan ((1000, 626), (1280,0), 10.0) with fade # Shh no it was five
hide reza
show maverick normal flip
$ renpy.pause (8.5)
hide rezashotsixtimes with dissolve

m "I immediately went to check on Lorem. {w}They were unconscious, but didn't have any visible injuries which was a releif."
m "Maverick hobbled over to me."
Mv nice flip "Guess I was wrong about you."
c "Are you okay?"
Mv "Hurts like hell, but I'll live. {w}How is he?"
c "He's unconscious, but I think other than that he's fine."
Mv "I'll get help, you stay here and watch over him."
show maverick nice
$ renpy.pause (0.2)
hide maverick with easeoutleft

m "Maverick went to get help while I watched over Lorem, I checked on Reza, and unsuprisingly, he was dead."
m "He had an unanticipated amount of ammo on him though, much more needed for simple self-defence."
play sound "fx/door/hallwaydoor.ogg"
m "The sound of a door opening behind me snapped me out of my thoughts. {w}It was the Administrator."
hide izumi 
show izumi normal with dissolve
c "Hey Izumi, did you get lost on your way here, where were you?"
As "It's intresting that you remeber her name, even though you were nerver told it in this timeline."
c "{i}Her{/i} name? {w}What do you mean?"
m "A muffled sigh came from behind their mask."
As "You really haven't pieced it together yet? Height or voice not ring a bell?"
hide izumi with dissolve
m "The Administrator took off their mask to reveal... {w}{i}My face?{/i}"
show izumi normal with dissolve
c "But... How is this possible?"
"???" "To make a long story short, time travel is a hell of a lot more complicated than we initially thought."
"???" "The Izumi in this timeline died at some point, and since I was the person next in line with the most experience, I took her place."
"???" "She left behind a lot to help me, it's almost as if she expected this to happen at some point..."
"???" "Anyway, I carried out her plan just as she would, which unfortunately includeed deleting our home coordanates."
c "Why did you do that?"
"???" "Well, it was part of Izumi's plan and it was the most reliable way of stopping Reza from escaping with the generator we need to stop the comet."
"???" "But more importantly, we didn’t save our people too this time, so one of us has to go back."
c "Are you asking me or telling me? Because I'm pretty sure both of us want to stay here."
"???" "You were the one who was successful in their timeline, so it's only fair you get to choose."
"???" "As for my timeline..."
"???" "..."
"???" "It's better you don’t know."
"???" "Anyway, we don’t have much longer, it's your choice."
menu:

    "[[Go back.]":
        c "I’ll go back."
        "???" "Honestly, I'm surprised to hear that, but it's your choice."
        hide izumi with dissolve
        m "They took off their cloak and mask and handed them to me, and I started heading to the portal."
        $ renpy.pause (1.0)
        "???" "Don't worry, I'll look after Lorem."
        stop music fadeout 2.0
        $ renpy.pause (2.0)
        scene black with dissolveslow
        play sound "fx/system.wav"
        s "Congratulations! You abandoned Lorem while he was unconscious, hope you’re happy with yourself."
        jump mainmenu


    "[[Stay in this timeline.]":
        c "I’d prefer to stay here."
        "???" "It's strange, I expected that, yet I'm still disappointed. {w}I'll go tonight, but later, don’t want to draw suspicion by the portal being used."
        c "Good luck."
        "???" "Thanks, I'll need it..."
        m "They briskly walked out of the underground building, presumably into the forest and to Izumi's hideout."
        show izumi normal flip with dissolve
        $ renpy.pause (0.2)
        hide izumi with easeoutright
    
if brycedead == False:
    m "Soon after, Maverick returned with Bryce and some paramedics, who had already bandaged Maverick's wound, they proceded to check over me, and then bring Lorem to the hospital to be monitored."
    m "Bryce took mine and Maverick's statements, and escorted me back to my apartment."

else:
    m "Soon after, Maverick returned with some paramedics, who had already bandaged Maverick's wound, they proceded to check over me and then bring Lorem to the hospital to be monitored."
    m "I left after, and made my way back to my apartment."

stop music fadeout 2.0
scene black with dissolveslow
scene o3 with dissolveslow
$ renpy.pause (2.0)
m "Still quite shaken from the encounter with Reza, I just went straight to bed, hoping to proses everything in the morning."
$ renpy.pause (2.0)
scene black with dissolveslow

$ renpy.pause (3.0)

if player_name == "Thing":
    jump ryann_lorem2_spiteeval

else:
    jump ryann_lorem2_lorem6


        
