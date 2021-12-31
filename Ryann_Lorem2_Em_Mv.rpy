
label Ryann_Lorem2_Emera_Mav:

$ save_name = (_("LI - Emera"))

scene o4 with dissolveslow
$ renpy.pause (2.0)
play music "mx/basicguitar.ogg"
m "I woke up to sunlight on my face, but I refused to get up as I roughly knew what awaited me later."
c "(Why do beds feel so comfortable when you need to get up and do stuff?)"
$ renpy.pause (1.5)
c "(The sooner I get this over with, the sooner I dont have to think about it.)"
m "I reluctantly dragged myself out of bed, and while still half asleep, got ready to meet with Emera."

scene black with dissolveslow
play sound "fx/steps/clean.wav"
$ renpy.pause (1.0)
scene town5 with dissolveslow


m "I found myself outside the building where Emera worked. It was a bright and sunny day. Too bad I wouldn't get to enjoy it."
if katsuunplayed == False:
    m "Before I went inside I noticed Katsuharu on the other side of the park."
    c "..."
    c "(That dragon still owes me ice cream...)"
    $ renpy.pause (1.0)
    m "I ignored the thought and tried to focus on why I came here again."
    m "I walked inside and with some directions from the receptionist, I made my way to Emera's office."

else:
    m "I walked inside and with some directions from the receptionist, I made my way to her office."

scene corridor with dissolveslow
stop music fadeout (2.0)
m "I knocked on the door."
play sound "fx/knocking1.ogg"
$ renpy.pause (3.0)
Em "Come in."
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)
scene emeraroom with dissolveslow
show emera normal with dissolve
play sound "fx/door/door_close.ogg"
play music "mx/library.ogg"
$ renpy.pause (1.0)

Em "Ah, good day [player_name]."
c "Good morning Emera, your letter said you had something to discuss with me?"
Em ques "I see you’re getting straight to business."
$ renpy.pause (1.0)
Em normal "There was an in-depth investigation done over yesterday and the night before on the underground building, because of the... {w}situation with Reza."
Em "Due to water pockets surrounding the building, only just beyond the entrance could be examined carefully."
Em "The portal was examined as well, and it was found out that it is no longer functioning."
c "You mean it's broken?"
Em "Not in the way you think. The portal itself is properly functioning, but the coordinates to the human world are missing."
m "I obviously knew this already, but explaining how would definitely be difficult. {w}Playing dumb however, wasn’t. "
c "Really? How did this happen?"
Em ques "That is what we’re unsure of, and from that reaction, I'm assuming you are too."
Em normal "Which brings us to the point of this meeting."
Em frown "Because we cannot contact humanity, we are forced to revoke your ambassador status."
c "I see."
Em normal "But to repay you for your service, we will allow you to apply for citizenship, and let you keep your apartment, and have certain utilities subsidized."
c "Thank you, that will definitely be satisfactory."
Em "I'm glad it's to your liking, but you will have to fill in some paperwork before you leave."
c "I expected that, but before I start there’s something crucially important I must warn you about."
Em "What is it?"
c "Have you heard at all about a comet lately?"
Em ques "I am aware of it, it's path is projected to pass by the planet safely, if that’s what you were worried about."
c "Actually, it won't, according to my PDA, the comet will directly hit the planet causing a global extinction event if nothing is done about it."
show emera normal with dissolve
c "Thankfully, because the generator Reza tried to take wasn't damaged, it should supply enough power to safely divert it."
$ renpy.pause (2.3)
Em "I will have someone look into this matter, thank you for bringing it to my attention."
Em "Regardless, I do not want to keep you any longer, but as I said, there’s papers that must be filled."
show emera normal at left with move
$ renpy.pause (0.5)
play sound "fx/rummage3.ogg"
m "She walked over to a cabinet, and pulled out a huge stack of papers."
c "(I thought she said {i}some,{/i} but that looks like an encyclopedia.)"
show emera normal flip with dissolve
$ renpy.pause (0.3)
show emera at center with move
Em "These are the essentials: citizenship, health forms, property ownership..."
stop music fadeout (2.0)
scene black with dissolveslow
hide emera with dissolveslow
nvl clear
$ renpy.pause (1.0)
m "The next few hours were a blur, the only things I can recall were wrist pain, probably from the sheer amount of writing."
m "And a huge amount of trouble with health forms and citizenship, which clearly weren't meant for non-dragons."
$ renpy.pause (1.5)

scene town5 with dissolveslow
play music "mx/elegant.ogg"
m "Somehow, I managed to get it all done, but just as I was leaving..."

if brycedead == False:
    if ryannwindowssmashed > 0:
        m "I saw Bryce, who started walking over to me."
        if brycestatus == "good" or brycestatus == "neutral":
            show bryce normal b with easeinright
            Br "Hey [player_name]."
            c "Hey Bryce, what's up?"
            Br "Now that Reza’s been dealt with, it's much more peaceful then before. {w}But that’s not why I came over to you."
            c "What is it then?"
            Br stern b "We still need to have that chat about the window."
            c "Right..."
            Br normal b "Let’s go, it won't take that long."

        elif brycestatus == "none":
            show bryce normal b with easeinright
            Br "Hey [player_name]."
            c "Hey Bryce."
            Br stern b "I'll get straight to the point."
            Br "I'm sure you remember the incident with the window?"
            c "Yeah..."
            Br "We still need to talk about that, come on."

        else:
            show bryce stern b with easeinright
            Br "[player_name]."
            c "What is it?"
            Br "We need to have that discussion about your incident earlier."
            c "Incident?"
            Br " You smashing that window, come with me."
            c "Why should I?"
            Br "Because I was told you lost your ambassador status, and the perks that came with it."
            c "Wow, so you're threating me? Fine, let's just get this over with."

        scene black with dissolveslow
        $ renpy.pause (1.0)
        scene office with dissolveslow
        show bryce stern b with dissolve
        m "Bryce led me to the police station, then to his office."
        Br  "Sit down."
        play sound "fx/undress.ogg"
        $ renpy.pause (2.0)
        Br "So, since you’ve lost your ambassador status, I could charge you for anti-social behavior, disturbing the peace and vandalism."
        Br "But for stopping Reza, I’ll drop it this once."
        if brycestatus == "good" or brycestatus == "neutral" or brycestatus == "none":
            Br "Look, I dont want to be speaking down to you like a child, but I still had to report what happened, so it's either this, or getting arrested."
            Br "So..."
            scene black with dissolveslow
            hide bryce with dissolve
            $ renpy.pause (2.0)
            m "For the next roughly 15 minutes Bryce lectured me in a strict, yet still friendly tone, I still left even more tired than before."

        else:
            Br brow b "But still..."
            scene black with dissolveslow
            hide bryce with dissolve
            $ renpy.pause (2.0)
            m "Bryce proceeded to chew me out for the next half hour, I blocked out most of it, but still left with a headache and even more exhausted than before."

        $ renpy.pause (1.0)
        scene town6 with dissolveslow
        m "I was on my way home when I was suddenly called by Maverick."
        c "(Oh god, what now?)"
        $ renpy.pause (1.5)
        show maverick normal with easeinright
        $ renpy.pause (1.0)
        Mv "[player_name], I wanted to talk to you."
        Mv "I wanted to apologize."
        c "Oh, that’s not what I expected."
        Mv "In the underground building I saw your true intentions."
        Mv "I was wrong for assuming you were working with Reza. I misjudged you, and I'm sorry."
        Mv "I hope we can put this behind us."
        menu:
            "Accept his apology.":
                $ ryannmavapology = True
                c "Honestly, I don’t blame you for acting the way you did, from your point of view I can see why you were suspicious of me."
                Mv nice "I'm glad to hear that. I’ll be seeing you around then."
                show maverick nice flip with dissolve
                $ renpy.pause (0.2)
                hide maverick with easeoutright

            "You were out of line.":
                $ ryannmavapology = False
                c "Honestly, I still think you were out of line, you threatened and stalked me just because you had a hunch? Or was it just because of my species?"
                Mv angry "Fine, if that’s the way you’re going to be about it, forget it."
                show maverick angry flip with dissolve
                $ renpy.pause (0.2)
                hide maverick with easeoutright

    else:
        if brycestatus == "bad" or brycestatus == "abandoned":
            m "I saw Bryce and Maverick, but only Maverick walked over to me."
            $ renpy.pause (1.5)
            show maverick normal with easeinright
            Mv "[player_name], I wanted to talk to you."
            Mv "I wanted to apologize."
            c "Oh, that’s not what I expected."
            Mv "In the underground building I saw your true intentions."
            Mv "I was wrong for assuming you were working with Reza. I misjudged you, and I'm sorry."
            Mv "I hope we can put this behind us."
            menu:
                "Accept his apology.":
                    $ ryannmavapology = True
                    c "Honestly, I don’t blame you for acting the way you did, from your point of view I can see why you were suspicious of me."
                    Mv nice "I'm glad to hear that. I’ll be seeing you around then."
                    show maverick nice flip with dissolve
                    $ renpy.pause (0.2)
                    hide maverick with easeoutright

                "You were out of line.":
                    $ ryannmavapology = False
                    c "Honestly, I still think you were out of line, you threatened and stalked me just because you had a hunch? Or was it just because of my species?"
                    Mv angry "Fine, if that’s the way you’re going to be about it, forget it."
                    show maverick angry flip with dissolve
                    $ renpy.pause (0.2)
                    hide maverick with easeoutright      
        
        else:
            m "I saw Bryce and Maverick, and they both walked over to me."
            $ renpy.pause (1.5)
            show bryce normal b at Position(xpos = 0.15) with easeinright
            show maverick normal at Position(xpos=0.825) with easeinright
            show bryce normal b flip with dissolve
            Br "Hey [player_name]."
            c "Hey Bryce, and Maverick."
            Mv "Hey."
            $ renpy.pause (2.0)
            Br stern b flip "Well, what are you waiting for?"
            Mv angry "Alright, get off my back."
            Mv normal "[player_name], I wanted to apologize."
            show bryce normal b flip with dissolve
            Mv "In the underground building I saw your true intentions."
            Mv "I was wrong for assuming you were working with Reza. I misjudged you, and I'm sorry."
            Mv "I hope we can put this behind us."
            menu:
                "Accept his apology.":
                    $ ryannmavapology = True
                    c "Honestly, I don’t blame you for acting the way you did, from your point of view I can see why you were suspicious of me."
                    Mv nice "I'm glad that we can move on from this."
                    Br smirk b flip "See Maverick, it wasn't that hard."
                    Mv normal "Shut it Bryce."
                    Br laugh b flip "He's quite the charming fellow, isn't he [player_name]?"
                    Br normal b flip "I gotta go, I'm still on the clock, we'll see you around."
                    show maverick normal flip with dissolve
                    $ renpy.pause (0.3)
                    hide maverick with easeoutright
                    $ renpy.pause (0.2)
                    hide bryce with easeoutright

                "You were out of line.":
                    $ ryannmavapology = False
                    c "Honestly, I still think you were out of line, you threatened and stalked me just because you had a hunch? Or was it just because of my species?"
                    Mv angry "Fine, if that’s the way you’re going to be about it, forget it."
                    show maverick angry flip with dissolve
                    $ renpy.pause (0.3)
                    hide maverick with easeoutright
                    $ renpy.pause (1.0)
                    Br stern b flip "I understand you two didn't get along but did you have to say that?"
                    c "I just said what I thought, I didn't have to accept his apology."
                    Br "I know, but still, you could have just lied."
                    Br "Anyway, I'm still on the clock, I gotta go."
                    c "Bye."
                    hide bryce with easeoutright

else:
    m "I saw Maverick, who started walking over to me."
    $ renpy.pause (1.5)
    show maverick normal with easeinright
    Mv "[player_name], I wanted to talk to you."
    Mv "I wanted to apologize."
    c "Oh, that’s not what I expected."
    Mv "In the underground building I saw your true intentions."
    Mv "I was wrong for assuming you were working with Reza, I misjudged you, and I'm sorry."
    Mv "I hope we can put this behind us."
    menu:
        "Accept his apology.":
            $ ryannmavapology = True
            c "Honestly, I don’t blame you for acting the way you did, from your point of view I can see why you were suspicious of me."
            Mv nice "I'm glad to hear that, I’ll be seeing you around then."
            show maverick nice flip with dissolve
            $ renpy.pause (0.2)
            hide maverick with easeoutright

        "You were out of line.":
            $ ryannmavapology = False
            c "Honestly, I still think you were out of line, you threatened and stalked me just because you had a hunch? Or was it just because of my species?"
            Mv angry "Fine, if that’s the way you’re going to be about it, forget it."
            show maverick angry flip with dissolve
            $ renpy.pause (0.2)
            hide maverick with easeoutright


c "(Well that was unexpected.)"
scene black with dissolveslow
stop music fadeout (1.0)
$ renpy.pause (1.0)
scene np5e with dissolveslow
m "I proceeded to slowly make my way home, completely out of energy."
scene o3 with dissolveslow
m "I just collapsed onto the bed, not even attempting to get undressed or find a comfortable sleeping position."
scene black with dissolveslow
$ renpy.pause (3.0)

jump ryann_lorem2_ipsum


