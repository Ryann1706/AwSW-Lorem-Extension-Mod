
label ryann_lorem2_ipsum:

$ save_name = (_("LI - Ipsum"))

scene o4 with dissolveslow
play music "mx/sail.ogg"
m "I woke up like any other day, but still adjusting to not having any pressure or worry about Reza."
m "I pondered what I could do for the day, then I remembered Ipsum asking to do some tests on me."
c "(Well, I don’t really have any other plans, so I guess I could.)"
play sound "fx/phonepickup.ogg"
$ renpy.pause (0.5)
play sound "fx/phonering.ogg"
$ renpy.pause (3.5)
stop sound

Lo "Hello?"
c "Hey Lorem, is Ipsum there?"
if rnloremromance > 3:
    Lo "O-Oh, hey [player_name], I’ll... uh, get him for you now..."
else:
    Lo "Hey [player_name], I can get him now for you."

$ renpy.pause (2.0)
Ip "Hey [player_name], what is it?"
c "I know it’s a bit short notice, but I can come in for those tests you wanted to do."
Ip "Actually, it’s perfect timing, I don’t start work for a while, so we can do it in... roughly an hour?"
c "Sounds good to me."
Ip "I’ll meet you outside and bring you to the testing room."
c "See you soon then."
play sound "fx/phonepickup"
c "(Guess I just have to wait for a bit now...)"
c "(Also, I should finally give Ipsum his Ixomen Sphere back...)"
$ renpy.pause (1.5)

scene black with dissolveslow
$ renpy.pause (1.0)
stop music fadeout (1.5)
play sound "fx/steps/clean.wav"
$ renpy.pause (2.0)
scene gate with dissolveslow
play music "mx/anna3.ogg"
m "I got to the production facility and Ipsum wasn’t there."
c "(Guess I'm the first one here.)"
m "I didn’t have to wait long though."
show ipsum normal with easeinright
Ip "Hey, how long were you waiting for?"
c "Only a few minutes."
Ip "Well, I’ll show you to the testing room then."
scene black with dissolveslow
$ renpy.pause (1.0)
scene testingroom with dissolveslow
$ renpy.pause (1.5)
show ipsum normal with dissolve

Ip "We’re actually pretty lucky to have gotten this room. Usually it has to be reserved days in advance."
c "I see."
c "Also, before I forget, I brought your Ixomen Sphere with me."
Ip happy "Great, you can leave it there and I’ll bring it home after my shift."
c "Alright."
play sound "fx/spheretake.ogg"
c "So, could you tell me more about these tests?"
Ip normal "Don’t worry, I'm not doing anything too invasive, just taking a few samples and scans."
Ip "I won't do anything if you’re not comfortable with it though."
c "Alright, I’ll keep it in mind."
$ renpy.pause (1.5)
Ip think "Coming here wasn’t the only reason to do these tests though..."
c "What’s the other reason?"
Ip normal "I wanted to talk to you in private about Lorem, and given the nature of this room, privacy is pretty important."
c "What did you want to talk about?"
Ip "I wanted to say how much I appreciate you spending time with Lorem."

if c4witnessavailable == False:
    Ip "Like I've said before, they don't have many friends, so getting to spend time with someone else other than me, especially a human, has been really good for them."
else:
    Ip "They don't have many friends, so getting to spend time with someone else other than me, especially a human, has been really good for them."

Ip "They seem so much more cheerful and optimistic lately, which I think is your doing."
Ip "After everything else they've been through, they really need the support."
$ renpy.pause (1.5)
Ip think "I'm assuming they told you about their... {w}condition already?"
c "They did."
Ip "How did you react?"
c "I told them I didn’t mind at all, and hugged them."
Ip happy "I'm really grateful about that. Other people haven't been as understanding."
$ renpy.pause (1.0)
Ip normal "Anyway, sorry about rambling, now one thing before we start doing this."
play sound "fx/ryanncurtainpull.mp3"
m  "Ipsum walked over to the curtains in the room and pulled them fully out."
Ip "I'm assuming because of the clothes you’re wearing, humans don’t like being exposed?"
c "Yes, that’s true."
Ip think "If you don’t mind me asking, why?"
c "Well, one reason is because human skin isn’t as good of an insulator as fur or scales, so in the past clothes were the solution."
c "Also, as our society was developed it became a social norm and law to wear clothes."
c "For humans, wearing little or no clothes infront of someone, is either seen as inappropriate and shameless, or as a sign of affection, and an implication of something more... intimate."
Ip sad "Ah, I’m sorry if I made you feel uncomfortable or offended you when I said I was curious what was under your clothes earlier then."
c "It’s fine, you didn’t know."
$ renpy.pause (0.5)
show ipsum think with dissolve
$ renpy.pause (1.0)
Ip "Okay, could you wait behind here while I prepare this machine?"
m "I stood behind the curtain while Ipsum walked over to a machine and started interacting with it."

if annadead == True:
    $ renpy.pause (2.0)
    c "Did you hear about what happened to Anna?"
    Ip "Yes, I was told about her death, but not much more than that."
    c "She was one of Reza's victims."
    Ip sad "Oh, I didn't know that part."
    $ renpy.pause (1.5)
    Ip "She wasn’t an amazing person, she was arrogant, stubborn and had a superiority complex, or at least that was my impression of her."
    Ip "But there's no denying she was a genius, and she made great contributions to the scientific community, it definitely was a great loss."
    $ renpy.pause (2.0)
    m "We had a few minutes of silence while waiting for the machine to start-up."

else:
    m "I was about to ask something when I heard loud angry footsteps approaching the room."
    play sound "fx/ryanndoorslam.mp3"
    show ipsum normal with dissolve
    show ipsum at right with move 
    show anna rage b flip at left with easeinleft
    An "Ipsum!" with vpunch
    Ip "Oh, hello Anna, what a pleasant surprise it is for you to visit."
    An "Don’t you dare test me right now! I just saw you booked this room to test on [player_name], when I {i}specifically{/i} told you I was the only one allowed to do that."
    m "I stepped out from behind the curtains."
    c "You know I'm right here, right?"
    if annastatus == "bad" or annastatus == "abandoned":
        An face b flip "I was hoping you weren't."
        if annastatus == "abandoned":
            An "Also, really cool of you to completely ghost me, I didn’t realize sending a 20 second voice message was such a strenuous task for humans."
        else:
            pass
    else:
        An sad b flip "No, I didn’t."

    $ renpy.pause (1.5)
    if rnagreedannatest == True and rndidannatest == False and rncancelannatest == False:
        # If agreed to the tests, but didnt do or canncel them
        An disgust b flip "Regardless, you agreed for me to do tests on you, then you just don’t follow through, and let Ipsum do them instead?"
        c "Okay, I will admit, that’s my bad, but I'm an ambassador, did you expect me not to be busy, especially when I'm helping the police?"
        c "Ipsum’s gonna do some tests anyway, can't he just share the results with you?"

    elif rndidannatest == True:
        # If did the tests
        c "You already did your tests on me, we agreed you could do tests on me, not {i}only{/i} you could do tests on me."
        c "This is something completely separate from what you wanted to do, so why are you mad?"

    elif rncancelannatest == True:
        # If canceled the tests because Anna's lab got raided
        c "I agreed for you to do tests on me, but did you forget that we canceled doing them because of what happened to your lab?"
        An face b flip "No, I obviously didn’t forget."
        c "So why are you mad that Ipsum is doing it, if you can’t?"

    else:
        # If didnt agree to do the tests
        c "Also, when did we agree on that?"
        An face b flip "What?"
        c "When did we agree you could do tests on me?"
        An sad b flip "Well, we didn’t..."
        c "And you’re mad I'm actually letting Ipsum do tests on me, even though you doing them was never even mentioned before?"

    An sad b flip "..."
    An face b flip "..."
    An disgust b flip "It’s not about those tests, it's about him going against what I specifically told him."
    An normal b flip "It doesn't matter anyway, now that I've gotten hold of one of your PDA’s."
    Ip normal "If it doesn't matter anyway, then why did you come storming in here and have a temper tantrum?"
    An disgust b flip "Shut your mouth Ipsum."
    Ip "That’s not very nice."
    c "What did you want from the PDAs anyway?"

    if annastatus == "bad" or annastatus == "abandoned":
        An disgust b flip "Why the hell do you care? How about you mind your own business?"
        c "It is my business if it's about the PDAs, considering they belong to humanity."
        An face b flip "I just needed medical data, now shut up about it."

    elif annastatus == "good":
        An smirk b flip "Oh, just some medical data that could save my, and millions of others lives."

    else:
        An normal b flip "I just needed medical data."
        c "Thats vague."
        An face b flip "And? Do you want an entire list of things I've looked at?"

    An disgust b flip "I'm going. But Ipsum I'm warning you. You’re on thin ice."
    show anna disgust b with dissolve 
    $ renpy.pause (0.3)
    hide anna with easeoutleft
    $ renpy.pause (1.0)
    show ipsum at center with move

    Ip think "Well, that was... interesting."
    c "So much for this room having privacy."
    Ip normal "It was pretty impressive that you actually managed to talk back to her, when most people try they just get shut down completely."

$ renpy.pause (1.5)
Ip "Alright, this should be ready now."

if rndidannatest == True:
    c "That’s for looking at muscle groups, bones and organs, right?"
    Ip think "Yep, I'm assuming Anna used this on you then?"
    c "Yeah."
    c "(Hopefully this being used on me twice doesn't give me a dragon's dose of radiation.)"

else:
    c "What are you doing?"
    Ip normal "This lets me see your muscles, bones and organs, not in much detail, it's more of a general overview."

Ip normal "Just lie down here, you can still talk, but try not to move too much, it should only take a minute or two."
c "Alright."
play sound "fx/bed.ogg"
$ renpy.pause (1.0)
c "So, what else were you going to do?"
Ip think "Honestly, I'm just doing stuff as I go, doing this whole thing was really short notice on both our ends."
play soundloop "fx/startx.ogg"
queue soundloop "fx/hum.ogg"
Ip normal "So, we won't be doing a huge number of things."
c "Like what?"
Ip think "Maybe I’ll take some blood, a hair and nail sample, and unrelated but I'm really intrigued by the fact you don’t have a tail."
c "I can understand the interest in blood, but why hair and nails?"
Ip "Well, obviously I have hair too, but it’s actually pretty uncommon for dragons, I want to know how similar or different it is."
c "Well, most humans have hair on their head, and some people have hair on more parts of their body, but that depends on gender and genetics."
Ip "Stuff like that is a lot more interesting to me than you’d think, for dragons, gender has no influence on hair."
c "Interesting."
Ip "Also, about nails, all dragons have claws, most other mammals and reptiles here too, so why you still have nails from an evolutionary perspective bewilders me."
c "Well, claws are better for things like slashing and puncturing, but nails are better for grabbing and climbing, which were more beneficial to humans in the past."
c "Speaking of past humans, we used to have tails, but lost them to evolution and got our upright stance, all we have left is a bone called the coccyx."
Ip "I see."
stop soundloop fadeout 2.0
$ renpy.pause (1.5)
Ip normal "Alright, this machine is done, you can get up now."
if rndidannatest == True:
    c "Wait, but when Anna used it, it took some time to prosses the data, why didn’t it now?"
    Ip "It already has, it finished scanning while we were talking, you looked comfortable so I let you stay lying down."
    c "Alright."
else:
    pass

play sound "fx/bed.ogg"
$ renpy.pause (1.0)
Ip think " Okay, for this next part you’ll need to take off some of your clothes, more specifically the part covering your chest and abdomen."
Ip normal "Again, only if you’re okay with it."
c "I don’t really mind, also it’s called a shirt."
Ip "Got it."
play sound "fx/undress.ogg"
m "I stood behind the curtain Ipsum provided and took off my shirt, putting it aside for the time being."
c "So, what is this for?"
Ip think "Remember I mentioned the other machine was more of a general overview? Well, this one can give a more detailed look at some of your organs."
c "How does it do that?"
Ip normal "The simplest way to explain is it’s like a very specific and detailed ultrasound."
c "Alright."
play sound "fx/button_press.ogg"
m "Ipsum proceeded to point the machine at my abdomen and lower chest, taking a decent number of scans."
play sound "fx/undress.ogg"
m "Afterwards he moved the machine away, while I got redressed."

Ip "I don't want to keep you here too long, so I’ll just take some samples and look at them in more detail later."
play sound "fx/rummage.wav"
m "Ipsum rummaged through a drawer and pulled out a few things."
if blood == True:
    m "Some scissors, something that looked near identical to some nail clippers and the same tube and needle Anna had used before, or hopefully a different one that just looked the same."
    Ip normal "Can I have your hand?"
    m "I gave Ipsum my hand, a bit apprehensive, but I at least knew what to expect this time."
    m "The needle stuck into my hand; the pain wasn't as bad as the first time but it still did hurt."

else:
    "Some scissors, something that looked near identical to some nail clippers and a tube with some kind of needle attached to it."
    Ip normal "Can I have your hand?"
    m "I gave Ipsum my hand, which he then put the tube onto the back of my hand."
    m "I recoiled slightly from pain caused by something sticking into the back of my hand."

m "Afterwards some blood dropped into the vial, and Ipsum set it aside, taking another two smaller vials from a cupboard."
Ip think "I don’t know your biology well enough yet, so you can take the other two samples."
play sound "fx/ryannhaircut.mp3"
m "I took the scissors and cut off a small cluster of hairs, and put it into one of the vials."
play sound "fx/nail.ogg"
m "Followed by a piece of nail, in the other."
show ipsum normal flip with dissolve
$ renpy.pause (0.2)
show ipsum at right with move
play sound "fx/clink2.ogg"
m "I gave Ipsum the two vials, which he then took the three of and put in the back of a cupboard."
Ip think "They should be safe there until I get them later."
show ipsum normal with dissolve
show ipsum at center with move
Ip happy "Now that all that’s over with, we can have some fun."
c "What do you mean?"
Ip "You didn’t think these tests were going to be the only thing we’d do, did you?"
c "I kinda did, but I'm assuming you had something else planned?"
Ip "Of course, just doing those tests would have been really boring, so we're going to do some good old-fashioned mischief too."
c "What did you have in mind then?"
Ip normal " Actually, I thought you could come up with something. That game you told us earlier was pretty fun, so maybe whatever you come up with will be good too."
c "Alright, let me think..."

label ryann_lorem2_ipsum_prank:

menu:

    "Ipsum’s idea":
        jump ryann_lorem2_ipsum_ipsumidea 

    "Pull the fire alarm" if not ryannipsumalarm:
        $ ryannipsumalarm = True 
        c "We could pull the fire alarm."
        Ip think "That could be pretty dangerous given some of the things done here, so maybe think of something else?"
        jump ryann_lorem2_ipsum_prank

    "Use the Ixomen Sphere":
        jump ryann_lorem2_ipsum_sphere

    "Scare someone":
        jump ryann_lorem2_ipsum_scare



label ryann_lorem2_ipsum_ipsumidea:

c "I can’t really think of anything. Do you have any ideas?"
Ip think "Hmm..."
$ renpy.pause (1.5)
Ip happy "I got it."
c "What is it?"
if annadead == True:
    Ip normal "We need to take a trip to Damion's lab."
    c "Let’s go then."

else:
    Ip normal "We need to take a trip to Anna’s lab."
    c "Are you sure that’s a good idea? Anna did say you were on thin ice."
    Ip happy "But it couldn’t have been us doing anything, we were in the testing room the whole time, right?"
    c "Right, I almost forgot that part."

scene ryannfacilitylab with dissolveslow
show ipsum normal with dissolve
m "We made our way to the lab, and thankfully no one was inside."
Ip "I need a minute to get a few things."
show ipsum normal flip with dissolve
$ renpy.pause (0.3)
hide ipsum with easeoutright
m "Ipsum then walked into a small storage closet in the back of the room."
$ renpy.pause (2.0)
show ipsum normal with easeinright
m "After a minute he returned with two beakers and a piece of string, one of the beakers had a piece of metal in it, while the other was empty. "
c "What’s that?"
Ip happy "Just some potassium."
c "And what’s it for?"
Ip "Well, I'm sure you’re aware of how reactive potassium is with water, and it sure would be a shame if something like that were to happen unexpectedly and scare someone."
$ renpy.pause (1.0)
play sound "fx/faucet2.ogg"
$ renpy.pause (2.5)
stop sound fadeout (1.0)
$ renpy.pause (1.0)
show ipsum at left with move
m "He walked over to a sink and mostly filled one beaker with water and brought it over to the door we came through."
play sound "fx/glassdown.wav"
m "He put the empty beaker upside down with the potassium on top of it, and the water filled beaker next to it."
m "The door was fully opened with the string tied to the handle, then loosely put around the potassium, the slightest movement ready to nudge it into the water."
show ipsum normal flip with dissolve
$ renpy.pause (0.3)
show ipsum at center with move
Ip think flip "Now we just need to conceal it in some way."
m "We looked around the room looking for something to hide the newly built trap, when I spotted a filing cabinet at the back of the room."
play sound "fx/rummage3.ogg"
m "I checked inside and found an unused folder."
c "This will work nicely."
m "With the folder now in place, we were ready."
Ip happy flip "Now we leave, and wait."

scene testingroom with dissolveslow
show ipsum normal with dissolve
m "We made our way back to the testing room and eagerly waited."
m "After not too long, we heard footsteps down the hallway, followed by..."
play sound "fx/ryanndistantexplosion.mp3"
$ renpy.pause (1.5)
if annadead == True:
    Dm "Who the hell did this?!"
else:
    An "Which one of you bastards did this?!" with vpunch

Ip happy "I didn’t expect that to be loud enough to be heard through the wall, heh."

if annadead == True:
    m "Damion almost walked by, but came in when he saw us in the room."
    play sound "fx/door/door_open.wav"
    show ipsum normal with dissolve
    show ipsum at right with move
    show damion arrogant flip at left with easeinleft
    Dm "Ipsum, would you care to explain the explosion that just happened in my lab?"
    Ip think "Well, we heard it, but we’ve been in here the whole time."
    Dm "So, who did it then?"
    Ip normal " Not sure how either of us are supposed to know that."
    Dm "Well, it had to be someone."
    Ip "You know I reserved this room for [player_name], why would I waste this opportunity to do that?"
    $ renpy.pause (1.5)
    Dm "Fine, but I’ll find who did this."
    Ip "Have fun doing that."
    show damion arrogant with dissolve 
    $ renpy.pause (0.3)
    hide damion with easeoutleft
    $ renpy.pause (1.0)
    show ipsum at center with move
    m "As soon as Damion left our earshot, we started chuckling."

else:
    m "Anna stormed in again, just as she did earlier."
    play sound "fx/ryanndoorslam.mp3"
    show ipsum normal with dissolve
    show ipsum at right with move
    show anna rage b flip at left with easeinleft
    An "IPSUM!" with vpunch
    Ip "Welcome back Anna, did you-{w=0.5}{nw}"
    An "Don’t you dare play dumb now! Did you do it?"
    Ip think "I don’t even know what {i}it{/i} is."
    An "The explosion in my lab!"
    Ip "We did hear that, but we’ve been in here the entire time. Also, you said I'm on thin ice, why would I then go and do something like that?"
    An face b flip "..."
    An disgust b flip "Who the hell was it then?"
    Ip normal "I'm not sure how we’re supposed to know that."
    An "If I find out this was you, you’re dead."
    Ip "Good luck finding whoever did it then."
    show anna disgust b with dissolve
    $ renpy.pause (0.3)
    hide anna with easeoutleft
    $ renpy.pause (1.0)
    show ipsum at center with move 
    m "As soon as we were sure Anna was out of earshot, we burst out laughing. "

c "I got to admit, it’s pretty impressive being able to lie on the spot like that."
Ip happy "This isn't my first time doing something like this. I’ve never been caught, and I never will."
c "I don’t doubt it."

jump ryann_lorem2_ipsum_end

label ryann_lorem2_ipsum_sphere:

c "Maybe we could use your Ixomen Sphere to do something?"
Ip happy "See, that’s the kind of thing I never would have thought of, the question is what to do with it."
c "You know it way better than I do."
Ip normal "True, and I have an idea that just might work."
play sound "fx/spheretake.ogg"
Ip "Listen to this."
play sound "fx/knocking1.ogg"
$ renpy.pause (2.0)
c "Woah, that's really realistic."
Ip happy "Exactly, now if someone were to hear this, then open the door and no one's there..."
c "They might get a bit annoyed."
Ip "Now we just need to find our victim."
c "Wait, wouldn’t they see or hear it though?"
Ip normal "Not if it was silently floating above the doorway."
c "It can float silently?"
Ip "It really drains the battery, but yes. We’re not going to be doing this for too long and you brought the charger with you, so we’re fine."
Ip "Speaking of the charger, it also doubles as a controller, so we don’t even need to be near the door."
c "I might need to get one of these for myself... "
Ip happy "It will be completely worth it, trust me."
Ip "Now, let's have some fun."

hide ipsum with dissolve
scene facin2 with dissolveslow
m "Ipsum and I stood in the doorway of the testing room with the door slightly ajar, peeking out of it, watching the sphere make it's way down the corridor."
m "It got to infront of the door and started floating higher, out of eyeshot of anyone in the room."
play sound "fx/knocking1.ogg"
$ renpy.pause (2.5)
play sound "fx/door/door_open.wav"

if annadead == True:
    $ renpy.pause (0.5)
    show damion normal at right with easeinright
    Dm "Yes?"
    Dm face "What?"
    $ renpy.pause (1.5)
    Dm arrogant "Oh."
    show damion arrogant flip with dissolve
    $ renpy.pause (0.3)
    hide damion with easeoutright
    play sound "fx/door/door_close.ogg"
    $ renpy.pause (1.0)
    play sound "fx/knocking1.ogg"
    $ renpy.pause (2.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (0.5)
    show damion arrogant at right with easeinright
    Dm "Really mature, whoever this is, I hope you’re realizing you’re interrupting actually important work."
    show damion arrogant flip with dissolve
    $ renpy.pause (0.3)
    hide damion with easeoutright
    play sound "fx/door/door_close.ogg"
    Ip "Seems like he’s getting annoyed already, heh, but for how arrogant he is, he deserves it."
    play sound "fx/knocking1.ogg"
    $ renpy.pause (2.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (0.5)
    show damion arrogant at right with easeinright
    Dm "This is childish at this point, just stop it or else I’ll find who this is."
    c "“Just stop it”, he sounds like a whiney child."
    Ip "He definitely has the same scene of self-importance as one."
    show damion arrogant flip with dissolve
    hide damion with easeoutright
    play sound "fx/door/door_close.ogg"
    $ renpy.pause (0.5)
    play sound "fx/knocking1.ogg"
    $ renpy.pause (2.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (0.5)
    show damion face at right with easeinright
    Dm "Seriously, this isn't funny, grow up."
    m "It was hard for us to continue without chuckling pretty hard at this point."
    c "Why does he keep falling for it?"
    Ip "I don’t know, but I'm not complaining, we should stop before he starts crying though."
    c "Judging by how he’s acting he's not far from it "
    scene testingroom with dissolveslow
    show ipsum normal with dissolve
    m "After making sure Damion wasn’t at the door, Ipsum brough the sphere back."

else:
    show anna normal b at right with easeinright
    $ renpy.pause (1.0)
    An "I'm pretty busy right now, so-"
    $ renpy.pause (1.0)
    show anna face b with dissolve
    $ renpy.pause (0.5)
    An "Seriously?"
    show anna face b flip with dissolve
    $ renpy.pause (0.3)
    hide anna with easeoutright
    $ renpy.pause (1.0)
    play sound "fx/knocking1.ogg"
    $ renpy.pause (2.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (0.5)
    show anna disgust b at right with easeinright
    An "Really mature, I bet you’re finding it hilarious that you’re wasting both of our time here, grow up!"
    show anna disgust b flip with dissolve
    hide anna with easeoutright
    c "She really is hot headed, huh?"
    Ip "That’s why she's one of my favorite targets."
    play sound "fx/knocking1.ogg"
    $ renpy.pause (2.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (0.5)
    show anna disgust b at right with easeinright
    An "Which one of you bastards keeps doing this? You’re dead when I get my hands on you!" with vpunch
    show anna disgust b flip with dissolve
    $ renpy.pause (0.3)
    hide anna with easeoutright
    m "It was hard for us to continue without laughing at this point."
    play sound "fx/knocking1.ogg"
    $ renpy.pause (0.5)
    stop sound
    play sound "fx/ryanndoorslam.mp3"
    show anna rage b at right with easeinright
    m "As soon as the sound played from the sphere, Anna swung the door open expecting to find the culprit, but only found an empty corridor."
    An "You better get out here now or I’ll slit your neck when I find you!" with vpunch
    c "How is she this mad already?"
    Ip "That’s just how she is, be glad you don’t work with her."
    hide anna with dissolve
    scene testingroom with dissolveslow
    show ipsum normal with dissolve
    m "In fear of Anna reaching her mental limit and snapping completely, we slowly retrieved the Sphere."

Ip happy "Again, that was a lot more fun than I thought. I might just do this again at some point."
c "I’ve said it before, but that Sphere really is useful."
Ip normal "Can you say that more often in front of Lorem so they’ll stop saying it’s a toy for grown-ups?"
c "I will if I remember."
Ip "Thank you."

jump ryann_lorem2_ipsum_end

label ryann_lorem2_ipsum_scare:

c "It’s pretty simple, but we could just scare someone?"
Ip normal "Ah, a classic, it is pretty simple, but who said it needed to be complex?"
Ip "Now we just need to find our victim."
show ipsum at left with move
m "Ipsum stepped into the hall and looked around, then suddenly came back in the room."
show ipsum normal flip with dissolve
Ip "There’s someone down the hall, I’ll call them over here then you can jump out and scare them."
c "That’s convenient."
show ipsum normal with dissolve
hide ipsum with easeoutleft
$ renpy.pause (1.5)
Ip "Hey, excuse me, could you help me over here for a second?"
m "I waited for Ipsum to give me some kind of signal to jump out."
$ renpy.pause (2.0)
m "The door was open enough for me to jump out, and see Ipsum, but not enough for me or the other person to see each other."
m "Ipsum signaled me and I leaped through the door."
scene facin2 
show ipsum normal at right
show maverick normal b flip at left 
with dissolve
$ renpy.pause (0.3)
show maverick scared b flip with dissolve
m "But I stopped dead in my tracks when I saw Maverick."
$ renpy.pause (0.7)
show maverick normal b flip with dissolve
$ renpy.pause (0.7)
if ryannmavapology == True:
    show maverick nice b flip with dissolve
    $ renpy.pause (0.7)
    show maverick laugh b flip with dissolve
    Mv "{i}HA.{/i}" with vpunch
    Mv "For you, of all people, to be able to scare someone like me? That’s amazing."
    Mv nice b flip "I see you really have put all that behind us."
    c "Shouldn’t you be on sick leave?"
    Mv normal b flip"You know well how understaffed we are, after persisting about it for long enough I was allowed to do less exerting things."
    c "Like what?"
    Mv "Naomi is the only other flyer available, so I'm collecting and dropping off reports and other things like she would."
    c "With an injured leg?"
    Mv "It’s either this, or field work, and this is better than wasting my time doing nothing."
    c "Fair point."
    Mv "I’ve got to get going."
    c "Alright."
    hide maverick with easeoutright
    $ renpy.pause (1.5)
    Ip "It’s refreshing to find someone who can actually take a joke instead of getting unreasonably angry."
    Ip happy "It is pretty funny when that happens though."

else:
    show maverick angry b flip with dissolve
    $ renpy.pause (0.7)
    Mv "Is this a joke?"
    c "Yeah kinda."
    Mv "Do you really find this funny?"
    c "Eh, little bit."
    Mv "I tried to apologize earlier, but you didn’t accept it, and now you’re doing this? That’s just childish."
    c "Aw, did the big scary dragon get scared by me and is embarrassed by it now?"
    m "He said nothing in response, he just glared at me and continued walking."
    $ renpy.pause (0.3)
    hide maverick with easeoutright
    $ renpy.pause (0.5)
    show ipsum at center with move 
    Ip happy "Heh, well someone's pretty annoyed."

show ipsum at center with move 
c "Well, that deffinetly could have gone worse."
Ip normal "I at least thought it was a bit funny."

jump ryann_lorem2_ipsum_end


label ryann_lorem2_ipsum_end:

$ renpy.pause (2.0)
Ip think "Wait, what time is it?"
Ip "Ah, my shift is starting soon, so it looks like this is the end of our get together."
c "I guess it is, I had a really great time though."
Ip normal "Maybe we should hang out again at some point?"
c "Sure, hopefully Lorem doesn't get jealous."
Ip happy "I don’t think they will, if anything they’ll be grateful their favorite dragon and favorite human are getting along."
Ip normal "Also, that reminds me, Lorem told me that they wanted to hang out with you again soon."
c "Maybe they are jealous?"
Ip happy "Heh, let’s hope not."
Ip normal "Anyway, I’ll see you later, thanks again for doing this."
c "See ya."

scene black with dissolveslow
$ renpy.pause (4.0)
stop music fadeout 2.0

jump ryann_lorem2_lo7_start

