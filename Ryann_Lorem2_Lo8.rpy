
label ryann_lorem2_lo8_start:

$ save_name = (_("LI - Lorem 8"))

scene loremapt with dissolveslow
play sound "fx/knocking1.ogg"
$ renpy.pause (2.0)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)
play music "mx/feelings.ogg"
show lorem normal with dissolve
$ renpy.pause (0.5)

Lo "Hey [player_name]."
c "Hey Lorem, so, what did you want us to do today?"
Lo think "Well, I don't really know, I couldn’t really think of anything."
if rnloremromance > 3:
    Lo blush "It’s just... now that we’re… {w}you know..."
    c "Dating?"
    Lo "Yeah…"
    c "You wanted us to go on our first proper date?"
    Lo normal blush "You read my mind."
    Lo think "Ipsum is also off work, he’s just in his room, so we can’t stay here."
    c "Well, as long as we’re together it doesn’t really matter what we do. We can just make it up as we go along."
    Lo "Right... But we do have to start somewhere."
    c "How about going to a cafe, and we can try to think of something else to do after?"
    Lo normal "Sounds good to me."

else:
    Lo "It’s just… I want to make up for the other day, it’s my fault we were down there, so I wanted to apologize by us doing something together."
    c "No, you shouldn’t be apologizing. I was the one who insisted on going down there, it’s my fault."
    Lo "But you wouldn’t have insisted if I hadn't brought it up in the first place."
    $ renpy.pause (1.5)
    c "There's no point in us arguing over this, let's just say we’re both responsible for going down there, and leave it at that."
    Lo normal "Alright."
    Lo think "Still, we could both really use today to help us destress from all that."
    c "How about going to a cafe first, and think of what else to do later?"
    Lo normal "Sure, let’s go then."

$ renpy.pause (1.0)
play sound "fx/steps/clean.wav"
scene black with dissolveslow
$ renpy.pause (3.0)
scene cafe with dissolveslow
show lorem normal with dissolve

m "We then made our way to a cafe, and thankfully, there were very few people there, so we could sit pretty much anywhere we wanted."
play sound "fx/chair.wav"
m "We sat next to the window, wanting to enjoy the sunlight and fortunately nice weather."

if adinedead == True:
    m "And after a bit of waiting, a waitress came over to our table."
    waitress "Welcome, what can I get for you two?"

else:
    m "And soon after, Adine made her way over to us."
    show lorem at Position(xpos=0.8) with ease
    $ renpy.pause (0.5)
    if adinestatus == "bad" or adinestatus == "abandoned":
        show adine annoyed b flip at left with easeinleft
        Ad "As much as I don’t want to, I'm required to take your order."

    elif adinestatus == "good" or adinestatus == "neutral":
        show adine normal b flip at left with easeinleft
        Ad "Hey [player_name], and Lorem, you two are still hanging out together I see."
        c "That we are."
        Ad "Well, I hope you two have fun."
        Ad "Also, [player_name], I enjoyed hanging out last time, so if you wanted to meet up again, I wouldn’t mind."
        c "Wait a second… {w}You’re not jealous of Lorem, are you?"
        Ad giggle b flip "Oh shush, I'm not!"
        Ad normal b flip "Anyway, what can I get both of you?"

    else:
        show adine normal b flip at left with easeinleft
        Ad "Hello Lorem, and [player_name], nice to see you both."
        c "Hey Adine, how's work going?"
        Ad "Well, we only opened not too long ago, so not bad so far."
        Lo "Hopefully it stays that way."
        Ad giggle b flip "Hopefully it does indeed."
        Ad normal b flip "Speaking of work, what can I get you two?"

Lo think "Well, I'm not really that hungry."
c "Neither am I, but let’s at least get something to drink."
menu:
    "Water":
        $ ryannplayerdrink = "water"
        c "I'll just have water."

    "Tea":
        $ ryannplayerdrink = "tea"
        c "I'll have some tea."

    "Coffee":
        $ ryannplayerdrink = "coffee"
        c "I'll have some coffee."

    "Soda":
        $ ryannplayerdrink = "soda"
        c "I'll have some soda."

if ryannplayerdrink == "tea":
    Lo normal "I’ll also have tea."
else:
    Lo normal "And I’ll have tea."

if adinedead == False:
    if  adinestatus == "good" or adinestatus == "neutral" or adinestatus == "none":
        Ad "I'll be back in a few minutes with your order then."
        show adine normal b with dissolve
        $ renpy.pause (0.3)
        hide adine with easeoutleft
        

    else:
        show adine annoyed b with dissolve
        $ renpy.pause (0.3)
        hide adine with easeoutleft

else:
    waitress "I'll be back with your orders soon."

$ renpy.pause (0.3)
show lorem at center with ease
$ renpy.pause (0.5)

if ryannplayerdrink == "coffee":
    c "I don’t know why, but I expected you to get coffee too."
else:
    c "I don’t know why, but I expected you to get coffee instead."

Lo think "Oh, I can't drink coffee, I get way too hyper."
c "Because of how small you are?"
Lo normal "Yeah, that’s why I'm more of a tea person."
c "That must be Ipsum’s influence on you, huh?"
Lo think "You know, I never thought of that, but you might actually be right."
c "Next you’ll be getting an Ixomen Sphere, and Ipsum will start gardening..."
Lo relieved "Oh, haha..."
$ renpy.pause (1.0)
show lorem think with dissolve
$ renpy.pause (0.5)
show lorem think flip with dissolve 

m "Afterwards, me and Lorem started looking out of the window while waiting for our drinks."
if rnloremromance > 3:
    m "But after a minute, I found myself looking at Lorem instead, their beautifully glistening amber eyes and cute little ears and wings, I just wanted to hold them close and protect them."
    Lo shy flip "Uh... [player_name], you’re staring at me..."
    c "You’re so cute, you know that?"
    Lo "Oh... T-Thank you..."

else:
    m "I saw the occasional dragon passing by, glancing or staring at me. I gave a friendly wave or nod, but secretly hoped they wouldn’t come in and interrupt me and Lorem."
    m "Thankfully none did, but they didn’t go unnoticed by Lorem."
    Lo normal flip "Well, looks like someone is pretty popular, huh?"
    c "Do you really blame them for being interested in me? If I recall correctly, you were just as, if not more excited when you first met me."
    Lo "Heh, alright, that's fair."

m "Soon after, our drinks arrived."
show lorem normal with dissolve
$ renpy.pause (0.3)
if adinedead == False:
    show lorem at Position(xpos=0.8) with ease
    if adinestatus == "good" or adinestatus == "neutral" or adinestatus == "none":
        show adine normal b flip at left with easeinleft
        $ renpy.pause (0.3)
        play sound "fx/glasses.wav"
        Ad "Here are your drinks, just let me know if you need anything else."
        c "Will do, thanks Adine."
        show adine normal b with dissolve 
        $ renpy.pause (0.3)
        hide adine with easeoutleft

    else:
        show adine annoyed b flip at left with easeinleft
        $ renpy.pause (0.3)
        play sound "fx/glasses.wav"
        Ad "Here."
        Lo think "Uh... Thank you..."
        show adine annoyed b with dissolve 
        $ renpy.pause (0.3)
        hide adine with easeoutleft 
        $ renpy.pause (0.5)
        Lo "You two really don’t get along, huh?"
        c "Yeah, we don’t, and I’d prefer we don’t go into it."
        Lo "Noted."

else:
    play sound "fx/glasses.wav"
    waitress "Here are your drinks."
    c "Thanks."

show lorem think with dissolve 
show lorem at center with ease
play sound "fx/coffee.wav" # Eh, 1 in 4 is close enough
if ryannplayerdrink == "water":
    m "The water was perfectly cool and refreshing, it was simple, yet still nice."

elif ryannplayerdrink == "tea":
    m "The tea was at a perfectly warm temperature, with just the right amount of sugar and milk in it too, just the right thing to help you relax."

elif ryannplayerdrink == "coffee":
    m "The coffee had a pleasantly strong taste, it was brewed to perfection, and had a nice caffeinated kick to help me get through the rest of the day."

elif ryannplayerdrink == "soda":
    m "The soda wasn’t something I recognised, it was a light blue, slightly lighter than Lorem, which was a slight concern. But it tasted pretty good regardless, it had a nice fizz and sweet taste to it."

m "Lorem didn’t drink though, it looked like they were thinking about something."
c "Hey, what are you thinking about?"
Lo "I was just trying to remember something..."
$ renpy.pause (1.5)
Lo happy "I got it! I know someplace we can go after here now."
c "Where is it?"
Lo normal "I want to keep it a surprise, so you’ll have to wait and see."
c "I’ll be looking forward to it then."
$ renpy.pause (0.5)
m "After finishing our drinks and paying, we made our way outside, and Lorem started leading me somewhere."

scene town3 with dissolveslow
show lorem normal with dissolve
$ renpy.pause (0.5)
c "So, where are we going?"
Lo "There’s a store nearby here, and there’s a few things I wanted to get before we go to where I was thinking of."
c "Still keeping it a surprise?"
Lo "Trust me, it’ll be worth it."
m "After a bit of walking, we got to outside the store."
Lo think "Actually, there’s something I forgot. I’ll be back in a few minutes, would you mind waiting here?"
c "Alright, just don’t take too long."
Lo normal "I won’t."
play sound "fx/flap1.ogg"
$ renpy.pause (0.5)
hide lorem with dissolve
m "Lorem then took off flying, and they were surprisingly fast given how small their wings were."
stop music fadeout 2.0
m "I decided to wait inside, hoping to find something to occupy myself instead of just standing around doing nothing."
play music "mx/zhong.ogg"
scene store with dissolveslow 
play sound "fx/bell2.ogg"
$ renpy.pause (0.5)
if zhongunplayed == False:
    $ renpy.pause (1.5)
    show zhong normal c at right with dissolve
    m "I saw Zhong at the cash register and went to make small talk."
    c "Hey Zhong."
    Zh "Ah, hello [player_name], what brings you here?"
    c "I’m just waiting for someone, after getting some things we’re heading out to do something."
    Zh "Well, I hope you enjoy it and find what you’re looking for here."
    c "So do I."
    c "By the way, how are you and your son doing?"
    Zh smile c "My son’s doing good, we’re getting closer and closer to our holiday, which he’s excited about."
    Zh normal c "As for me, not too bad, it’s been a pretty slow day so far, and it’ll probably stay that way."
    c "You must be enjoying not having much actual work to do though."
    Zh "You’d think, but slow days are at least three times longer than busy days."
    c "And you’re not even getting paid for that extra time..."
    Zh smile c "Hah, exactly."
    play sound "fx/bell2.ogg"
    m "Just then Lorem came back into the store."
    c "It was a nice chat, but I’ve got plans to get back to."
    Zh normal c "Alright, just let me know if you need anything."
    c "Will do."
    $ renpy.pause (0.5)
    hide zhong with easeoutright

else:
    m "I didn’t really have an idea of what I could do to distract myself from waiting, but I just started browsing various things for the time being."
    m "A stand of newspapers and magazines caught my interest first though."
    m "As expected, the newspapers referred to either mine and Reza’s arrival into the dragons world, the recent murders or other things I didn’t have enough knowledge on the dragons world to really understand."
    m "The magazines were a lot more eye-catching though."
    m "There was pretty much any category you could think of, lifestyle, cooking, fitness, catalogs, sports, childrens and some for dragons I assumed were celebrities."
    m "I briefly skimmed over a few in more detail, some by the  names of “Universal Fitness” and  “LIFESTYLE: The Magazine for Modern People” caught my attention more than others did."
    if bryce2magazine == True and adine2unplayed == False:
        c "(So this is where Adine and Bryce get their magazines...)"
    elif bryce2magazine == True:
        c "(So this is where Bryce gets his magazines...)"
    elif adine2unplayed == False:
        c "(So this is where Adine gets her magazines...)"
    else:
        c "(Who would actually buy these?)"

    play sound "fx/bell2.ogg"
    m "After skimming through a few more, Lorem had returned."

show lorem normal with dissolve
$ renpy.pause (0.5)
Lo "Hope you weren't too bored while waiting for me [player_name]."
m "I looked at what Lorem was now holding, it was a wicker picnic basket."
c "What do you have that for?"
Lo "Well, I thought it could be a good idea for us to go on a picnic, earlier I remembered a perfect spot we could go to, and a picnic seemed fitting."
c "Sounds good, and I’m assuming we’re here to get food and other stuff?"
Lo "Exactly."
c "Let’s have a look at what we can find then."
$ renpy.pause (0.5)
hide lorem with dissolve 
m "After doing some searching, comparing and questioning on whether things would put my health at risk, we had a decent selection of snacks for us to enjoy."
m "We had soda, chocolate, crisps, and pretty much any other kind of sweets you could want. {w}Of course we had actual proper food too, nuts, grains, you know, healthy stuff."
m "After getting everything we thought we wanted, we headed towards the checkout."
$ renpy.pause (0.5)
show lorem normal flip at Position(xpos=0.2)
show zhong normal c at right
with dissolve
$ renpy.pause (0.5)
Zh "Hello, I’m hoping you got everything you were looking for?"
Lo think flip "Yeah, I think so."
Zh "Let me check that out for you then."
play sound "fx/register.ogg"
show lorem normal flip with dissolve
$ renpy.pause (6.0)
stop sound fadeout 1.0
Zh "There you are."
Lo "Thank you."
stop music fadeout 2.0
$ renpy.pause (1.5)
scene town3 with dissolveslow
show lorem normal with dissolve 
play music "mx/feelings.ogg"
m "We made our way back outside, and once again, Lorem started leading me to the still unknown location."
scene forest1 
show lorem normal
with dissolveslow
m "But when we started heading away from the town and into the woods, I grew slightly uncertain."
c "Lorem, where are we actually going?"
Lo "Trust me, it’ll be much better as a surprise."
c "If you say so..."
$ renpy.pause (1.0)
stop music fadeout 3.0
scene black with dissolveslow
m "After a bit more walking, we headed into some denser foliage. Not enough to slow or stop us, but enough to obscure what could possibly be behind it."
m "Some light started to shine through to us soon enough though."
Lo "I think this is it..."

scene ryannbeachevening with dissolveslow
play music "mx/starlight.ogg"
$ renpy.pause (1.5)
show lorem think flip at left with easeinleft
Lo happy flip "Yes, it is!"
c "Woah..."
Lo "I know. It’s beautiful, right?"
if rnloremromance > 3:
    c "It looks like the perfect scene for a romantic date."
    Lo blush flip "That’s exactly what I thought too..."

else:
    c "It really is..."

$ renpy.pause (0.5)
show lorem normal flip with dissolve 
$ renpy.pause (0.3)
show lorem at center with move
m "We made our way to the center of the beach and started setting up for our picnic, first laying a blanket across the sand."
m "Lorem sat down on it and put the basket beside them."
if rnloremromance > 3:
    menu:
        "Sit beside Lorem.":
            play sound "fx/undress.ogg"
            m "I moved it out of the way slightly so we could sit together, and Lorem didn’t hesitate this time to start cuddling up to me."
            Lo normal blush flip "I still can’t get over how warm you are, especially with us being out here."
            c "Well, feel free to cuddle with me anytime you want."
            Lo "I’m definitely taking advantage of that."

        "Sit behind Lorem.":
            m "Instead of sitting down next to them, I walked around behind Lorem."
            Lo think flip "[player_name]? Where are you-{w=0.75}{nw}"
            play sound "fx/undress.ogg"
            $ renpy.pause (0.3)
            show lorem shy flip with dissolve
            m "I sat down with Lorem between my legs, and arms around their abdomen, pulling them into a warm hug."
            show lorem blush flip with dissolve
            m "Lorem shifted slightly to adjust their tail and wrap it around my leg again, and to fully fold their wings to properly fall back into my embrace."
            m "Being cautious of their horns and spiked wings, I slowly moved to rest my chin on Lorem's head."
            show lorem sleep blush flip with dissolve 
            $ renpy.pause (1.0)
            Lo "That feels amazing..."
            $ renpy.pause (2.0)

else:
    play sound "fx/undress.ogg"
    m "I sat on the other side of it so we could both reach."

show lorem normal flip with dissolve
$ renpy.pause (2.5)
m "For a while we just sat in silence, yet it wasn’t an awkward silence, it didn’t feel weird, we didn’t feel any pressure to talk. We just sat there, existing and enjoying each other's company, staring out to the sea."
$ renpy.pause (2.0)
c "So, I’m curious, how did you find out about this place?"
Lo think flip "Well, a few months ago I had to do a delivery to a fairly isolated farm south of here, my guess would be about 20 minutes worth of flying from here."
Lo normal flip "Anyway, I obviously got tired from flying for so long and was looking for a place to rest, and just barely spotted this beach."
Lo "I flew over and it was completely empty, no people, no trash, nothing at all."
Lo think flip "I think because of the amount of trees, bushes and other stuff you have to go through to get here, no one comes here. Me, you and Ipsum are the only ones who know."
c "So, we can pretty much have a private beach to ourselves whenever we want?"
Lo normal flip "In all the times I’ve been here I haven't seen anyone else, so most likely yes."
$ renpy.pause (2.0)
m "There was another moment of silence between us, but it didn’t last long as Lorem had gotten the picnic basket and took out some snacks for the both of us."
m "They weren't too bad, they were definitely different from previous human snacks, but I figured I’d get more used to them over time."
$ renpy.pause (1.0)
if rnloremromance > 3:
    Lo blush flip "I’ve... never really been in this kind of relationship before... so, I don't really know what kind of things I should be doing..."
    c "Lorem, again, you don't need to overthink this, just do what feels natural."
    Lo think flip " Alright, so how about..."
    m "Lorem got up from me, just to come back and give me a quick lick on the cheek, then moved back to their original position."
    Lo blush flip "How was that...?"
    c "Definitely unique, is licking common for dragons?"
    Lo think flip "Yeah it is, is it not for humans?"
    c "It’s not common, but it isn’t completely unheard of either."
    Lo "Would you prefer I didn’t do it then…?"
    c "Well, I don’t really mind it, so if you want to, then feel free."
    Lo normal flip "Alright."

else:
    c "So, how often do you come to this beach?"
    Lo normal flip "At least once every week or two. Like I said, I don’t think many people know about this beach, so it’s a good place to find some privacy."
    Lo "It’s also a great place to come to when I want to think, or destress, it's just so peaceful and tranquil here."
    c "I see what you mean, the sound of the waves, the view of the ocean and being surrounded by untouched nature. It’s perfect."
    Lo "I’m glad I was able to share it with you then."

$ renpy.pause (2.0)
scene ryannbeachnight
show lorem normal flip
with dissolveslow
m "Before we had even realised, the sun had set, revealing the breathtakingly beautiful night sky."
c "Woah... Lorem look."
Lo happy flip "Wow... That’s... I can’t find the words..."
c "So majestic... {w}So beautiful..." # Reference to Omori
Lo "Yeah..."
Lo think flip "You never usually see that back in the town."
c "Probably because there’s less light pollution out here."
Lo "Yeah, that would make sense."
$ renpy.pause (1.5)

if rnloremromance > 3:
    Lo blush flip "A-Actually there’s something else I brought..."
    m "Lorem moved away from me, and went over to the picnic basket again, but instead of snacks, they pulled out a candle."
    Lo "Since this is supposed to be our first proper date... I thought it might be nice to have this...?"
    c "Well, go ahead then."
    m "Lorem then went to the edge of the blanket and dug a small hole into the sand to put the candle in."
    c "Wait, how are we going to light it?"
    Lo normal flip "I have a fire breath weapon, remember?"
    c "Right, but couldn’t it be dangerous?"
    Lo "Like I said, it’s pretty small anyway, and I know how to control it, so I’m sure we’ll be fine."
    m "Two small amounts of liquid came out of Lorem’s mouth, and on making contact with the candle, it was lit."
    $ renpy.pause (0.5)
    Lo blush flip "So... um, do you like it...?"
    c "You’re so adorably precious."
    m "I leaned over to Lorem and gave them a quick kiss on the nose."
    play sound "fx/kiss.wav"
    show lorem shy flip with dissolve
    $ renpy.pause (1.5)
    Lo blush flip "I’ll take that as a yes..."
    $ renpy.pause (0.5)
    show lorem normal flip with dissolve 
    m "Lorem then proceeded to lie down on their back on the blanket, and I copied, so we could both get a better look at the night sky."

else:
    m "Lorem then laid down on their back on the blanket to get a better look at the night sky. I copied them, lying down too."

scene stars with dissolveslow 
if rnloremromance > 3:
    m "Staring at the stars, I moved my hand over to Lorem, and it seemed they had the same idea, our hands met, and we held each other's hands."
    m "Feeling the heat of the moment of being under the night sky and the soft candle light, I looked over to Lorem and gave them a kiss, they were caught off guard, yet didn’t hesitate to return it."
    $ renpy.pause (2.5)
    m "After a few seconds we parted, and went back to staring at the sky."

else:
    Lo "It’s so amazing..."
    c "It feels like you could just stare at it forever."
    Lo "Yeah..."
    c "It’s a shame most of those stars are probably already dead though."
    Lo "What do you mean?"
    c "Well, the light from those stars takes hundreds, or even thousands of years to get to us, so in that time the light is traveling, the star could have died."
    Lo "I never knew that..."
    Lo "It’s kind of amazing, in a way."
    c "How do you mean?"
    Lo "Well, the light has been traveling for hundreds of years, and out of everything it could shine on, it shines on just us."
    c "Huh, I guess you’re right."

$ renpy.pause (2.0)
Lo "..."
Lo "[player_name]?"
c "Yes?"
Lo "I wanted to thank you."
c "For what?"
Lo "Just… {w}for everything."
Lo "For being here right now, for accepting me for being a hermaphrodite, even for just hearing me out when we first met."
if rnloremromance > 3:
    Lo "Before I met you, when I thought about the future I mostly felt worried, about how people saw my game, would it turn out the way I envisioned it, how people would react if they found out about me being a hermaphrodite..."
    Lo "But with you, I feel... {w}hopeful, {w=0.75}and I’m actually looking forward to what will happen in the future, especially with you being a part of it..."
    c "Lorem..."
    $ renpy.pause (2.5)
    c "I’m looking forward to the future with you too."
    Lo "I can’t describe how grateful I am to hear you say that."
    m "Lorem surprised me with another lick on the cheek before cuddling into my side."
    $ renpy.pause (2.5)
    Lo "I love you [player_name]."
    c "I love you too Lorem."

else:
    Lo "You’ve changed my life, you’ve {i}saved{/i} my life, I wouldn’t be here if it wasn’t for you."
    Lo "I’ll never be able to repay you for all you’ve done for me..."
    c "Well, please feel free to try, I take cash, credit, real estate..."
    Lo "Haha..."
    c "Seriously though, you don’t owe me anything, your friendship and loyalty is enough."
    $ renpy.pause (2.0)
    Lo "[player_name], truly, thank you. I really couldn’t ask for a better friend."
    c "Neither could I Lorem."

$ renpy.pause (2.5)
scene black with dissolveslow
stop music fadeout 2.5
$ renpy.pause (4.5)

play sound "fx/system.wav"
if rnloremromance > 3:
    s "You got the romantic ending!"
else:
    s "You got the friendship ending!"

if ryannsecretscene == True:
    $ renpy.pause (4.5)
    jump ryann_lorem2_secret
else:
    s "Too bad there wasn't some kind of flower or daisy crown related scene in this mod..."
    s "Or... {w}is there?"
    $ renpy.pause (4.5)
    jump ryann_lorem2_credits


# Secret flower crown scene

label ryann_lorem2_secret:

$ save_name = (_("LI - Secret"))

play music "mx/serene.ogg"
play sound "fx/steps/rough_gravel.wav"
$ renpy.pause (2.0)
scene np3x
show ipsum normal flip at left
show lorem think at Position(xpos=0.8) 
with dissolveslow
$ renpy.pause (1.5)
Lo "Ipsum, can you tell us where you’re taking us now?"
c "Yeah, why haven’t you told us yet?"
Ip "Both of you have patience, you’ll find out soon."
Lo relieved "You said we’d find out soon before we left the apartment..."
Ip "Soon."
c "I guess unclear surprises are something you two have in common..."
$ renpy.pause (0.5)
scene forest1 
show ipsum normal flip at left
show lorem think at Position(xpos=0.8)
with dissolveslow
m "We started to make our way into a forest, and a sense of déjà vu came over me."
c "Surprises that take place in forests too apparently..."
Lo "Wait, but this isn't the right way to the beach..."
Ip happy flip "Because we’re not going to the beach."
Lo "Then where are we going?"
Ip normal "You’re about to find out."
$ renpy.pause (0.5)
hide ipsum with easeoutleft
m "Ipsum made a sharp turn off the trail and through some thick foliage. Lorem struggled, but managed to keep up with us."
scene black with dissolveslow
m "After we got through the trees, bushes and whatnot, we came out to a clearing on the other side."
scene ryannsecretforest with dissolve
show ipsum normal at left with easeinright
show ipsum normal flip with dissolve
show lorem normal at Position(xpos=0.8) with easeinright
$ renpy.pause (0.5)
Ip happy flip "Here we are."
c "And what exactly are we doing here?"
Ip normal flip "Look at the grass."
m "Me and Lorem looked at the grass like Ipsum instructed, and unsurprisingly, it looked just like tall grass."
Lo think "It’s just grass..."
Ip "Look closer."
m "Once again, me and Lorem looked at the grass, but closer this time, us crouching down to look more thoroughly through it."
m "After parting the top denser layer of grass, we discovered lots of daisies closer to the ground."
c "There’s lots of daisies in the grass."
Ip "That there is."
Ip happy flip "Now Lorem, if I remember correctly, you made a crown out of daisies before, correct?"
Lo relieved "You didn’t seriously bring us out here to make daisy crowns, did you?"
Ip normal flip "Well, what if I did?"
Lo "Well, I’m not doing that, not in front of [player_name]..."
c "Why not?"
Lo sad "It’s just... It’ll be really embarrassing..."
c "So you felt comfortable enough to tell me you were a hermaphrodite, but a daisy crown is where you draw the line?"
Ip "And it’s not like you’ll be the only one doing it, me and [player_name] will too."
$ renpy.pause (1.5)
show lorem relieved with dissolve
$ renpy.pause (0.5)
m "Lorem sighed."
Lo "Alright..."
c "Come on Lorem, try to lighten up, it’ll be fun."
Lo shy "Yeah, we might as well get started then..."
if ryann_adatp_played == True:
    c "Well, I know the basics of making flower crowns, but does Ipsum know?"
    Ip think flip " No, I do not."
    c "Well, I think it’s better if Lorem teaches you, given they're the master here and all."

else:
    c "We could, if I actually knew how to make a daisy crown..."
    Ip think flip "You never showed me how to either. So, it looks like you’ll have to teach us, with you being the master at this and all."
    
Lo normal "Alright… {w}So first, obviously you’ll need some daisies, and next, make sure they’re at least roughly the same length..."
m "After a tutorial from Lorem, me and Ipsum were slowly, but surely on our way to having flower crowns, albeit with Ipsum’s slightly less dexterous hands, I was getting there sooner."
m "We both did finish soon enough though."
m "Ipsum put his on first."
$ renpy.pause (0.5)
show ipsum happy fl flip with dissolve
$ renpy.pause (0.5)
Ip "So, how does it look?"
Lo happy "It looks so cute!"
Ip "But I bet not as cute as you’ll look."
show lorem shy with dissolve
c "I think it looks quite charming."
Ip normal fl flip "Why thank you."
Ip sad fl flip "It is a bit uncomfortable with my fur though..."
c "I guess it’s my turn."
show ipsum normal fl flip with dissolve 
m "Being careful not to damage it, I put the flower crown on  my head."
$ renpy.pause (1.5)
c "Well, how is it?"
Ip happy fl flip "You know, it suits you a lot better than I thought it would."
Lo happy "Yeah, it looks lovely on you!"
Ip normal fl flip "It must be uncomfortable for your fur too, I imagine."
c "Not really, I guess it’s because humans are more used to having things over our hair."
Ip sad fl flip "Right, I’m still not used to calling it hair."
c "Don’t worry about it, I’m not used to saying fur either."
$ renpy.pause (0.5)
show ipsum normal fl flip with dissolve
$ renpy.pause (1.5)
show lorem shy with dissolve
$ renpy.pause (0.5)
m "Me and Ipsum both now had our eyes on Lorem."
Ip happy fl flip "And now, for the big reveal..."
c "The moment we’ve all been waiting for..."
Lo "Okay, okay, I’ll put it on now..."
m "After a few seconds of apprehension, Lorem slowly put the flower crown on."
$ renpy.pause (1.5)
show lorem shy fl with dissolveslow
$ renpy.pause (0.5)
Lo normal fl "Well... how is it?"
Ip normal fl flip "..."
c "..."
Lo shy fl "Uh... Is it that bad...?"
Ip happy fl flip "Words can’t describe how absolutely adorable you are right now."
c "It should be illegal for something to be that cute."
Lo relieved fl "You two better not tell anyone about this..."
c "Can we agree that Lorem is never allowed to take off that flower crown?"
Lo shy fl "What?"
Ip "Oh, we can absolutely agree on that."
Lo "But I don't agree!"
Ip normal fl flip "Sorry Lorem, but it seems like you’re outvoted."
c "Yep, it’s settled then, you’re never taking it off."
Lo think fl "I’m going to get back at you both for this."
c "Sorry, we can’t hear you over how much of a cutie you are."
Lo "Just you both wait..."
Ip "You can’t exactly be menacing while wearing a daisy crown Lorem."
m "Lorem let out a long sigh."
Lo relieved fl "You two will never let me forget this, will you?"
c "Absolutely not."
Ip happy fl flip "Oh, what I’d give for a camera right now..."

$ renpy.pause (2.0)
scene black with dissolveslow
stop music fadeout 2.0
$ renpy.pause (5.0)
jump ryann_lorem2_credits

