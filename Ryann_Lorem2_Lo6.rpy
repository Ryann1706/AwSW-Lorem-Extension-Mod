
label ryann_lorem2_lorem6:

$ renpy.pause (3.0)
play music "mx/basicguitar.ogg"
scene o4 with dissolveslow
m "I woke up looking at the ceiling I was now well-acquainted with, but without the normal nightmares I usually got."
m "I got up and did my daily morning routine as best I could, given the lack of certain things that dragons didn’t need, but humans did."
m "With the threat of Reza eliminated, and the other me going through the portal, I had the chance to reflect on me staying in the dragon's world permanently."
m "There were pros and cons, and I knew I’d have to deal with some sooner then I liked, but I tried to focus on the positive things, like getting to stay with Lorem."
m "After the confrontation with Reza, he was told to take it easy, and was let off work, but with Ipsum still working I decided to visit so he wouldn’t get lonely."
m "But just as I was about to leave..."
play sound "fx/door/doorbell.wav"
$ renpy.pause (2.0)
m "...I heard someone at the door."
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)

if remydead == False:
    if remystatus == "good" or remystatus == "neutral":
        $ renpy.pause (0.5)
        show remy normal with dissolve
        Ry "Good morning [player_name]."
        c "Oh, hey Remy, how are you doing?"
        Ry "I'm doing better than usual actually, but anyway I'm here to deliver this letter."
        c "Who's it from?"
        Ry "It’s from Emera, she said she wanted to talk to you about something, there's more about it in the letter."
        c "Alright, well it was nice seeing you."
        Ry "It was nice seeing you too, I have to go now, so see you later."
        c "See ya."
        hide remy with dissolve
        jump ryann_lorem2_lorem6_letter

    elif remystatus == "bad" or remystatus == "abandoned":
        $ renpy.pause (0.5)
        show remy look with dissolve
        Ry "I was told to give this to you, here."
        m "He shoved a letter in my direction."
        c "Uh, thanks."
        hide remy with dissolve
        m "He left without saying anything, leaving me standing in the doorway."
        jump ryann_lorem2_lorem6_letter

    else:
        $ renpy.pause (0.5)
        show remy normal with dissolve
        Ry "Hello [player_name], I was asked to deliver this to you."
        c "Hey Remy, who is this from?"
        Ry "It's from Emera, she said she wanted to talk to you about something, there's more about it in the letter."
        c "Alright, thanks."
        Ry "It’s no problem, goodbye."
        c "Bye."
        hide remy with dissolve
        jump ryann_lorem2_lorem6_letter

else:
    $ renpy.pause (0.5)
    show emera normal with dissolve
    Em "Good day, [player_name]."
    c "Oh, good morning, Emera."
    Em "I'm sorry but I'm quite busy today so I can't stay and chat but here’s a letter for you, it's about something we must discuss."
    c "If you're busy, how come you're delivering it?"
    Em "No one else was available to do it, I'm sorry but I must leave at once."
    c "Goodbye then."
    hide emera with dissolve
    jump ryann_lorem2_lorem6_letter


label ryann_lorem2_lorem6_letter:

m "I went back inside to read the letter I was given, and it said the following:"
$ renpy.pause (0.5)
play sound "fx/envelope.wav"
nvl clear
window show
n "Dear [player_name],"
n "I hope you are in good health and condition given the circumstances you were under in recent times."
n "I am writing to inform you that we must discuss matters related to the portal, your ambassador status and other important details."
n "Please come to see me at my office at your earliest convenience."
n "Minister of Culture and Arts,"
n "Emera."
window hide
nvl clear
$ renpy.pause (0.5)
c "(Lovely, I knew this was inevitable but I didn’t think It'd be so soon.)"
c "(I don’t know how long this will take, and I don’t want to keep Lorem waiting...)"
c "(I guess tomorrow will have to do.)"
play sound "fx/door/door_close.ogg"
scene black with dissolveslow
stop music fadeout 1.5
$ renpy.pause (1.0)
play sound "fx/steps/clean.wav"
$ renpy.pause (1.7)

play music "mx/snowflake.ogg"
scene loremapt with dissolveslow
$ renpy.pause (1.0)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)
show lorem happy flip with dissolve
Lo "Hey [player_name]!"
c "Hey Lorem, how are you doing?"
Lo think flip "Well, I'm a bit sore, but more confused than anything."
Lo "All I can remember is Maverick getting shot, and then I charged at Reza, then... I woke up in a hospital bed."
Lo normal flip "But you’re here, so I'm assuming it went at least well enough."
c "It did, but I have a lot to explain so you should get comfortable."
Lo "Alright."
play sound "fx/door/door_close.ogg"
$ renpy.pause (1.0)
play sound "fx/undress.ogg" # (Its the sound of them sitting on the couch I swear)
m "We sat down on the couch and I began to explain."
c "Alright so, what happened was, you were knocked out, I threw Ipsum’s Ixomen Sphere at Reza, then took his gun and shot him and you were taken to the hospital after that."
Lo think flip"Okay, that makes sense, but what was Reza talking about? He said the generator was from our {i}time{/i}, what did he mean by that?"
c "This might sound hard to believe, but... The human and dragon's world aren't separated by space, {w}they’re separated by time."
Lo "Wait... You’re saying the portal is actually a time machine?"
c "Well, basically yeah, but there's more."
c "The coordinates to the human world are... Gone, so I’ll be staying here permanently."
Lo sad flip "Oh... [player_name] I’m so sorry to hear that, but what do you mean they’re gone, what happened?"
Lo "Actually, you don’t have to talk about it if you don’t want to... It must still be pretty painful..."
c "It’s okay Lorem, but there's one last thing, have you heard anything about a comet lately?"
Lo think flip "Ipsum offhandedly mentioned it at some point, but with everything else you’ve said I don’t think it's good news."
c "Well, yes and no, the important part is that us stopping Reza from escaping through the portal with the generator saved your entire species from extinction."
Lo sad flip "I don’t follow, but I'm not sure I want to think about what would have happened if we didn’t stop him, if us stopping him saved dragon kind."
Lo "..."
c "Maybe we should talk about something less depressing, considering I came over so we could have a good time."
Lo "Yeah..."
Lo think flip "..."
Lo "Actually, I still owe you dinner from you letting me draw you."
c "It’s a bit early for dinner."
Lo normal flip "I can make you lunch then, is there anything specific you want?"
c "As long as it's not Pantoli’s Pizza, I'll be happy with it."
Lo "Ha! Good one, {w}you can wait here I shouldn’t be that long."
show lorem normal with dissolve
$ renpy.pause (0.2)
hide lorem with easeoutleft
m "Lorem strolled into the kitchen leaving me in the living room."
c "(I guess I could look around and see what kind of stuff Lorem and Ipsum have.)"
jump ryann_lorem2_lorem6_aptsearch


label ryann_lorem2_lorem6_aptsearch:

if ryannlookatthings == 4:
    $ renpy.pause (0.5)
    c "(I think I've looked at enough.)"
    jump ryann_lorem2_lorem6_loremreturn
else:
    pass

menu:
    "Look at shelf" if ryannlookatshelf < 2:
        m "I looked at the bookshelf and there was mostly only video games and books."
        menu:
            "Look at video games." if not ryannlookgames:
                $ ryannlookatthings += 1
                $ ryannlookgames = True
                $ ryannlookatshelf += 1
                m "I didn’t recognize anything there but a few things looked vaguely familiar."
                m "There was a game which, according to the back of the box, was about two carpenter brothers called Marco and Louis, who had to go on an adventure to save Princess Apricot."
                c "(Huh... This definitely doesn't remind me of anything from back home.)"
                jump ryann_lorem2_lorem6_aptsearch

            "Look at books." if not ryannlookbooks:
                $ ryannlookatthings += 1
                $ ryannlookbooks = True
                $ ryannlookatshelf +=1
                m "The shelf for books was split into two parts, on one side was books about plant care, design, coding and an out of place novel called “The Exteriors”."
                m "On the other side were books about biology and physics but there were also magazines, one about medicinal and flavored teas, and another about a dragon tech company I obviously didn’t recognize."
                c "(Wow, I wonder which side belongs to who. {w}Don’t know why I thought I find anything interesting on a shelf full of books.)"
                jump ryann_lorem2_lorem6_aptsearch
            
    "Look at the plant" if not ryannlookplant:
        $ ryannlookatthings += 1
        $ ryannlookplant = True
        m "I didn’t recognize the plant, but it did seem to be thriving."
        c "(Ipsum wasn’t joking when he said Lorem loved plants.)"
        jump ryann_lorem2_lorem6_aptsearch

    "Look at the TV" if not ryannlookTV:
        $ ryannlookatthings += 1
        $ ryannlookTV = True
        m "The TV looked exactly like the ones back home, I looked closer and saw cables running from it and into the back of the stand it was on."
        m "I looked inside the cabinet it was on and saw what I assumed was a DVD player and a console, with its controllers lying next to it."
        c "(I wonder how different movies and video game are between humans and dragons?)"
        jump ryann_lorem2_lorem6_aptsearch


    "Wait for Lorem":
        if ryannlookatthings == 0:
            m "I decided to respect Lorem and Ipsum's privacy and just sat down and waited for Lorem instead."
            jump ryann_lorem2_lorem6_loremreturn
        else:
            m "I sat back down and waited for Lorem."
            jump ryann_lorem2_lorem6_loremreturn
    

label ryann_lorem2_lorem6_loremreturn:

m "After waiting for a bit Lorem came back out from the kitchen carrying two plates with some appetizing sandwiches."
show lorem normal flip with easeinleft
$ renpy.pause (0.5)
Lo "I know it's not amazing but I didn’t want to keep you waiting too long."
m "He set one down in front of me and sat next to me with the other."
m "I bit into the sandwich, {w}and it was delicious! {w}The combination of the unknown meat, vegetables and uniquely flavored bread was an entirely different experience, but not unwelcome."
c "Wow Lorem, this is amazing!"
Lo shy flip "O-oh, thanks [player_name], it's really nothing special..."
Lo "..."
c "(Maybe I should break this awkward silence?)"



label ryann_lorem2_lorem6_questions:

if ryannlo6ask == 3:
    jump ryann_lorem2_lorem6_ipsum
else:
    pass

menu:
    "Ask about Ipsum." if not ryannaskipsum:
        c "So, where's Ipsum?"
        Lo normal flip "He’s at work in the production facility, he should be home in a few hours if you’re looking for him."
        c "Nah, I was just curious since he wasn’t here."
        Lo "Ah, alright."
        $ ryannlo6ask += 1
        $ ryannaskipsum = True
        jump ryann_lorem2_lorem6_questions

    "Ask about books." if ryannlookbooks and  not ryannaskbooks:
        c "I was looking at the book shelf there, and I saw a book called The Exteriors, what's it about?"
        Lo think flip "Well, I don’t want to spoil it in case you want to read it, but it's about two rival teenage gangs called the Oilers and the Glovs."
        Lo normal flip "I thought it was really good, but it doesn't have an entirely happy ending."
        c "Well, nothing gold can stay Ponyboy."
        Lo think flip "What?"
        c "It was a reference to... {w}Never mind."
        $ ryannlo6ask += 1
        $ ryannaskbooks = True
        jump ryann_lorem2_lorem6_questions
        # This whole section is a reference to a book called “The Outsiders”, the two gangs in it are called the Greasers and the Socs
        # I thought it was good, so I’d recommend it 
    
    "Ask about games." if not ryannaskgames:
        if ryannlookgames == True:
            c "I saw a game over on the shelf, Super Marco Bros, what's it about?"
            Lo happy flip "Oh, that's one of my favorites! it’s a 2D side scroller where you have to jump to get power ups and ovoid enemy's and obstacles."
            Lo "There's lots of different worlds and level in it too! it's fairly old, but it’s a classic, do you have anything similar in your world?"
            c "It does sound familiar but I can't seem to quite place it..."
            $ ryannlo6ask += 1
            $ ryannaskgames = True
            jump ryann_lorem2_lorem6_questions
        
        else:
            c "I know that you're making your own game, but what kind of games do play normally?"
            Lo normal flip "I play lots of different types, mostly adventure games, but there's this one game I love called Super Marco Bros, I highly recommend you check it out if can."
            c "(Huh, that definitely doesn't sound familiar at all.)"
            $ ryannlo6ask += 1
            $ ryannaskgames = True
            jump ryann_lorem2_lorem6_questions
        
    "Ask about plants" if not ryannaskplant:
        if ryannlookplant == True:
            c "I looked at that plant and seems to be doing really well, Ipsum wasn’t joking when he said you loved plants."
            Lo normal flip "Well, it's not just plants, it’s botany I love."
            c "He also said you made a daisy crown, I'd love to see that, I bet you’d look so cute."
            Lo shy flip "Uhm... I-I..."
            m "He looked away blushing and avoiding eye contact, clearly embarrassed about me bringing it up."
            $ ryannlo6ask += 1
            $ ryannaskplant = True
            $ rnloremromance += 1
            jump ryann_lorem2_lorem6_questions

        else:
            c "Ipsum mentioned you loved plants, so how true is that?"
            Lo normal flip "Well, it's not just plants, it’s botany I love."
            Lo "But yeah, I do love plants, I'm actually considering getting a few more, but Ipsum says I can have more plants when he can have more space for his tea."
            Lo relieved flip "But that’ll never happen, he already has so much, seriously there's definitely over twelve different kinds and I can't taste any difference."
            c "Did Ipsum give you permission to drink his tea?"
            Lo normal flip "What he doesn’t know can't hurt him."
            $ ryannlo6ask += 1
            $ ryannaskplant = True
            jump ryann_lorem2_lorem6_questions

    "Ask about TV." if not ryannaskTV:
        if ryannlookTV == True:
            c "I saw what looked like a console and a DVD player, but do you us the TV for anything else?"
            Lo normal flip "Well, there a subscription service you can pay for to watch shows, but most of them aren’t worth watching, except a show called humans which is apparently pretty good, but not accurate to actual humans."
            Lo "Also, it's not DVD, its DDVD."
            c "What does the extra D stand for?"
            Lo "The whole thing stands for, digital dragon video disc."
            c "(Do they have to clarify its for, or made by dragons?)"
            $ ryannlo6ask += 1
            $ ryannaskTV = True
            jump ryann_lorem2_lorem6_questions

        else:
            c "So, what do you use that TV for? I don’t have one in my apartment."
            Lo normal flip "We really only use it for video games or watching DDVDs."
            c "DDVD?"
            Lo "It stands for digital dragon video disc."
            c "For humans it's just DVD, not... {w}DHVD?"
            Lo think flip "Huh, I thought it would be."
            $ ryannlo6ask += 1
            $ ryannaskTV = True
            jump ryann_lorem2_lorem6_questions

    "Foucus on eating.":
        if ryannlo6ask == 0:
            m "I decided to focus on eating the delicious sandwich in front of me instead of talking."
            jump ryann_lorem2_lorem6_ipsum

        else:
            m "I decided to focus on eating the delicious sandwich in front of me instead of talking anymore."
            jump ryann_lorem2_lorem6_ipsum


label ryann_lorem2_lorem6_ipsum:


m "We were interrupted by Ipsum coming through the front door."
play sound "fx/door/door_open.wav"
$ renpy.pause (0.5)
show lorem normal flip with dissolve
show lorem at left with move
show ipsum normal at right with easeinright
Lo "Oh, Ipsum I thought you were supposed to be in work?"
if annadead == True:
    Ip "I am, but with what happened to Anna the shift schedules are still a bit messy, so I was sent home early. "
else:
    Ip "I am, but with what happened to Damion the shift schedules are still a bit messy, so I was sent home early." 

Ip think "And, once again I didn’t know [player_name] would be here today."
c "I assumed you would’ve been in work, and I didn't want Lorem to get lonely being here by himself."
Ip happy "Well, isn't that very considerate."
play sound "fx/undress.ogg" # ( Again I swear its the sound of sitting on the couch )
m "Ipsum sat down on the other end of the couch, as he did Lorem got up and picked up the two now empty plates."
play sound "fx/glasses.wav"
Lo "I’ll be back in a few minutes."
show lorem normal with dissolve
$ renpy.pause (0.2)
hide lorem with easeoutleft
$ renpy.pause (1.0)
show ipsum think with dissolve
$ renpy.pause (0.5)
m "I zoned out for a bit, thinking about what would happen to me and my ambassador status with the portal now completely non-functional, but I snapped out of it when I noticed Ipsum staring at me."
c "Uh, Ipsum?"
Ip normal "Oh, sorry about that, I'm just still very curious about your biology, given you being an entirely different species."
Ip think "Hmm, if you wouldn't mind, maybe I could take some samples to examine and run some tests on you in the production facility?"
if annadead == True:
    Ip sad "And... {w}With what happened to Anna... She won't be a problem."
    Ip normal "Its only if you want to do them, if you don’t, I'd understand."
else:
    Ip sad "Ah, right, Anna said you're off limits to only her..."
    if rndidannatest == True:
        c "Anna already did some tests on me, but I never agreed for {i}only{/i} her to do tests on me."
        Ip think "Really...? Maybe we could do it then, if you don’t mind, of course."

    elif rncancelannatest == True:
        c "Well, I agreed to Anna doing tests on me we had to cancel because something happened to her lab."
        Ip think "I heard about that happening, but I didn’t know it was Anna’s lab."
        Ip "If you canceled, maybe we could do it then, if you don’t mind, of course."

    elif rnagreedannatest == True and rncancelannatest == False and rndidannatest == False:
        c "Well, I did agree to do tests for Anna, but I haven't done them."
        Ip "That could be a problem then."
        c "I agreed she could do tests on me, but why can't you too? If I gave you my permission, what can she do about it?"
        Ip think "Yeah, that could work... {w}What's the worst that could happen? Maybe we could do it then, if you don’t mind, of course."

    else:
        if blood == True:
            c "I never agreed for Anna to do any tests on me, she just took some of my blood and gave me her number and said we could discus biology."
        else:
            c "I never agreed for Anna to do any tests on me, she just gave me her number and said we could discus biology."
        
        Ip think "Really...? Maybe we could do it then, if you don’t mind, of course."

c "Sure, I wouldn’t mind, it might be a few days before we can though."
Ip happy "Glad to hear that, just let me know when you’re available."
$ renpy.pause (0.7)
show lorem normal flip at left with easeinleft
Lo "Hey, what were you two talking about while I was gone?"
Ip normal "Oh, just science, physics mostly."
Lo relieved flip "[player_name] you know what happened last time, don’t get him started again."
Ip "You’re just saying that because you know you won't be able to keep up with us."
Lo "Hmph."
Lo think flip " Actually [player_name], how much do you know about physics?"
menu:
    "Lots":
        c "I know a lot about physics."
        Ip "Really? You won't mind if I asked you a question if you're such a genius when it comes to physics then, right?"
        c "Go ahead."
        Ip "Alright, ahem, what is a superconductor?"
        menu:
            # The wrong ones are fake but they sound sciencey enough to work
            "A super charged electron using gamma radiation.":
                $ renpy.pause (0.3)
                Ip happy "Heh, it's funny when someone who doesn't know physics tries to talk about physics."

            "A conductive material with little to no resistance.":
                $ renpy.pause (0.3)
                Ip think "Oh, wow. I didn’t expect you to know that, I'm impressed."

            "An insulated lithium-ion battery connected to a copper aluminide relay.": 
                $ renpy.pause (0.3)
                Ip happy "Heh, it's funny when someone who doesn't know physics tries to talk about physics."

            "I have no clue what any of that means.":
                $ renpy.pause (0.3)
                Ip happy "Heh, it's funny when someone who doesn't know physics tries to talk about physics."


    "A decent bit":
        c "I know a bit, but not lots."
        Ip "Well, would you mind humoring me and letting me ask a question?"
        c "Alright."
        Ip "Okay, what’s a tensegrity structure?"
        menu:
            "Parts in compression separated by parts in tension.":
                Ip think "Huh, not bad, not many people know that."

            "Parts in tension separated by parts in compression.":
                Ip normal "You still have a bit to go to be a physicist apparently."

            "Parts in tension that are in equilibrium.":
                Ip normal "You still have a bit to go to be a physicist apparently."

            "I don’t know.":
                Ip normal "You still have a bit to go to be a physicist apparently."


    "Barely anything":
        c "I barely know anything about physics."
        Lo normal flip "See? I'm not the only one who doesn't know physics."
        Ip "At least your honest, you really should consider learning about it though, it's really interesting."
        c "I’ll stick to biology for now thanks."
    
Lo normal flip "Anyway, enough science talk, [player_name] got enough of that last time, let's do something fun instead."
c "What did you have in mind?"
Lo think flip "I'm not actually sure..."
c "I have an idea of a human game we could play."
Lo normal flip "Oooh, what is it?"
c "It's called would you rather, the idea of it is you give someone two hypothetical situations, and they have to choose which of the two they’d rather."
Lo "Can they be good or bad?"
c "Yeah, but you’d obviously want to choose two good or two bad, not one of each because whoever would choose the good one."
c "I can start so you two can properly understand."
c "So..."

label ryann_lorem2_lorem6_wyr:

if rnwyrasked == 0:
    pass
elif rnwyrasked == 1:
    c "So, do both of you understand now?"
    Ip think "I think I get it."
    Ip "So, [player_name], {w}if you had the opportunity would you rather change into a dragon or stay as a human?"
    c "Yeah, that’s the idea exactly."
    c "Now, as for the question..."
    menu:
        "Human":
            c "I’d say how I am now; I think I’d miss my hands too much."
            c "Also, suddenly having claws, a tail and other things would be too huge a change, considering I've never had them at all up to this point."
            Ip normal "You do bring up some fair points."

        "Dragon":
            c "Do I get to keep things like my mind and personality, it's just my body changing?"
            Ip normal "Yep."
            c "Oh, I’d definitely prefer being a dragon then, you can do so many more cool things than humans can."
            Ip happy "Now the real question is, what species of dragon?"
            c "I don’t know many dragon species, so I’ll pass on that question for now."

    c "So, if we’re going anti-clockwise its Lorem’s turn now."
    Lo think flip "Alright, so..."
    Lo normal flip "Ipsum, would you rather, never own an Ixomen Sphere or give up on your tea collection?"
    Ip sad "That’s just unfair, how could I choose between those two?"
    c "Sorry, but that’s how the game goes."
    Ip normal "I’d have to choose my Ixomen Sphere though."
    c "I have to admit, it is pretty useful."
    Ip happy "Exactly."

        
elif rnwyrasked == 2:

    Ip think "So, Lorem."
    Ip "Would you rather, never play video games or take care of plants?"
    Lo relieved flip "Now that’s just cruel."
    Ip normal "So, you can ask me that kind of question but I can't?"
    Lo sad flip"I meant because I'm not giving up on my game, so the poor plants will just die."
    Ip think "Oh, I should have clarified your game wasn’t included."
    Lo normal flip "I’d still choose games regardless."
    Lo "Anyway, [player_name]."
    Lo think flip "Would you rather eat ice cream or mac & cheese?"
    menu:
        "Ice cream":
            c "I’d have to go with ice cream."
            Lo normal flip "But what flavor?"
            c "I guess that depends on what flavors are available."
            c "Speaking of availability I've noticed a lack of certain flavors that were in the human world."
            c "Well, its most of them but, mainly strawberry."
            Lo think flip "When did you see what flavors we had?"
            c "I did have to buy food at some point while I’ve been here."
            Lo relieved flip "Right, duh."
            show lorem normal flip with dissolve

        "Mac & Cheese":
            c "I think I’d choose mac & cheese."
            c "But not the kind you’d get from a box, I mean the homemade kind."
            c "But nearly every time I make it, it's always a bit burnt, the time when its perfect to take out of the oven is far too short."
            Ip think "I've never had the homemade kind."
            c "Well, you’re missing out then."


else:
    jump ryann_lorem2_lorem6_afterwyr


menu:
    "Lorem":
        c "Lorem..."
        menu:
            "Live in the world of your favorite book or game?" if not rnwyraskedlo1:
                $ rnwyraskedlo1 = True
                $ rnwyrasked += 1
                c "Would you rather, live in the world of your favorite book or favorite video game?"
                Lo think flip "Hmm, probably my favorite game, my favorite book has a decent bit of violence, so I’ll avoid that."
                Ip happy "I bet you favorite game is about farming."
                Lo relieved flip "Ha ha..."
                show lorem normal flip with dissolve
                jump ryann_lorem2_lorem6_wyr

            "Trade your wings for strength and height or stay the same?" if not rnwyraskedlo2:
                $ rnwyraskedlo2 = True
                $ rnwyrasked += 1
                c "Would you rather, trade you wings for strength and height or stay how you are now?"
                Lo think flip "Well, height and strength are tempting, but I think I’d missing flying too much."
                Lo normal flip "Also, I wouldn’t have anything to rub in Ipsum’s face."
                Ip think "We’ll see about that."
                Lo happy flip "Keep up that attitude and I'll fly away with your glasses and hide them."
                jump ryann_lorem2_lorem6_wyr

            "Be blind or deaf?" if not rnwyraskedlo3:
                $ rnwyraskedlo3 = True
                $ rnwyrasked += 1
                c "Would you rather, be blind or deaf for the rest of your life?"
                Lo think flip "Oh, that’s a bit tough..."
                Lo "..."
                Lo "I couldn’t work on my game if I was blind so I'll pick deaf."
                jump ryann_lorem2_lorem6_wyr

    "Ipsum":
        c "Ipsum..."
        menu:
            "Live in the future or past?" if not rnwyraskedip1:
                $ rnwyraskedip1 = True
                $ rnwyrasked += 1
                c "Would you rather live in the future or past?"
                Ip happy "The future definitely, I love to see the advancements in technology and science."
                Lo normal flip "You really just want an excuse to get another Ixomen Sphere."
                jump ryann_lorem2_lorem6_wyr

            "Have no hair, or be completely covered in hair?" if not rnwyraskedip2:
                $ rnwyraskedip2 = True
                $ rnwyrasked += 1
                c "Would you rather lose the hair you currently have or be completely covered in hair?"
                Ip "There actually are dragons that are completely coved in fur, they’re just less common."
                Ip think "I think that could be interesting to have more fur like that though."
                Lo happy flip "And you’d give way better hugs!"
                c "It would be a pain to wash all that fur though, trust me."
                jump ryann_lorem2_lorem6_wyr

            "Know how or when you’ll die?" if not rnwyraskedip3:
                $ rnwyraskedip3 = True
                $ rnwyrasked += 1
                c "Would you rather, know how or when you’ll die?"
                Ip sad "Ah, that’s tough..."
                Ip think "Knowing when you die is bound to cause existential dread, so I’d choose how."
                Lo think flip "Wow, I didn’t expect such a deep answer."
                jump ryann_lorem2_lorem6_wyr



label ryann_lorem2_lorem6_afterwyr:

$ renpy.pause (0.5)
Ip happy "You know, I was skeptical at first but this was a lot more fun than I thought."
Lo happy flip "Yeah, it really was, you have to tell us more human games like this!"
c "Alright, but only if you can tell me about similar dragon games."
Lo normal flip "Maybe we could alternate which we do?"
c "Sounds like a deal."
$ renpy.pause (0.5)
show ipsum think with dissolve
$ renpy.pause (0.5)
Ip "Alright, how about one last question."
Ip "[player_name], if you had to, would you rather..."
Ip "Kiss me, {w}or Lorem?"
Lo shy flip "Ipsum!"
c "I'm starting to think you have ulterior motives here."
Ip happy "I don't, I just thought it would be funny to see Lorem flustered from me asking that."
$ renpy.pause (1.5)
c "If I did have to choose though..."
menu:
    "Lorem":
        $ rnloremromance += 2
        c "I'd choose Lorem."
        Ip "Really now?"
        show lorem shy with dissolve
        $ renpy.pause (1.5)
        c "Come on Lorem, we're just teasing you."
        Lo shy flip "..."
        Ip "Heh, I might have gone a bit overboard this time."
        Lo "Just a bit?"
        $ renpy.pause (0.5)
        Ip normal "Well, on that note, I have to go, my lab awaits me."

    "Ipsum":
        c "I'd choose Ipsum."
        Ip "Really now, is there any specific reason?"
        c "I wanted to see that smug grin dissapear from your face when your plan backfired."
        c "Unless, {w}this {i}is{/i} what you wanted to happen?"
        Lo think flip "[player_name], what do you mean?"
        c "Well, first Ipsum wondered what I looked like naked, now he wants to know if I'll kiss him?"
        c "You really do have ulterior motives, dont you?"
        Ip sad "N-no, thats not what I meant at all!"
        Lo normal flip "{i}Sure{/i}, it wasnt."
        $ renpy.pause (1.0)
        show ipsum normal with dissolve
        Ip "Ahem, well I have to go do stuff in my lab."
        c "Of course you do."


Lo relieved flip "Don’t explode anything while [player_name] is here."
Ip happy "But where's the fun in that?"
c "That’s not concerning at all."
Lo "Don’t worry about him, he joking... {w}Mostly..."
$ renpy.pause (0.5)
hide ipsum with easeoutleft
$ renpy.pause (0.5)
show lorem at center with move
show lorem normal with dissolve
Lo normal "And once again, there he goes, off to {i}hopefully{/i} not blow up the apartment."
$ renpy.pause (1.0)
Lo think "Wait, did you bring Ipsum’s Ixomen Sphere?"
c "Ah, I had a feeling I forgot something, I can bring it at some other point, he’s survived without it this long, he can wait a few more days."
Lo normal "Heh, yeah."
$ renpy.pause (1.0)
c "I know I asked before when I invited you over for dinner but, how's your game going now?"
Lo think "..."
Lo "Well, ever since that talk you gave me, I've been feeling a lot more secure in what I'm doing."
Lo "I'm doing the best I can for myself, and I'm not catering entirely to others so I don’t lose myself."
Lo "I know that now, but I also still need help, I can't do this on my own."
c "You know you can always count on me and Ipsum to be there for you."
Lo normal "Yeah, I know and I really do appreciate that, but I need to put myself out there and be better."
Lo think "You and Ipsum can't be the only people who accept me for me, right?"
c "Of course not, anyone who doesn't accept you is the one losing out, not you."
$ renpy.pause (1.0)
Lo "Really...?"
c "Yeah, you’re an astounding person, anyone who says otherwise is an immature bigot who should be ignored."
c "But remember, you'll have my support no matter what."
$ renpy.pause (0.5)
Lo relieved "Thank you, I know I've said it before, but that means a lot."
m "Lorem walked up to me and hugged me, but because of his height he just rested his head against my upper abdomen, I still returned the hug regardless."
$ renpy.pause (2.5)
m "After a good few seconds Lorem let go and back off a bit."
c "It's gotten fairly late and I might be pretty busy tomorrow, so I’ll see you later, okay?"
Lo normal "Alright, see you soon!"

if rnloremromance > 0:
    menu:
        "Kiss them on the cheek.":
            $ rnloremromance += 3
            m "Before I left, I bent down next to the little dragons face and..."
            play sound "fx/kiss.wav"
            show lorem shy with dissolve
            $ renpy.pause (0.7)
            c "See ya."
            Lo "[player_name], I-"
            m "Before Lorem could continue I had alredy started leaving."

        "Do nothing.":
            pass

else:
    pass

play sound "fx/door/door_open.wav"
$ renpy.pause (1.5)
play sound "fx/door/door_close.ogg"

hide lorem with dissolve
scene black with dissolveslow
stop music fadeout 2.0
$ renpy.pause (3.0)

jump Ryann_Lorem2_Emera_Mav

