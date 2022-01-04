
label ryann_lorem2_lo7_start:

$ save_name = (_("LI - Lorem 7"))

scene o4 with dissolveslow
$ renpy.pause (2.0)
play music "mx/cruising.ogg"

m "I woke up normally, like every other day."
c "(Another day, another morning I have no idea what to do.)"
c "(Ipsum said Lorem wanted to hang out again soon, so we can do that, assuming they aren't working.)"
$ renpy.pause (1.5)
play sound "fx/phonepickup.ogg"
$ renpy.pause (0.5)
play sound "fx/phonering.ogg"
$ renpy.pause (3.5)
stop sound 
Lo "Hello?"
c "Hey Lorem, it’s [player_name]."
Lo "Hey! Did you forget something the last time you called?"
c "No, Ipsum told me you wanted to hang out soon, and I wanted to let you know I'm free today."
Lo "Great, so am I! Is it alright if I come over later then?"
c "Sure, that’s fine with me."
Lo "I’ll see you soon then."
$ renpy.pause (0.5)
play sound "fx/phonepickup.ogg"
$ renpy.pause (1.0)

scene black with dissolveslow
$ renpy.pause (1.0)
scene o with dissolveslow
$ renpy.pause (1.5)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)
show lorem normal with dissolve
c "Hey Lorem."
Lo "Hey [player_name], can I come in?"
c "Of course."
play sound "fx/door/door_close.ogg"
$ renpy.pause (1.0)

c "So, is there any reason specifically you wanted to meet up again so soon?"
Lo "Do I need a reason to hang out with you?"
c "I guess not."
Lo think "By the way, Ipsum told me you two hung out yesterday, how did that go?"
c "It was actually a lot more fun than I thought it would be."
Lo normal "That's good to hear, I'm glad that you two are able to get along as well."
Lo think "So, what did both of you get up to?"
c "Well, Ipsum wanted to run a few tests on me and get some samples to study, so we met at the production facility before his shift."
Lo normal "That explains why he didn’t leave his room at all of yesterday and today, and why he left pretty soon after you called him."
Lo relieved "But you didn’t have to agree to doing that, you know that right?"
c "But I wanted to. It's not like he forced me, and it’s not the only thing we did anyway."
Lo normal "Ah, did he involve you in one of his pranks?"
c "Yeah."
Lo "He’s infamous for doing stuff like that, yet he never gets caught, it's honestly pretty impressive."
Lo "Anyway, there is something I wanted to do though. I wanted you to experience what actually good-quality pizza is like, not that cheap Pantoli’s stuff."
c "Alright, but I gave Ipsum his Ixomen Sphere yesterday too, so how are you gonna order it?"
Lo think "Ipsum also told me that, so I brought one of their menus with me."
play sound "fx/paper.wav"
m "Lorem unfolded one of their wings and took the menu out, putting it on the coffee table for us both to see."
Lo "I think I’ll have salad again, what topping do you want this time?"
c "Are we splitting this pizza too?"
Lo relieved "Like I said, this is better quality, which means it's more expensive, and the smallest size is still too big for me, so yes, we’re splitting it again."
show lorem normal with dissolve
m "Just from looking at the menu and it's vast amount of toppings, I could tell this wasn’t cheaply made like Pantoli’s."
m "Not knowing more than half the things on the menu, I decided to play it safe and order something I at least recognized."
menu:
    "Pepperoni":
        $ ryannpizzatopping = "pepperoni"
        c "(Can't go wrong with pepperoni.)"
        c "I’ll have peperoni."
        Lo normal "Ah, a classic, I'm tempted to get that now too."
        c "Will you?"
        Lo "I’ll stick with salad, and maybe steal one of your slices."
        c "Or you could just ask for one."
        Lo happy "But that’s not nearly as fun."

    "Chicken":
        $ ryannpizzatopping = "chicken"
        c "(I didn’t know they also had chickens here...)"
        c "I’ll have chicken."
        Lo think "Are chickens animals humans are familiar with?"
        c "We have an animal with the same name, so I'm assuming it is the same, or at least similar."

    "Salad":
        $ ryannpizzatopping = "salad"
        c "(So, salad on pizza isn't just a Pantoli thing...)"
        c "I’ll have salad too."
        Lo normal "Good choice."

    "Pineapple":
        $ ryannpizzatopping = "pineapple"
        c "(I wonder if humans and dragons share the same view about pineapple on pizza?)"
        c "I’ll have pineapple."
        Lo think "You actually like pineapples on pizza?"
        c "(Apparently, we do...)"
        c "And, what's wrong with that? I don’t think salad on pizza would be very appealing."
        Lo "There’s nothing wrong with it, I just think it’s a bit weird."


m "Afterwards, Lorem ordered the pizza and we just had to kill time before it arrived."
c "You said that pizza was expensive, but how expensive?"
Lo relieved "All I’ll say is, I'm happy I worked overtime the past two days to make up for the one I missed."
c "You didn’t have to spend that much for me."
Lo normal "With how much you’ve done for me, it’s the least I could do."

m "There was a moment of silence between us, then I noticed Lorem glancing around the room as if they were searching for something."
c "Are you looking for something?"
Lo think "Yeah, do you not have a TV in your apartment?"
c "No, it's been like this since the day I’ve arrived here, which included no TV."
Lo "That seems a bit odd, pretty much every apartment here has a TV, why not yours?"
c "Maybe to avoid culture shock, but they still gave me books, so I don’t really know."
Lo "I don’t think we’ll know for certain, the reason I was looking was because the pizza might take a while to get here."
Lo normal "You gave Ixomen back his Ipsum Sphere, so there isn't much to do except read, huh?"
$ renpy.pause (1.0)
show lorem shy with dissolve 
$ renpy.pause (1.0)
Lo "Uh... Forget you heard that."
menu:
    "You’re adorable.":
        $ rnloremromance += 1
        c "You’re so adorable."
        Lo "R-Really...?"
        $ renpy.pause (1.0)
    
    "Forget you said what?":
        c "Forget you said what?"
        Lo normal "Exactly."
        $ renpy.pause (0.5)
    
    "I'm telling Ipsum about that.":
        c "I'm telling Ipsum you said that."
        Lo relieved "Please don’t, he’ll never let me live it down..."
        c "I'm kidding, I won't... {w}probably."
        $ renpy.pause (0.5)


Lo normal "Uh, anyway, there has to be something for us to do while we wait."
c "Actually, there's something I wanted to ask you."
Lo think "What is it?"
c "You’re making your own game, so I'm assuming you know a lot about video games."
Lo normal "Just a lot? I’ve been playing video games for most of my life, go ahead and ask anything."
c "I actually wanted to know what video games are like for dragons in general, and how similar they are to human ones."
Lo happy "Oh, well where do I begin..."
scene black with dissolve
m "Lorem proceeded to tell me in depth about dragon video games, some descriptions and names sounding so similar I could have been fooled that they were cheap knock-offs of previously existing human games."
play sound "fx/door/doorbell.wav"
m "We got so in-depth we lost track of time, and before we knew it the doorbell rang."
scene o with dissolve
m "Lorem got up to answer it and returned with the pizza."
show lorem normal flip with easeinleft
$ renpy.pause (0.3)
show lorem normal with dissolve
Lo think "That got here pretty quick."
c "Or we just probably got distracted."
Lo normal "Either way, it's here now."

if ryannpizzatopping == "salad":
    m "Lorem brought the pizza to the coffee table, and as expected, it was covered with a salad."
else:
    m "Lorem brought the pizza to the coffee table, and as expected, it was half salad and half [ryannpizzatopping]."

play sound "fx/pizzabite.ogg"
m "Me and Lorem bit into our pizza at the same time..."

if ryannpizzatopping == "pepperoni":
    m "And it was amazing! The juiciness of the pepperoni mixed with the freshness of the cheese and sauce, and the crust toasted to perfection was on a whole other level."

elif ryannpizzatopping == "chicken":
    m "And it was amazing! The slight, yet flavorful difference with the chicken, the freshness of the cheese and sauce, and the crust toasted to perfection was on a whole other level."

elif ryannpizzatopping == "salad":
    m "And it was really good! Salad on a pizza was definitely something I wasn’t used to, yet the fresh crispiness of the vegetables combined with the freshness of the cheese and sauce, and the crust toasted to perfection was on a whole other level."

elif ryannpizzatopping == "pineapple":
    m "And it was really good! The tangy yet fruity punch from the pineapple combined with the freshness of the cheese and sauce, and the crust toasted to perfection was on a whole other level."

m "I looked to Lorem, who was also enjoying the complete bliss from the astounding food."
c "I think normal pizza will be ruined for us now."
Lo happy "Definitely, but it's so worth it."
$ renpy.pause (1.5)
show lorem think with dissolve 
m "I continued eating, completely captivated by the pizza, but I snapped out of it when I noticed Lorem gazing out the window, fixated on something."
c "What are you looking at?"
Lo "Huh? Oh, I was just looking at the portal, I was thinking about the underground building attached to it."
Lo "I know we were there when Reza was, but we barely saw any of it, and being there at all made me really curious what else could be in there."
c "Actually, there was an investigation done after what happened with Reza, that’s when it was found out that the portal is broken."
Lo sad "Oh, [player_name], I'm really sorry for bringing that up..."
c "Lorem, don’t worry about it, like I said before, I'm fine."
Lo "I know... But still, sorry."
$ renpy.pause (1.5)
c "If you really are curious what's down there, maybe we could go check?"
Lo think "Are we allowed to do that?"
c "Probably not, but the portal does have some connection to humanity, and as far as I'm aware the investigation is done, so as long as we’re quick it should be fine."
c "Also, remember I told you about the comet a while ago?"
Lo "Yeah."
c "The generator Reza tried to take from there can provide enough power to safely divert it, so we could use the excuse I was looking for some way to reactivate the portal or fix it."
Lo "Can you actually fix it?"
c "Sadly no, the portal is broken for good, but no one else has to know that."
Lo sad "..."
Lo think "Do you really want to check what's down there?"
c "I have to admit, I am pretty curious too."
Lo "Alright then, yeah, maybe we could."
c "We can go later then, when there’s less people outside that could see us."
Lo "Good call."
$ renpy.pause (0.5)

hide lorem with dissolve 
scene black with dissolveslow 
$ renpy.pause (1.5)
scene o2 with dissolveslow
show lorem normal with dissolve 
Lo "I didn’t think that pizza would be so filling, what should we do with the rest of it?"
c "We could just leave it in the fridge for later?"
Lo "Sure."
$ renpy.pause (0.3)
show lorem normal flip with dissolve 
hide lorem normal with easeoutright 
$ renpy.pause (2.0)
show lorem normal with easeinright
$ renpy.pause (0.5)
c "It's probably late enough to go to the underground building now."
Lo "Alright, let's go then..."
hide lorem with dissolve

scene np5 with dissolveslow
stop music fadeout 2.0
$ renpy.pause (1.0)
play sound "fx/door/door_close.ogg"
$ renpy.pause (1.5)
play music "mx/amb/night.ogg"
scene np2 with dissolveslow 
show lorem think with dissolve 
play sound "fx/steps/rough_gravel.ogg"
$ renpy.pause (1.5)
m "Lorem was staring at the sky while we were walking."
Lo think "Is that the comet?"
c "Yeah, it is."
$ renpy.pause (1.5)
Lo sad "Are you sure we’ll be fine?"
c "I'm confident we will be, with the power from the generator, and information from the PDA’s, the comet should be safely redirected."
Lo relieved "Good..."
$ renpy.pause (1.0)
hide lorem with dissolve 
$ renpy.pause (1.5)
scene np1n with dissolveslow
show lorem think with dissolve
$ renpy.pause (1.5)
m "I noticed as we got closer to the portal Lorem had gotten more and more apprehensive, so I tried to help them calm their nerves."
menu:
    "I’ll protect you no matter what happens.":
        c "Hey Lorem."
        Lo "Yeah?"
        c "You doing alright?"
        Lo "Uh, I'm just nervous about actually doing this..."
        c "You don’t have to worry about anything."
        c "I promise, I’ll look out for you, and protect you no matter what happens down there."
        Lo relieved "..."
        Lo normal "Thank you..."
        m "We continued walking together, Lorem seemed to be doing better thanks to my reassurance."

    "[[Make a joke.]":
        c "Lorem, why are you so nervous?"
        Lo think "Oh, you noticed...? It’s just... what if we get caught, we’re technically trespassing, right?"
        c "Really? That’s what you’re worried about?"
        c "Lorem, for someone to find us trespassing, they’d also have to be down there, right?"
        Lo "Right..."
        c "So, if they’re also trespassing, they’ll get arrested too, so we’ll be fine."
        Lo relieved "But whoever arrested them would arrest us too."
        c "But they’re trespassing too, so they’ll get arrested before they arrest us, check and mate."
        show lorem normal with dissolve 
        m "I heard Lorem quietly chuckling, not wanting me to hear them laughing at my stupid joke."
        Lo "You always know what to just say to lighten the mood, huh?"
        m "We continued walking, the tone slightly lifted from my dumb joke."

    "You can hold my hand if you’re scared.":
        $ rnloremromance += 1
        c "Lorem, you have no reason to be scared, I’ll be with you the entire time."
        Lo "I know..."
        $ renpy.pause (1.5)
        c "You can hold my hand if you want."
        Lo shy "..."
        $ renpy.pause (1.5)
        Lo normal blush "Okay..."
        m "We continued walking, me holding Lorem’s small scaly hand to help comfort them."


$ renpy.pause(1.0)
stop music fadeout 2.0
scene hallway with dissolveslow
$ renpy.pause (1.5)
show lorem think with dissolve
m "We made our way into the same corridor we confronted Reza in earlier, I took a look around and saw four rooms immediately around us."
play music "mx/mysteryambience.ogg"

# This is before the mini game starts, so the player can get the genreal layout

label ryann_lorem2_lo7_before_coridor:
scene hallway with dissolve

menu:
    "What room should we go to?"

    "Maintenance room.":
        m "We went into the maintenance room, and straight away a few things stood out to us."
        m "The primary generator that powered the facility and portal, an industrial looking pump and a large toolbox."
        label ryann_lorem2_lo7_before_maintenance:
        menu:
            "Look at generator.":
                m "There was a very obvious sign next to the generator, “DO NOT BRING LIQUIDS NEAR, RISK OF CATASTROPHIC FAILURE.”"
                show lorem think with dissolve
                c "You’d think it’d be obvious enough not to bring liquids near anything electrical."
                Lo relieved "Apparently not."
                hide lorem with dissolve

            "Look at pump.":
                $ ryannpumpbefore = True
                m "There was a label on the pump saying “Last scheduled maintenance done on 20...”"
                m "The rest of the label was too faded to read, but judging by the look of the pump it was definitely a while ago."
                c "(That’s not at all concerning...)"

            "Look at toolbox.":
                m "Unsurprisingly, the toolbox had lots of useful tools in it, a crowbar, a heavy-duty pipe wrench, a claw hammer, some flex tape and more miscellaneous things."
                m "There was also a note on the toolbox, which said the following:"
                m "“Someone keeps taking my tools without asking, so I'm keeping some in my quarters. If you want something you’ll actually have to ask,” - Otomo "

            "Go back to corridor.":
                jump ryann_lorem2_lo7_before_coridor

        jump ryann_lorem2_lo7_before_maintenance


    "Lab.":
        scene ryannundergroundlab with dissolveslow
        m "We walked into the lab, there was lots of high-tech machines I didn’t recognize or couldn’t understand at first glance."
        m "The more obvious things were a security locker, some cardboard boxes piled in the corner and an indent in the wall with wires coming out of it."
        label ryann_lorem2_lo7_before_lab:
        menu:
            "Look at security locker.":
                m "The security locker was very sturdy, it looked like the only way to get in was a keycard scanner."
                m "I peeked inside through a small gap, but I couldn’t see much, there were random electrical components, an industrial valve, some storage boxes varying in size..."

            "Look at boxes." if not ryannlookedboxes:
                $ ryannlookedboxes = True
                c "(Reza must have used one of these boxes for the generator, why are they here though?)"
                play sound "fx/rummage.wav"
                m "Me and Lorem searched all the boxes, but they were all empty or had useless junk."
                
            "Move boxes." if ryannlookedboxes and not ryannmovedboxes:
                $ ryannmovedboxes = True
                play sound "fx/box.wav"
                m "We moved the boxes aside, and behind it was an eye washing station, I tried to turn it on but it wasn’t working for some reason."
                m "The drain on the floor beneath it had a puddle of water on it, but it seemed like the drain wasn’t actually working, was it disabled as well, or just broken?"
                show lorem think with dissolve 
                Lo "That’s a huge safety hazard."
                c "Ipsum would be seething if he saw that."
                Lo normal "Oh definitely."
                hide lorem with dissolve

            "Look at eye washing station." if ryannlookedboxes and ryannmovedboxes:
                m " The eye washing station wasn't working, and neither of us being plumbers we didn’t try and fix it."

            "Look at wall indent.":
                m "I looked at the indent in the wall, wondering what it could be used for, but then I saw a sign next to it saying it was where the backup generator was supposed to be."
                show lorem think with dissolve 
                Lo "What is this used for?"
                c "It’s where the generator Reza took was."
                Lo "Ah, well that explains the wires."
                hide lorem with dissolve

            "Go back to corridor.":
                jump ryann_lorem2_lo7_before_coridor

        jump ryann_lorem2_lo7_before_lab

    
    "Meeting room.":
        scene whiteroom with dissolve 
        m "We stepped into the meeting room, and there wasn't really anything exciting, there was a set of cabinets, a row of lockers and as expected a long table with chairs."
        label ryann_lorem2_lo7_before_meeting:
        menu:
            "Look at table.":
                $ ryannlookedtable = True
                show lorem think with dissolve
                m "The table was pretty standard, there was four chairs under it and a stack of papers at the end of it."
                m "Lorem skimmed through the first page, with a confused look."
                Lo "I don’t understand half the stuff on that, so I don’t think there's really a reason for us to look into it..."
                hide lorem with dissolve

            "Look at cabinet.":
                $ ryannlookedcabinet = True
                m "The cabinet didn’t have much of anything, just some kind of injector, a few first aid supplies, and random documents."

            "Look at lockers.":
                m "There were four lockers in a row, three of them were unlocked and had nothing on, or in them."
                m "The fourth was labeled “I. Otomo” and had a sturdy looking fingerprint lock."
                show lorem think with dissolve 
                Lo "Why is only one locker being used, and by who?"
                c "..."
                c "I don’t know."
                hide lorem with dissolve 

            "Go back to corridor.":
                jump ryann_lorem2_lo7_before_coridor
        
        jump ryann_lorem2_lo7_before_meeting


    "Living quarters.":
        scene sec with dissolve 
        m "We walked into the living quarters, which was very well furnished, there was normal things to have in a bedroom, a bed, footlocker, shelf, desk, laptop, etc."
        m "If this room was your only point of reference you’d probably think it was part of a normal house."
        label ryann_lorem2_lo7_before_living:
        menu:
            "Look at shelf.":
                $ ryannlookedlist = True
                m "The shelf had lots of things on it, mostly folders, documents and other pieces of paper with numerous things on them."
                m "But most obviously a list, of presumably a maintenance worker."
                nvl clear
                window show
                n "{b}List of things to fix:{/b}"
                n "{b}High priority:{/b}"
                n " - The coupling on the backup generator is loose so it can easily be taken out, the others are saying it's not an issue, but I know it is, since when were they the maintenance crew?"
                n "{b}Medium priority:{/b}"
                n " - The pressure on the eye washing station in Lab A isn't optimal, I’ve disabled the drain and intake pipe with a pipe wrench for now until I fix it."
                n " - One of those idiots put a crack in the casing of the primary generator, I put some duct tape on it for now as the risk for flooding or coolant leaking is low enough."
                n "{b}Low priority:{/b}"
                n " - The Maintenance room pump is long overdue for scheduled maintenance, the risk of flooding is low enough and I have more urgent tasks before I can get to it."
                window hide
                nvl clear
                $ renpy.pause (0.5)
                jump ryann_lorem2_lo7_before_living

            "Look at footlocker.":
                m "The footlocker was fairly small and made of solid steel, it had a pretty strong looking padlock on it too."
                c "(No way we’re getting that open easily without the key.)"
                jump ryann_lorem2_lo7_before_living

            "Look at laptop.":
                m "I opened the laptop and was greeted by a standard start up screen, when suddenly..."
                show lorem think with dissolve
                Lo "Wait, that laptop works?"
                stop music fadeout 2.0
                play sound "fx/system3.wav"
                s "ERROR: UNREGISTED USER DETECTED, ACTIVATING LOCKDOWN."
                Lo scared "[player_name], what’s happening?!"
                c "I don’t know!"
                scene hallway with dissolve
                show lorem scared with dissolve 
                play sound "fx/run.ogg"
                m "We ran out into the corridor we entered from and saw a large blast door closing us out from the entrance."
                m "We ran and tried to escape before it closed completely, but we stopped when we heard some extremely concerning noises."
                play sound "fx/creak3.ogg"
                $ renpy.pause (3.5)
                play music "mx/fervor.ogg"
                m "The door started to jam, then suddenly fell with a loud crash, and soon after, the sound of running water."
                m "I regained my bearings from the shock and noticed water had started leaking in from the wall next to the door, the impact from the door slamming must have partially ruptured the water pockets."
                Lo "Where is that water coming from?!"
                c "It must be the water pockets surrounding the building!"
                Lo "What?!"
                c "There’s water pockets in the ground around the underground building, I thought with just the two of us it’d be safe enough."
                c "(Wait... If the water touches the primary generator, we’ll never get out of here!)"
                c "Lorem, we need to stop the water from touching the generator, it's our only chance at getting out of here."
                Lo "I-I..."
                $ renpy.pause (1.5)
                Lo sad "O-okay [player_name], w-what should we do?"
                c "If the water touches the generator, it could stop working, or worse, we need to stop that."
                Lo "How?!"
                m "I turned around and had only then noticed another blast door further down the hall, limiting us to the same four rooms around us,{w} I took a second to think of our options..."
                $ renpy.pause (1.5)
                if ryannpumpbefore == True:
                    c "The pump... We need to activate the pump in the maintenance room, let's go!"
                else:
                    c "I’d say the maintenance room is our best bet, let's go!"
                
                jump ryann_lorem2_lo7_minigame_start

            "Go back to corridor.":
                jump ryann_lorem2_lo7_before_coridor
                


#======================================================================================================================================================================================
# Making it clear where the minigame actually starts
#======================================================================================================================================================================================

label ryann_lorem2_lo7_minigame_start:

label ryann_lorem2_lo7_minigame_coridor:

label ryann_lorem2_lo7_minigame_start_init:

    show screen ryannextrainfo
    $ ryannextradisplay = 2

    $ ryannDisplayVar1name = "Actions remaining:"
    $ ryannlDisplayVar1 = ryannactionsremaining
    $ ryannDisplayVar1unit = ""

    $ ryannDisplayVar2name = "Current item:"
    $ ryannDisplayVar2 = ryanncurrentitem
    $ ryannDisplayVar2unit = ""

scene hallway with dissolve 
if ryannactionsremaining == 0:
    jump ryann_lorem2_lo7_minigame_rip

menu:
    m "What should we do?"

    "Go to maintenance room.":
        $ ryannactionsremaining -= 1
        jump ryann_lorem2_lo7_minigame_maintenance
        m "We entered the maintenance room."

    "Go to lab.":
        scene ryannundergroundlab with dissolve
        $ ryannactionsremaining -= 1
        jump ryann_lorem2_lo7_minigame_lab
        m "We entered the lab."
    
    "Go to meeting room.":
        scene whiteroom with dissolve
        $ ryannactionsremaining -= 1
        jump ryann_lorem2_lo7_minigame_meeting
        m "We entered the meeting room."

    "Go to living quarters.":
        scene sec with dissolve
        $ ryannactionsremaining -= 1
        jump ryann_lorem2_lo7_minigame_living
        m "We entered the living quarters."

    "Check on blast door.":
        $ ryannactionsremaining -= 1
        if ryanncurrentitem == "Crowbar":
            m "I tried to find a spot on the door to leverage the crowbar, but the blast door was too close to the ground to even try to get it underneath, even if I could, the door is far too heavy to move by hand."
        elif ryanncurrentitem == "Pipe wrench":
            play sound "fx/ryannmetalhit.mp3"
            m "I swung the pipe wrench at the blast door, but there wasn't even the slightest scratch or dent in it. I needed to try something else."
        elif ryanncurrentitem == "Claw hammer":
            play sound "fx/ryannmetalhit.mp3"
            m "I swung the claw hammer at the blast door, but there wasn't even the slightest scratch or dent in it. I needed to try something else."
        else:
            m "The blast door in the corridor was made of a thick sturdy metal, there was no way we were opening it by ourselves, we needed to find another way."

        jump ryann_lorem2_lo7_minigame_coridor


label ryann_lorem2_lo7_minigame_maintenance:
show screen ryannextrainfo
$ ryannlDisplayVar1 = ryannactionsremaining
$ ryannDisplayVar2 = ryanncurrentitem
if ryannactionsremaining == 0:
    jump ryann_lorem2_lo7_minigame_rip

menu:
    "Look at generator.":
        $ ryannactionsremaining -= 1
        if ryanntapeused == True:
            m "The tape I put on the generator casing wasn't enough to stop the water, but it will at least buy us some time."
        elif ryannlookedlist == True:
            m "Upon closer inspection of the generator, I noticed the duct tape on the casing of it, it looked extremely old and like it would fall off any second."
            if ryanncurrentitem == "Flex tape":
                $ ryanntapeused = True
                $ ryannactionsremaining += 10
                m "I used a generous amount of flex tape on the crack on the casing, it wouldn’t be enough to stop the water from spilling over the top, but it would at least buy us some time."
                c "(There's barely any of this tape left now, and definitely not enough of it left to be useful.)"
                $ ryanncurrentitem = "Nothing"

            else:
                c "(That tape wont stop any water anytime soon anymore, maybe we could do something about it?)"
            
        else:
            c "(If the water touches this, we're screwed... {w}I can't let Lorem know that, they seem scared enough already...)"
        
        jump ryann_lorem2_lo7_minigame_maintenance


    "Look at pump.":
        label ryann_lorem2_lo7_minigame_pump:
        show screen ryannextrainfo
        $ ryannlDisplayVar1 = ryannactionsremaining
        $ ryannDisplayVar2 = ryanncurrentitem
        if ryannactionsremaining == 0:
            jump ryann_lorem2_lo7_minigame_rip 

        if ryannpumpfixed == False and ryannpumpused == True:
            if ryanncurrentitem == "Screwdriver":
                if ryannvalveatpump == False:
                    $ ryannscrewdriveratpump = True
                    m "I tried to use the screwdriver to turn the slot for the valve, but it didn't give enough leverage. {w}Then I noticed some threads around the slot."
                    c "(Something definitely needs to be screwed in here, so I'll leave the screwdriver here for now.)"
                    $ ryanncurrentitem = "Nothing"

                else:
                    $ ryannpumpfixed = True
                    m "I put the valve back into its slot, and now with the screwdriver I tightened the valve into place."
                    m "After a slight shake to make sure it was fitted properly, I was confident enough that it would work."
                    $ ryanncurrentitem = "Nothing"

            elif ryanncurrentitem == "Valve":
                if ryannscrewdriveratpump == False:
                    $ ryannvalveatpump = True 
                    m "I slotted the valve into it's slot and tried to turn it, it did turn but it was extremely loose."
                    m "I then noticed another flathead shaped slot on the valve."
                    c "(This must need a screwdriver to be tightened, so I'll leave the valve here for now.)"
                    $ ryanncurrentitem = "Nothing"

                else:
                    $ ryannpumpfixed = True
                    m "As I put the valve into its slot, I noticed another flathead like slot on the valve, I took the screwdriver and tightened it."
                    m "After a slight shake to make sure it was fitted properly, I was confident enought that it would work."
                    $ ryanncurrentitem = "Nothing"


        m "There were multiple different things to interact with on the face of the pump."
        menu:
            "Turn the valve clockwise." if not ryannpumpused:
                $ ryannactionsremaining -= 1
                show lorem think with dissolve
                m "I tried to turn the valve, but no matter how much effort I put behind it, it wouldn't budge."
                Lo "[player_name], remember, righty tighty, lefty loosey."
                c "(Right, I'm trying to loosen the valve... {w}I think...)"
                hide lorem with dissolve 

            "Turn the valve clockwise." if ryannpumpfixed and not ryannpumpon:
                $ ryannactionsremaining -= 1
                show lorem think with dissolve
                m "I tried to turn the valve, but no matter how much effort I put behind it, it wouldn't budge."
                Lo "[player_name], remember, righty tighty, lefty loosey."
                c "(Right, I'm trying to loosen the valve... {w}I think...)"
                hide lorem with dissolve 

            "Turn the valve counterclockwise." if not ryannpumpused:
                $ ryannactionsremaining -= 1
                $ ryannpumpused = True
                m "I tried to turn the valve, it took a lot of force as it was stuck from the amount of rust on it, it eventually did give way though..."
                $ renpy.pause (0.5)
                play sound "fx/creak3.ogg"
                $ renpy.pause (3.5)
                m "Maybe a bit too much..."
                m "The valve had snapped off the pump completely, and part of it had bent, so the valve was just scrap metal now."
                show lorem scared with dissolve 
                Lo "What are we supposed to do now?!"
                c "Calm down Lorem, I'm sure we're able to fix this..."
                m "I looked closer at the pump where the valve had come off, and there seemed to be an indent in the pipe similar to the top of a flathead screw."
                c "Maybe that's where a new valve could slot in, or something else could be used for leverage to turn it?"
                hide lorem with dissolve 

            "Turn the valve counterclockwise." if ryannpumpfixed and not ryannpumpon:
                m "With the new valve slotted in I turned it, and it moved with surprising ease."
                $ ryannpumpon = True
                if ryannpumponoff == 2:
                    jump ryann_lorem2_lo7_minigame_end
                else:
                    m "Yet there was still something stopping the pump from working."
                    c "(Maybe I should have another look at this to make sure I haven't missed anything...)"

            "Press the on/off button." if ryannpumponoff < 2:
                $ ryannactionsremaining -= 1
                if ryannpumponoff == 0:
                    $ ryannpumponoff += 1
                    m "I pushed the on/off button, and a previously flashing light turned off."
                    
                elif ryannpumponoff == 1:
                    $ ryannpumponoff += 1
                    m "I pressed the button again, and the same light came back on, but a quiet hum started coming from the pump."
                    if ryannpumpon == True:
                        jump ryann_lorem2_lo7_minigame_end

                    else:
                        c "(That seems like a step in the right direction...)"

            "Change the output location.":
                m "There was a group of buttons that seemed to change the output of the pump, with what I assumed was some kind of coordinates or location number next to them."
                menu:
                    m "Should I change the output of the pump?"

                    "Change to location: 17.06":
                        pass

                    "Change to location: 93.60":
                        pass

                    "Change to location: 168.178":
                        pass

                    "Change to location: 31.01":
                        pass

                    "Look at something else.":
                        jump ryann_lorem2_lo7_minigame_pump

                $ ryannactionsremaining -= 1
                play sound "fx/button_press.ogg"
                $ renpy.pause (1.5)
                c "(I have no clue what that did, or if it actually helped or not...)"
                jump ryann_lorem2_lo7_minigame_pump

            "Move away from the pump.":
                jump ryann_lorem2_lo7_minigame_maintenance

        jump ryann_lorem2_lo7_minigame_pump



    "Check toolbox.":
        m "I looked through the toolbox and found some things that could be useful, there was also a note on the toolbox."
        menu:
            m "Should I take anything?"

            "Crowbar" if not ryanncrowbarused and not ryanncurrentitem == "Crowbar":
                $ ryannactionsremaining -= 1
                $ ryanncurrentitem = "Crowbar"
                play sound "fx/ryannpickuptool.mp3"
                m "I picked up the crowbar."

            "Pipe wrench" if not ryannwrenchused and not ryanncurrentitem == "Pipe wrench":
                $ ryannactionsremaining -= 1
                $ ryanncurrentitem = "Pipe wrench"
                play sound "fx/ryannpickuptool.mp3"
                m "I picked up the pipe wrench."

            "Claw hammer" if not ryanncurrentitem == "Claw hammer":
                # This is a red herring and doesn't actually have a use
                $ ryannactionsremaining -= 1
                $ ryanncurrentitem = "Claw hammer" 
                m "I picked up the claw hammer."

            "Flex tape" if not ryanntapeused and not ryanncurrentitem == "Flex tape":
                $ ryannactionsremaining -= 1
                $ ryanncurrentitem = "Flex tape"
                m "I picked up the tape."

            "Check note":
                $ ryannactionsremaining -= 1
                m "The note said the following:"
                m "“Someone keeps taking my tools without asking, so I'm keeping some my quarters. If you want something you’ll actually have to ask,” - Otomo"

            "Take nothing":
                pass
                
        jump ryann_lorem2_lo7_minigame_maintenance

    "Go back to corridor.":
        jump ryann_lorem2_lo7_minigame_coridor
         


label ryann_lorem2_lo7_minigame_lab:

$ ryannlDisplayVar1 = ryannactionsremaining
$ ryannDisplayVar2 = ryanncurrentitem
show screen ryannextrainfo
if ryannactionsremaining == 0:
    jump ryann_lorem2_lo7_minigame_rip

menu:
    "Check on security locker.":
        $ ryannactionsremaining -= 1
        if ryanncurrentitem == "Valve" or ryannvalveatpump == True:
            m "I looked through the locker again but couldn't find anything else useful."

        elif ryannhaskeycard == True:
            if ryannpumpused == True:
                play sound "fx/ryannpickuptool.mp3"
                m "Using the keycard I had gotten earlier I opened the locker, I spotted a spare valve and took it immediately, not caring much for anything else inside."

            else:
                play sound "fx/ryannpickuptool.mp3"
                m "Using the keycard I had gotten earlier I opened the locker, the only thing that seemed like it could be useful was a spare valve, the other random components and storage boxes didn't."

            $ ryanncurrentitem = "Valve"

        elif ryanncurrentitem == "Crowbar":
            m "Despite my best efforts using the crowbar, the locker was too sturdy to be forced open, it seemed like trying to find the keycard was our only option."
            m "I could at least peek inside the locker through a small gap, but I couldn’t see much, there were random electrical components, a valve, and some storage boxes varying in size."

        else:
            m "The security locker was very sturdy, it looked the only way to get in was a keycard scanner."
            m "I peeked inside through a small gap, but I couldn’t see much, there were random electrical components, a valve, and some storage boxes varying in size."

        jump ryann_lorem2_lo7_minigame_lab

 
    "Look at boxes." if not ryannlookedboxes:
        $ ryannlookedboxes = True
        $ ryannactionsremaining -= 1
        play sound "fx/rummage.wav"
        m "Me and Lorem searched through the boxes, but they were either empty or full of useless junk."
        jump ryann_lorem2_lo7_minigame_lab
                
    "Move boxes." if ryannlookedboxes and not ryannmovedboxes:
        $ ryannmovedboxes = True
        $ ryannactionsremaining -= 1
        play sound "fx/box.wav"
        m "We moved the boxes out of the way and spotted an eye washing station behind them."
        jump ryann_lorem2_lo7_minigame_lab

    "Look at eye washing station." if ryannlookedboxes and ryannmovedboxes:
        $ ryannactionsremaining -= 1
        if ryanncurrentitem == "Pipe wrench":
            m "I looked at the drain beneath the eye washing station yet it wasn't draining any water from the room."
            m "After a bit of seaching, I saw a pipe with a nut on it leading to the drain, I firmly tightend the pipe wrench around it and loosened it."
            m "Some air bubbles came up from the drain, then a small stream of water started flowing down the pipe, not enough to stop the water, but enough to buy us some time."
            m "I tried to retrieve the pipe wrench from the pipe, but it was stuck, probably from being tightened too much, we left it as we didnt have the time to spare getting it unstuck."
            $ ryanncurrentitem = "Nothing"
            $ ryannwrenchused = True 
            $ ryannactionsremaining += 10

        elif ryannwrenchused == True:
            m "The small drain underneath the eye washing station was draining a small amount of water from the room, not much but it was better than nothing."

        else:
            m "I tried to see if the eye washing station was working, but it wasn't. It's not like we needed more water now anyway..."
            m "But when I looked lower I saw the drain beneath it, yet it wasnt draining any of the water flooding the room."
            c "(If we can get that drain working, it won't be enough to stop the water completely, but it might be better than nothing?)"

        jump ryann_lorem2_lo7_minigame_lab


    "Look at wall indent":
        $ ryannactionsremaining -= 1
        m "There were wires coming out of the indent, and the sign next to it said the space was for the backup generator. Thankfully it wasn't here now."
        m "But there was nothing helpful there for us right now."
        jump ryann_lorem2_lo7_minigame_lab

    "Go back to coridor.":
        jump ryann_lorem2_lo7_minigame_coridor




label ryann_lorem2_lo7_minigame_meeting:

$ ryannlDisplayVar1 = ryannactionsremaining
$ ryannDisplayVar2 = ryanncurrentitem
show screen ryannextrainfo
if ryannactionsremaining == 0:
    jump ryann_lorem2_lo7_minigame_rip

menu:
    "Check table.":
        if ryannlookedtable == False: 
            $ ryannlookedtable = True
            $ ryannactionsremaining -= 1
            m "The table was surounded by four chairs, and the only thing on it was a stack of papers."
            m "I skimmed through the first page but saw nothing useful."

        else:
            m "There wasn't anything else on the table to check apart from the papers."

        jump ryann_lorem2_lo7_minigame_meeting

    "Search through papers." if ryannlookedtable:
        if ryannhaskeycard == False:
            $ ryannhaskeycard = True 
            m "I searched the papers more thoroughly isntead of skimming through them, but there wasn't really much that could help us."
            m "Just as I was about to put the papers down, a keycard fell out between them and fell to the floor."
            m "I picked it up, hoping to find a use for it."

        else:
            m "I searched the papers again, yet as expected there wasn't anything else useful."

        $ ryannactionsremaining -= 1
        jump ryann_lorem2_lo7_minigame_meeting


    "Search cabinet.":
        if ryannlookedcabinet == True:
            m "I seached the cabinet again, yet there still wasn't anyhting that could help us."

        else:
            $ ryannlookedcabinet = True
            m "The cabinet didn’t have anything useful, just some kind of injector, a few first aid supplies, and random documents"

        $ ryannactionsremaining -= 1
        jump ryann_lorem2_lo7_minigame_meeting


    "Search lockers.":
        if ryannhaskey == False:
            m "The only non-locked locker was labeled “I. Otomo” and it had a sturdy looking fingerprint lock on it."
            if ryanncurrentitem == "Crowbar":
                m "I jammed the crowbar into the top corner of the locker and began to force it open."
                play sound "fx/ryannusecrowbar.mp3"
                m "It was working for the most part and the locker door was begining to bend, {w}then suddenly the crowbar slipped."
                play sound "fx/metalbox.ogg"
                $ renpy.pause (1.0)
                m "The locker door was bent, but so was the crowbar."
                show lorem think with dissolve
                c "Damn, that crowbar must have been older than it looked, it's useless like this now."
                Lo "At least it held out long enough to open the locker."
                c "Fair point."
                $ ryanncurrentitem = "Nothing"
                $ ryanncrowbarused = True
                $ ryannhaskey = True
                m "I looked through the now opened gap into the locker, there was a horizontal pole with what looked like a uniform and some kind of cloak on hung up on it."
                m "Ironically, there was also a key on a small shelf at the top of the locker, I took it and put it in one of my pockets, grateful I might not need to use brute force to open another lock."
                hide lorem with dissolve
                $ ryannactionsremaining -= 1
                jump ryann_lorem2_lo7_minigame_meeting
                

            else:
                if ryanncurrentitem == "Pipe wrench":
                    if ryannwrenchlocker == False:
                        $ ryannwrenchlocker = True 
                        play sound "fx/ryannmetalhit.mp3"
                        m "I swung the pipe wrench at the lock, but it didn't break, it just indented the locker slightly."
                        c "(I shouldn't try that again, if I cave the locker door in, I doubt we could get it open at all.)"
                        $ ryannactionsremaining -= 1
                        jump ryann_lorem2_lo7_minigame_meeting

                    else:
                        pass

                elif ryanncurrentitem == "Claw hammer":
                    m "I swung the hammer at the lock, yet there wasn't any damage to it."
                    c "(That didn't work, I need to try something else...)"
                    $ ryannactionsremaining -= 1
                    jump ryann_lorem2_lo7_minigame_meeting

                elif ryanncurrentitem == "Screwdriver":
                    m "I searched around the locker trying to find the hinges, but when I eventually did I saw they were on the inside of the door, so there was no way to unscrew them."
                    $ ryannactionsremaining -= 1
                    jump ryann_lorem2_lo7_minigame_meeting

                else:
                    pass
    
        else:
            m "There wasn't anything else in the locker I could reach that would actually be useful to us right now."
            jump ryann_lorem2_lo7_minigame_meeting

        m "Even though the lock was sturdy, the actual locker door seemed to be made of a thinner sheet of metal."
        c "(Maybe I can force this open with something?)"
        $ ryannactionsremaining -= 1
        jump ryann_lorem2_lo7_minigame_meeting

    "Go back to coridor.":
        jump ryann_lorem2_lo7_minigame_coridor


label ryann_lorem2_lo7_minigame_living:

$ ryannlDisplayVar1 = ryannactionsremaining
$ ryannDisplayVar2 = ryanncurrentitem
show screen ryannextrainfo
if ryannactionsremaining == 0:
    jump ryann_lorem2_lo7_minigame_rip

menu:
    "Search shelf.":
        m "There's multiple things to check on the shelf."
        menu:
            "Look at blueprint.":
                $ ryannactionsremaining -= 1
                m "There was a blueprint of the underground building, at first I was expecting to learn something useful from it, but I was surely disappointed."
                m "It either showed us stuff we already knew, like the four rooms connected to the coridor, or something that we couldn't access, like an exit ladder behind the second blast door."

            "Check folders.":
                $ ryannactionsremaining -= 1
                m "There was an entire shelf decicated just to folders, just from skimming the labels on them, I doubted they could help us."

            "Look at maintenance list.":
                $ ryannlookedlist = True 
                $ ryannactionsremaining -= 1
                m "There was a list on the shelf of things that needed to be fixed, presumably belonging to a maintenance worker."
                nvl clear
                window show
                n "{b}List of things to fix:{/b}"
                n "{b}High priority:{/b}"
                n " - The coupling on the backup generator is loose so it can easily be taken out, the others are saying it's not an issue, but I know it is, since when were they the maintenance crew?"
                n "{b}Medium priority:{/b}"
                n " - The pressure on the eye washing station in Lab A isn't optimal, I’ve disabled the drain and intake pipe with a pipe wrench for now until I fix it."
                n " - One of those idiots put a crack in the casing of the primary generator, I put some duct tape on it for now as the risk for flooding, or coolant leaking is low enough."
                n "{b}Low priority:{/b}"
                n " - The Maintenance room pump is long overdue for scheduled maintenance, the risk of flooding is low enough and I have more urgent tasks before I can get to it."
                window hide
                nvl clear
                $ renpy.pause (0.5)

            "Move away from the shelf.":
                jump ryann_lorem2_lo7_minigame_living

        jump ryann_lorem2_lo7_minigame_living


    "Check footlocker.":
        m "The footlocker was fairly small, made of solid steel and had a tough looking padlock."
        if ryannhaskey == False:
            if ryanncurrentitem == "Pipe wrench":
                $ ryannactionsremaining -= 1
                play sound "fx/ryannmetalhit.mp3"
                m "I swung the pipe wrench at the footlocker, but there was no noticable damage to it at all."
                c "(That's made of solid steel, there's no way I can just bash it open. Maybe finding the key would be easier?)"
                jump ryann_lorem2_lo7_minigame_living

            elif ryanncurrentitem == "Claw hammer":
                $ ryannactionsremaining -= 1
                play sound "fx/ryannmetalhit.mp3"
                m "I swung the claw hammer at the footlocker, but there was no noticable damage to it at all."
                c "(That's made of solid steel, there's no way I can just bash it open. Maybe finding the key would be easier?)"
                jump ryann_lorem2_lo7_minigame_living

            elif ryanncurrentitem == "Crowbar":
                $ ryannactionsremaining -= 1
                m "I tried to use the crowbar to force open the footlocker, but it was too small to get some proper leverage on it, even if I could, it's made of solid steel."
                c "(This isn't working, maybe I could try and find the key?)"
                jump ryann_lorem2_lo7_minigame_living

            else:
                c "(I doubt the key would be too far from here, maybe we should look around for it?)"
                jump ryann_lorem2_lo7_minigame_living


        else:
            if ryannscrewdriveratpump == True or ryanncurrentitem == "Screwdriver":
                m "I searched the footlocker again, but nothing else seemed useful."
                $ ryannactionsremaining -= 1
                jump ryann_lorem2_lo7_minigame_living

            else:
                if rnunlockedfootlocker == False:
                    $ rnunlockedfootlocker = True
                    m "Using the key I got earlier I unlocked the footlocker, inside it were some personal items and some tools."
                    m "Out of all the tools only the screwdriver seemed useful."
                    $ ryanncurrentitem = "Screwdriver"
                    $ ryannactionsremaining -= 1

                else:
                    m "I checked the footlocker again, and still, the screwdriver was the only useful thing in it."
                    $ ryanncurrentitem = "Screwdriver"
                    $ ryannactionsremaining -= 1


            jump ryann_lorem2_lo7_minigame_living


    "Check laptop.":
        m "I opened the laptop and was greeted with the following options:"
        label ryann_lorem2_lo7_minigame_laptop:

        $ ryannlDisplayVar1 = ryannactionsremaining
        $ ryannDisplayVar2 = ryanncurrentitem
        show screen ryannextrainfo    
        if ryannactionsremaining == 0:
            jump ryann_lorem2_lo7_minigame_rip

        menu:
            "Deactive lockdown.":
                play sound "fx/keyboard.ogg"
                $ renpy.pause (3.5)
                play sound "fx/system3.wav"
                s "ERROR: Can not deactive lockdown, water detected in: Compartment A"
                s "Contact maintenance for immediate assistance."
                jump ryann_lorem2_lo7_minigame_laptop

            "Enter search term:":
                play sound "fx/system3.wav"
                s "Lockdown search engine engaged, search terms limited, lowercase input only. Type \"help\" for help."
                $ ryannsearchterm = renpy.input(_("Enter search term:"))
                play sound2 "fx/keyboard.ogg"
                $ renpy.pause (3.5)

                if ryannsearchterm == "flower" or ryannsearchterm == "flowers" or ryannsearchterm == "flower crown" or ryannsearchterm == "daisy" or ryannsearchterm == "daisies" or ryannsearchterm == "daisy crown":
                    play sound "fx/system.wav"
                    Rnn "Hope you don't have hay fever..."
                    $ ryannsecretscene = True
                    jump ryann_lorem2_lo7_minigame_laptop

                elif ryannsearchterm == "bacon" or ryannsearchterm == "meatsnacks" or ryannsearchterm == "meat snacks" or ryannsearchterm == "Wedding_day" or ryannsearchterm == "donut" or ryannsearchterm == "doughnut" or ryannsearchterm == "donuts" or ryannsearchterm == "doughnuts":
                    Rnn "Wrong mod buddy." 
                    jump ryann_lorem2_lo7_minigame_laptop

                elif ryannsearchterm == "help":
                    play sound "fx/system3.wav"
                    s "Lockdown mode search terms include: manual, sos, emergency, copy, paste, undo, delete, cut, power, generator, status."

                elif ryannsearchterm == "manual":
                    label ryann_lorem2_lo7_minigame_manual:

                    $ ryannlDisplayVar1 = ryannactionsremaining
                    $ ryannDisplayVar2 = ryanncurrentitem
                    show screen ryannextrainfo
                    if ryannactionsremaining == 0:
                        jump ryann_lorem2_lo7_minigame_rip

                    play sound "fx/system3.wav"
                    s "Welcome to user eManual, please select a category:"
                    menu:
                        "Introduction":
                            s "User eManual is to provide information to users and crew when requested."
                            s "Information available includes, lockdown procedure, emergency situations and more. "
                            s "For more information or accessibility contact a maintenance crew member or administrator."
                            $ ryannactionsremaining -=1
                            jump ryann_lorem2_lo7_minigame_manual

                        "Lockdown":
                            s "In an emergency situation a lockdown order can be given manually, or in certain circumstances trigger automatically."
                            s "Automatic triggers include: flood, fire, severe structural damage, unregistered users and more."
                            s "Lockdown triggers can be added, removed or modified by qualified maintenance crew and administrators."
                            s "Lockdowns can be disabled after an active emergency has been resolved."
                            $ ryannactionsremaining -=1
                            jump ryann_lorem2_lo7_minigame_manual

                        "Emergencies":
                            s "In the case of an emergency, an automatic lockdown will engage, see \"Lockdown\" for more information."
                            s "Necessary equipment, machinery and tools can be found per compartment to resolve an emergency."
                            s "If not, contact a maintenance crew member."
                            $ ryannactionsremaining -=1
                            jump ryann_lorem2_lo7_minigame_manual

                        "Exit":
                            jump ryann_lorem2_lo7_minigame_laptop

                elif ryannsearchterm == "copy" or ryannsearchterm == "delete" or ryannsearchterm == "cut":
                    play sound "fx/system3.wav"
                    s "ERROR: Nothing selected."

                elif ryannsearchterm == "undo":
                    play sound "fx/system3.wav"
                    s "ERROR: Nothing to undo."

                elif ryannsearchterm == "paste":
                    play sound "fx/system3.wav"
                    s "ERROR: Nothing copied to clipboard."

                elif ryannsearchterm == "sos" or ryannsearchterm == "emergency":
                    play sound "fx/system3.wav"
                    s "In emergency situations, consult the manual or contact a maintenance crew worker."
                    s "In the event a emergency is detected, an automatic lockdown will engage, consult manual for more information."

                elif ryannsearchterm == "power" or ryannsearchterm == "generator":
                    play sound "fx/system3.wav"
                    s "Primary generator status: Optimal"
                    s "Backup generator status: ERROR: Generator not found, contact maintenace crew member immediately."

                elif ryannsearchterm == "status":
                    play sound "fx/system3.wav"
                    s "Prossesing..."
                    s "Water detected in [[Compartment A], contact maintenance crew member immediately."

                else:
                    play sound "fx/system3.wav"
                    s "ERROR: Lockdown search mode engaged, search terms limited, type \"help\" for help."

                jump ryann_lorem2_lo7_minigame_laptop


            "Log off.":
                jump ryann_lorem2_lo7_minigame_living

    "Go back to coridor.":
        jump ryann_lorem2_lo7_minigame_coridor
        
     
label ryann_lorem2_lo7_minigame_rip:


scene black with dissolve 
stop sound
stop music fadeout 1.0
hide screen ryannextrainfo
$ renpy.pause (1.5)

m "I was suddenly overwhelmed with a sense of dread..."
$ renpy.pause (1.5)
play sound "fx/explosion.ogg"
$ renpy.pause (7.5)
Rnn "That didn't go so well, huh?"
Rnn "Don't worry, there's no shame in trying again, I won't tell anyone."
Rnn "At least you're not going in completely blind this time, good luck!"
$ renpy.pause (2.0)

$   ryannactionsremaining = 25
$   ryannsearchterm = ""
$   ryanncurrentitem = "Nothing"
$   ryanncrowbarused = False
$   ryannwrenchused = False
$   ryanntapeused = False 
$   ryannhaskey = False 
$   ryannhaskeycard = False 
$   ryannwrenchlocker = False
$   ryannpumpused = False
$   ryannpumpfixed = False
$   ryannpumponoff = 0
$   ryannpumpon = False
$   ryannvalveatpump = False
$   ryannscrewdriveratpump = False
$   ryannlookedtable = False
$   ryannlookedboxes = False
$   ryannmovedboxes = False
$   ryannlookedcabinet = False 
$   ryannlookedlist = False 

play music "mx/fervor.ogg"
jump ryann_lorem2_lo7_minigame_start


#======================================================================================================================================================================================
# Making it clear where the minigame ends
#======================================================================================================================================================================================


label ryann_lorem2_lo7_minigame_end:

hide screen ryannextrainfo

stop music fadeout 2.0
m "With the pump restarted, and the new valve being turned, the pump came to life."
play sound "fx/system3.wav"
s "Primary pump active, draining system initiated."
m "The water level in the room started to slowly, but surely decrease."
show lorem think with dissolve 
Lo think "D-Did we do it...?"
c "I think we did!"
Lo relieved "Thank goodness... But how do we get out now?"
c "I think that laptop might be able to do something."
Lo "Lets go then... I just really want to get out of here..."
$ renpy.pause (1.0)
scene sec with dissolveslow
$ renpy.pause (1.5)
m "We made our way back to the laptop and opened it."
play sound "fx/keyboard.ogg"
$ renpy.pause (3.5)
play sound "fx/system3.wav"
s "Welcome user, \"[player_name]\"."
s "Deactivating lockdown..."
s "New familiar user “Lorem” defined..."
$ renpy.pause (1.0)
m "We heard the sound of the door opening and left immediately, not wanting to be stuck down there in case anything else happened."
scene hallway with dissolveslow
$ renpy.pause (1.5)
if not ryanncurrentitem == "Nothing":
    if ryanncurrentitem == "Pipe wrench":
        m "As we were leaving, I tossed the pipe wrench on the ground, not wanting any reminder of this place, or anything that happened here."

    elif ryanncurrentitem == "Flex tape":
        m "As we were leaving, I tossed the tape on the ground, not wanting any reminder of this place, or anything that happened here."
        
    elif ryanncurrentitem == "Claw hammer":
        m "As we were leaving, I tossed the claw hammer on the ground, not wanting any reminder of this place, or anything that happened here."

else:
    pass

scene np2y with dissolveslow
play sound "fx/steps/rough_gravel.wav"
$ renpy.pause (1.5)
m "The walk back to my apartment was dead silent, both of us were still too shaken to even try to talk about anything."
$ renpy.pause (1.0)
scene np5 with dissolveslow
$ renpy.pause (2.0)
scene o3 with dissolveslow
show lorem sad with dissolve
$ renpy.pause (1.5)
play sound "fx/undress.ogg"
m "We entered my apartment and sat on the couch, still in complete silence."
m "I managed to at least partially compose myself, unlike Lorem who still seemed quite unsettled."
menu:
    "[[Put your arm around them.]":
        $ rnloremromance += 1
        play sound "fx/undress.ogg"
        m "I leaned over to the little dragon and put my arm around them, to help console them over what had just happened."
        m "They moved closer to me, resting at my side."
        m "We sat together in silence, me listening to Lorem's breathing slow as they gradually calmed down."
        m "After a while they moved away and broke the silence."

    "[[Get the leftover pizza.] ":
        m "I noticed I was fairly hungry and remembered about the pizza we had earlier, I thought Lorem might enjoy it too, and help him settle down."
        m "I got the box out of the fridge, and brought it out to the couch we were sitting on."
        m "Neither of us said anything, we just ate the pizza, which surprisingly, was still amazing despite being chilled from the fridge."
        Lo relieved "This is exactly what I needed, it's so much better after what just happened."
        $ renpy.pause (0.5)
        show lorem sad with dissolve 
        m "We sat in silence after eating, and Lorem eventually broke it."

    "[[Do nothing.]":
        m "We just sat there together, enjoying each other's company, trying to prosses everything and relax from what just happened."
        $ renpy.pause (2.5)
        m "After a while, Lorem broke the silence."

$ renpy.pause (2.0)
play music "mx/sleepingcity.ogg"
Lo "[player_name], there’s something I wanted to talk to you about..."
c "What is it?"
if rnloremromance > 7:
    Lo think "It's just... things you’ve been doing or saying lately..."
    Lo "It made me realize something."
    $ renpy.pause (1.5)
    Lo "I..."
    $ renpy.pause (2.0)
    c "Hey, Lorem, you know you can tell me anything right? I won't think any differently of you, promise."
    Lo relieved "But that’s the problem..."
    show lorem sad with dissolve 
    $ renpy.pause (2.0)
    Lo blush "I have feelings for you, I-I like you as more than a friend..."
    $ renpy.pause (1.5)
    show lorem normal blush with dissolve 
    m "Lorem and I looked deeply into each other's eyes, theirs having a hint of fear of being rejected, yet also hope and relief of finally telling me their true feelings."
    c "Lorem..."
    $ renpy.pause (1.5)
    c "I feel the same, I like you as more than a friend too."
    Lo "R-Really...?"
    m "I gently put my hand under Lorem’s chin, guiding their lips to mine, pulling them into a passionate kiss."
    show lorem shy with dissolve 
    m "Lorem was surprised by my action, but soon gave in, returning the kiss and subtly slipping in a small amount of tongue, which I took as an invitation to return the favor."
    show lorem sleep blush with dissolve 
    m "I moved my hand from their chin and started caressing their neck, while they held my shoulders pulling me closer."
    show lorem normal blush with dissolve 
    m "We slowly parted; eyes still locked."
    c "Really."
    Lo relieved "That’s such a relief, I was worried you wouldn’t feel the same because of me being a hermaphrodite."
    c "Remember what I said when you told me? I don’t mind at all."
    show lorem normal blush with dissolve 


elif rnloremromance > 3:
    Lo think "It’s just... I wanted to make sure of something..."
    Lo "I'm just unsure of what you think of me, it's hard to tell if you’re implying something or if it's just a human thing, so I’ll just be blunt and ask..."
    $ renpy.pause (2.0)
    Lo blush "Do... Do you see me as more than just a friend...?"
    $ renpy.pause (2.0)
    c "Yes, I do, I see you as more than a friend."
    Lo shy "W-Wait, really...?"
    Lo "B-But what about me being a hermaphrodite?"
    c "Remember what I said when you told me? I don’t mind at all."
    show lorem normal blush with dissolve 
    m "We stared into each other's eyes for what felt like several long minutes, I tilted my head to the side and started moving closer."
    show lorem shy with dissolve 
    m "Lorem seemed flustered, yet still copied my actions, the two of us getting closer to each other by the second."
    show lorem sleep blush with dissolve 
    m "We closed our eyes, and our lips made contact, I put my hand around the back of Lorem’s neck, as they grabbed my shoulder, pulling me closer."
    show lorem normal blush with dissolve
    m "We stayed like that for several long seconds, until we both slowly pulled away, still staring into each other's eyes."
    c "Do you believe me now?"
    show lorem blush with dissolve 
    Lo "Yes..."


else:
    Lo normal "I know I’ve said it before, but I wanted you to know how much our friendship means to me."
    Lo sad "I don’t really have many other friends other than you and Ipsum, and no one else who knows I’m a hermaphrodite."
    Lo normal "But I’m glad that after what just happened, I know that you’ll have my back no matter what."
    c "Of course, Lorem, that’s what friends do for each other, I'm glad to know you’ll be by my side no matter what too."
    c "One question though, does this mean I outrank Ipsum now?"
    Lo think "Hmm..."
    Lo normal "To stop anyone from being jealous, I’ll say you’re on par."
    c "I guess I’ll take it."


$ renpy.pause (2.0)
c "Anyway, it's getting late and I’d feel bad making you fly home in the dark, especially after what just happened, so do you want to stay over for the night?"
if rnloremromance > 3:
    Lo normal blush "I’d love to."
else:
    Lo normal "Sure, thanks for the offer."

m "I brought Lorem to my bedroom and started preparing the bed for them, after I did, I looked at them and gestured towards it."
Lo think "Wait, you’re letting me sleep in your bed?"
c "Of course, there's no way I'm letting you sleep on the couch, I want you to be as comfortable as possible."
Lo normal "Alright, thank you..."
m "Lorem got into the bed and under the covers slowly, clearly tired from the events of the day."
if rnloremromance > 3:
    m "I started to turn around and head to the living room to go and sleep on the couch, but I was stopped by a small scaly hand tugging my arm."
    Lo relieved "[player_name], wait."
    c "Yes?"
    Lo normal blush "Well, after what happened in the underground building, I don't really want to be alone right now, and I’m pretty small, so, um..."
    Lo blush "D-Do you want to... {w}share the bed...?"
    m "I turned back around and faced Lorem."
    $ renpy.pause (1.5)
    c "Sure Lorem."
    $ renpy.pause (1.0)
    play sound "fx/undress.ogg"
    show lorem shy with dissolve
    m "I started to get undressed, and as expected, Lorem got their usual adorable flustered look."
    m "I got into the bed, and made short work of reducing the gap between us, after some slight hesitation Lorem did too, nuzzling themselves into me."
    show lorem blush with dissolve
    $ renpy.pause (1.0)
    Lo "I didn’t know humans were so... warm, and soft, and cuddly..."
    show lorem sleep blush with dissolve 
    m "I wrapped my arms around them, careful not to injure their wings, and pulled them into a closer embrace."
    m "Lorem wrapped their arms around me too, eager to steal as much of my body heat as possible."
    m "I kissed the top of their muzzle, and rested my chin on their forehead, helping them drift into a peaceful slumber."
    c "Goodnight Lorem."
    Lo "Goodnight [player_name]."
    $ renpy.pause (2.0)
    show lorem sleep with dissolveslow
    m "I listened to Lorem’s breathing gradually slow down, and their grip on me relaxed, as they fell asleep."
    m "I held Lorem in my embrace, and closed my eyes too."
    m "For the first time in a while of being in the dragon's world, I finally felt at peace, and was filled with a wave of contentedness."
    m "I slowly drifted off to sleep as well."

else:
    m "I grabbed a spare blanket and turned to Lorem before leaving the room." 
    c "Goodnight Lorem."
    Lo "Goodnight [player_name]."
    hide lorem with dissolve
    $ renpy.pause (0.5)
    m "I made my way to the living room and started to prepare my own bed, setting the blanket down on the couch."
    play sound "fx/undress.ogg"
    m "I settled down, and after struggling for a while I eventually found a comfortable sleeping position."
    m "I looked out the window, and was alone with my thoughts."
    c "(I really am staying in the dragon's world permanently...)"
    c "(The thought alone would upset me... {w}But I'm glad I don't have to say goodbye to Lorem...)"
    m "For the first time in a while of being in the dragon's world, I finally felt at peace, and was filled with a wave of contentedness."
    m "I closed my eyes and slowly drifted off to sleep."

$ renpy.pause (1.5)
scene black with dissolveslow
stop music fadeout 2.0
$ renpy.pause (6.0)
scene o4 with dissolveslow
play music "mx/morningrise.ogg"
$ renpy.pause (1.0)
m "I woke up, still groggy from the events that occurred yesterday."
if rnloremromance > 3:
    show lorem sleep with dissolveslow
    $ renpy.pause (0.5)
    m "The adorable small dragon clinging to me was a pretty good reminder though."
    m "Me and Lorem had moved during the night, so they were now lying on top of me, their small tail wrapped around my leg, and wings unfolded, covering me like a scaly blanket."
    m "I hadn’t the heart to wake them."
    $ renpy.pause (3.5)
    m "After a while of being Lorem’s personal pillow, I made sure my movements getting up were very slow and careful as not to wake Lorem."
    Lo "Mmmhhh...?"
    m "Lorem’s still asleep mind tried to protest me getting up, but settled with lying on the part of the bed still warmed by my body heat."
    play sound "fx/undress.ogg"
    m "I got dressed and made my way to the kitchen to prepare a breakfast for the two of us for when Lorem woke up."
    hide lorem with dissolveslow

else:
    m "My stiff back and neck pain didn’t hesitate to remind me though."
    c "(Damn, this couch is unbearable to sleep on, I'm glad I did and not Lorem.)"
    m "After a decent amount of stretching, I went to check on Lorem. I made my way to the bedroom and slowly peeked through the door."
    show lorem sleep with dissolveslow 
    $ renpy.pause (0.5)
    m "Lorem was still asleep, comfortably sprawled across my bed, with a big dopey grin on their face. "
    hide lorem with dissolveslow
    m "I left just as quietly as I entered, and made my way to the kitchen to prepare a breakfast for the two of us for when Lorem woke up."

scene ryannkitchen with dissolveslow
m "After making my way to the kitchen and scouring the fridge and cabinets, I came up with the makings of a decent breakfast."
m "As I began to prepare it, I heard a set of small footsteps behind me."
show lorem normal flip at left with easeinleft
Lo "Hey [player_name]..."
c "Morning Lorem, you can wait in the living room, I’ll be out in a few minutes."
Lo "Mhmm."
show lorem normal with dissolve
$ renpy.pause (0.3)
hide lorem with easeoutleft
$ renpy.pause (0.5)
c "(I didn’t even think they could be more adorable, but being half asleep does it apparently.)"
m "After finishing up I brought our breakfast out to the living room."
scene o4 with dissolveslow
show lorem normal with dissolve 
play sound "fx/undress.ogg"
if rnloremromance > 3:
    m "I handed Lorem their plate and sat down next to them, but they seemed unusually quiet."
    c "Hey, Lorem, are you alright?"
    Lo think " It's just... About last night..."
    Lo "I... {w}You..."
    $ renpy.pause (1.5)
    Lo relieved "I don't know what I want to say..."
    $ renpy.pause (1.5)
    m "I leaned over to Lorem and gave them a quick peck on the cheek."
    show lorem shy with dissolve
    c "Maybe we don't have to say anything, and we can just enjoy this together, we don't need to overthink it."
    show lorem normal blush with dissolve
    $ renpy.pause (1.5)
    Lo "Yeah, maybe you're right."
    m "Lorem moved closer, cuddling into my side, and wrapping their small tail around my back."
    c "Someone’s suddenly very clingy."
    Lo normal blush "It’s because of your warm soft skin, and now I know you're okay with... {w}{i}us{/i},{w=0.5} I'm definitely gonna do this more often, now that I know about it."
    m "I said nothing in response, I just smiled at them and put my arm around their shoulder, pulling them closer."
    m "We ate our breakfast together and afterwards set the plates aside, continuing to cuddle on the couch, just wanting to truly enjoy the quiet, peaceful moment together."
    m "I looked down at Lorem, who had a huge grin, and adorable blush, leaning into me."
    menu:
        "Caress their side.":
            m "I moved my hand from Lorem’s shoulder and began to gently caress their side."
            play sound "fx/purr.ogg"
            m "And in response Lorem started purring adorably, and moving closer to me, nuzzling their head into my chest."
            Lo sleep blush "Your hands feel amazing..."
            m "I continued to caress them for a while longer, enjoying listening to their contented purring."
            c "You’re really enjoying this, huh?"
            Lo "I never thought {i}I’d{/i} be jealous of someone's hands; I hope you do stuff like this more often..."
            c "Maybe I will, just for you."
            $ renpy.pause (3.0)
            stop sound fadeout 3.5
            m "I stopped after a while, and consequentially the purring did too, Lorem sighed, then moved away slightly to look up at me."

        "Just cuddle.":
            m "I didn’t want to rush things and possibly make Lorem uncomfortable, so we continued to cuddle together on the couch."
            m "Their small tail subtly wrapped itself around my back even further, and one of their hands rested on my thigh."
            c "(I didn’t expect Lorem to be this comfortable already, given how nervous they were before, but I'm definitely not complaining.)"
            $ renpy.pause (2.5)
            m "After cuddling for a while longer, Lorem sighed, then moved away slightly to look up at me."

    Lo sad "I wish we could stay like this for longer, but I have work later..."
    c "Well, when are you next free?"
    Lo think "After work I’ll be busy, so tomorrow."
    c "That’s convenient."
    play sound "fx/undress.ogg"
    $ renpy.pause (3.0)
    m "I walked Lorem to the door, but just as they were about to leave, they turned back around towards me. With an assisting flap of their wings, they jumped up to kiss my cheek before leaving."
    play sound "fx/kiss.wav"
    $ renpy.pause (0.5)
    Lo normal blush "I-I'll see you tomorrow!"
    c "See ya."
    $ renpy.pause (0.5)
    hide lorem with easeoutleft

else:
    show lorem think with dissolve 
    m "I sat down, and as we ate, I noticed that Lorem was very quiet, it seemed they were occupied with their thoughts."
    c "Hey Lorem, you alright?"
    Lo "Huh? Oh, I was just thinking about how I reacted when we were in that underground building."
    Lo relieved "You managed to be brave and stay calm, while I was scared, like a coward."
    c "Lorem, you aren’t a coward, and I can tell you why."
    Lo "You don’t need to lie to make me feel better, I know I was scared and afraid the entire time we were down there..."
    c "Exactly, you were scared, but that doesn't mean you’re a coward, if you really were, you wouldn’t have done anything, yet you did."
    show lorem think with dissolve 
    c "A coward would have just given up, but despite being scared and having little hope, you didn’t give in and persevered, that’s true bravery."
    Lo "..."
    Lo normal "You’re right, I just thought that because I was comparing myself to how fearless you were."
    c "Oh, no, I was scared too."
    Lo think "Really? It definitely didn’t seem that way."
    c "I just didn’t show it because I knew the impact of how I reacted would have had on you."
    Lo normal "Well, I'm glad you did, that whole situation definitely could have ended a lot worse."
    c "Yeah..."
    Lo think "So, that’s... four times you’ve saved my life now? From Reza, the store when that shelf fell on me, in the underground building and soon enough, the comet."
    c "And you saved mine by telling me to throw the Ixomen Sphere at Reza."
    Lo normal "Heh, after saving each other that much we must be bonded for life then, huh?"
    c "I guess so."
    $ renpy.pause (1.5)
    show lorem relieved with dissolve 
    m "Lorem sighed."
    Lo think "I wish we could hang out more, but I have work later."
    c "Well, when are you next free?"
    Lo "After work I’ll be busy, so tomorrow."
    c "We can hang out then, assuming you don’t have plans already."
    Lo normal "I don’t, so I’ll see you then."
    c "See ya."
    $ renpy.pause (0.5)
    hide lorem with easeoutleft

$ renpy.pause (1.0)
scene black with dissolveslow 
stop music fadeout 2.0
$ renpy.pause (4.0)

jump ryann_lorem2_lo8_start



