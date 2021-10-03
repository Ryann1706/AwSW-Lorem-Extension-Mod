
label ryann_lorem2_rezaconfrontation:


$ renpy.pause (1.0)
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
m "He also doged Lorem's charge, hitting him with a well-placed kick knocking him into a wall, which he then fell to the ground."
show loremwounded at Pan((1080, 0), (500, 350), 6) with fade
$ renpy.pause (4.5)
hide loremwounded with fade
show reza gunpoint with dissolve
play sound "fx/glassimpact.ogg"
m "I hurled the Ixomen Sphere in Reza direction, witch moved with supprising speed, hitting Reza right between the eyes, causing him to stagger back, dazed, and involuntarily toss his gun towards me."
show reza angry with dissolve
m "I picked it up, and not wanting to take any chances, and unsure how to properly weild a gun, I just wildly fired in his direction."
play sound "fx/gunshots3.ogg"
$ renpy.pause (1.0)
m "Surprisingly, I hit every shot, and Reza slumped lifelessly against the wall."
show rezashotsixtimes at Pan ((1000, 626), (1280,0), 10.0) with fade # Shh no it was five
hide reza
$ renpy.pause (8.5)
hide rezashotsixtimes with dissolve

m "I immediately went to check on Lorem. {w}He was unconscious, but didn't have any visivble injuries which was a releif."
m "Maverick hobbled over to me."
Mv nice flip "Guess I was wrong about you."
c "Are you okay?"
Mv "Hurts like hell, but I'll live. {w}How is he?"
c "He's unconscious, but I think other than he's fine."
Mv "I'll get help, you stay here and watch over him."
show maverick nice
$ renpy.pause (0.2)
hide maverick with easeoutleft

m "Mavrick went to get help while I watched over Lorem, I check on Reza, and unsuprisingly, he was dead."
m "He had an unanticipated amount of ammo on him though, much more needed for simple self-defence."
play sound "fx/door/hallwaydoor.ogg"
m "The sound of a door opening behind me snapped me out of my thoughts. {w}It was the Administrator."
hide izumi with dissolve
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
"???" "The Izumi in this timeline died at some point and since I was the person next in line with the most experience, I took her place."
"???" "She left behind a lot to help me, it's almost as if she expecteed this to happen at some point..."
"???" "Anyway, I carried out her plan just as she would which, unfortunately includeed deleting our home coordanates."
c "Why did you do that?"
"???" "Well, it was part of Izumi's plan and it was the most reliable way of stopping Reza from escaping with the generator we need to stop the comet."
"???" "But more importantly, we didn’t save our people too this time, so one of us has to go back."
c "Are you asking me or telling me? Because I'm pretty sure both of us want to stay here."
"???" "You were the one who was successful in their timeline, so it's only fair you get to choose."
"???" "As for my timeline..."
"???" "..."
"???" "Its better you don’t know."
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
        "???" "Its strange, I expected that, yet I'm still disappointed. {w}I'll go tonight, but later, don’t want to draw suspicion by the portal being used."
        c "Good luck."
        "???" "Thanks, I'll need it..."
        m "They briskly walked out of the underground building, presumably into the forest and to Izumi's hideout."
        show izumi normal flip with dissolve
        $ renpy.pause (0.2)
        hide izumi with easeoutright
    

m "Soon after, Maverick returned with Bryce and some paramedics, who had already bandaged Maverick's wound, they proceded to check over me and them bring Lorem to the hospital to be monitored."
m "Bryce took mine and Maverick's statements and escorted me back to my apartment."
stop music fadeout 2.0
$ renpy.pause (2.0)
scene black with dissolveslow

Rn "Well I hope you enjoyed the mod, because right now thats all there is."
Rn "I am planning on finishing it but it'll probely be a while before its completly finished."
Rn "Also, if you find any bugs or have any ideas on what I should add, message me on discord at Ryann1706#2372."

if player_name == "Thing":
    Rn "Hopefully this is working right."
    Rn "If it is, this should be a personal message for Eval."
    Rn "I wanted to say thanks for helping test my mods for me."
    Rn "Also (as of writing this) the score for bug finding is Ryann:100+ to Eval:5."
    Rn "And I bet you wont be able to overtake me by the time i've fully finished this mod."
    Rn "Also make more mods so I can have even more of a lead."



elif player_name == "Jakzie":
    Rn "Hopefully this is working right."
    Rn "If it is, this should be a personal message for Jakzie"
    Rn "I just wanted to say thanks for helping me with my code. I really appreciate it."
    Rn "Also, I hope I didn’t annoy you with how often I messaged you."
    Rn "If there's any way to repay the favor let me know."

else:
    pass

jump mainmenu
        
