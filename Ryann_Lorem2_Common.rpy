
# This file is for variables and defining stuff, so kinda just ignore this one.


define Rnn = Character(_("Ryan"), color="#008000")

# For extra backgrounds
image ryannfacilitylab = "bg/ryannfacilitylab.jpg"
image ryannkitchen = "bg/ryannkitchen.jpg"
image ryannundergroundlab = "bg/ryannundergroundlab.jpg"
image ryannbeachevening = "bg/ryannbeachevening.jpg"
image ryannbeachnight = "bg/ryannbeachnight.jpg"
image ryannsecretforest = "bg/ryannsecretforest.jpg"


# For Lorem's extra sprites
image lorem blush = "cr/lorem_blush.png"
image lorem blush flip = im.Flip("cr/lorem_blush.png", horizontal=True)
image lorem normal blush = "cr/lorem_normal_blush.png"
image lorem normal blush flip = im.Flip("cr/lorem_normal_blush.png", horizontal=True)
image lorem scared = "cr/lorem_scared.png"
image lorem scared flip = im.Flip("cr/lorem_scared.png", horizontal=True)
image lorem sleep = "cr/lorem_sleep.png"
image lorem sleep flip = im.Flip("cr/lorem_sleep.png", horizontal=True)
image lorem sleep blush = "cr/lorem_sleep_blush.png"
image lorem sleep blush flip = im.Flip("cr/lorem_sleep_blush.png", horizontal=True)

# For Lorem and Ipsum's flower crown sprites, I'm definitely not using all of these but I might as well define them 
image lorem normal fl = "cr/lorem_normal_fl.png"
image lorem normal fl flip = im.Flip("cr/lorem__normal_fl.png", horizontal=True)
image lorem happy fl = "cr/lorem_happy_fl.png"
image lorem happy fl flip = im.Flip("cr/cr/lorem_happy_fl.png", horizontal=True)
image lorem relieved fl = "cr/lorem_relieved_fl.png"
image lorem relieved fl flip = im.Flip("cr/lorem_relieved_fl.png", horizontal=True)
image lorem sad fl = "cr/lorem_sad_fl.png"
image lorem sad fl flip = im.Flip("cr/lorem_sad_fl.png", horizontal=True)
image lorem shy fl = "cr/lorem_shy_fl.png"
image lorem shy fl flip = im.Flip("cr/lorem_shy_fl.png", horizontal=True)
image lorem think fl = "cr/lorem_think_fl.png"
image lorem think fl flip = im.Flip("cr/lorem_think_fl.png", horizontal=True)

image ipsum happy fl = "cr/ipsum_happy_fl.png"
image ipsum happy fl flip  = im.Flip("cr/ipsum_happy_fl.png", horizontal=True)
image ipsum normal fl = "cr/ipsum_normal_fl.png"
image ipsum normal fl flip = im.Flip("cr/ipsum_normal_fl.png", horizontal=True)
image ipsum sad fl = "cr/ipsum_sad_fl.png"
image ipsum sad fl flip = im.Flip("cr/ipsum_sad_fl.png", horizontal=True)
image ipsum think fl = "cr/ipsum_think_fl.png"
image ipsum think fl flip = im.Flip("cr/ipsum_think_fl.png", horizontal=True)



init python:
    # This is for dialoge changing for charging the Ixomen Sphere if you've read the book or not
    ryannixomenbook = False

    # These are for defining the status of the Anna3 tests, and overcomming Anna's status abondened being after Lorem 4
    rnagreedannatest = False
    rndidannatest = False
    rncancelannatest = False
    rnannastatus = "none"

    # These are variables for Lorem 6
    # Looking at things in Lorem's apartment
    ryannlookatthings = 0
    ryannlookbooks = False
    ryannlookgames = False
    ryannlookatshelf = 0
    ryannlookplant = False
    ryannlookTV = False
    # Switch from looking at things to asking about them
    ryannaskipsum = False
    ryannaskbooks = False
    ryannaskgames = False
    ryannaskplant = False
    ryannaskTV = False
    ryannlo6ask = 0
    # Switching to would you rather questions
    rnwyrasked = 0
    rnwyraskedlo1 = False
    rnwyraskedlo2 = False
    rnwyraskedlo3 = False
    rnwyraskedip1 = False
    rnwyraskedip2 = False
    rnwyraskedip3 = False
    # Lorem romanece counter
    rnloremromance = 0
    # For extra content if played Casual Vandalism
    ryannwindowssmashed = 0

    # Other random stuff
    ryannmavapology = False
    ryannipsumalarm = False
    ryannpizzatopping = "none"
    ryannplayerdrink = "none"
    
    # For the minigame, joy...

    # For the extra display
    ryannDisplayVar1name = ""
    ryannDisplayVar1 = 0
    ryannDisplayVar1unit = ""
    ryannDisplayVar2name = ""
    ryannDisplayVar2 = ""
    ryannDisplayVar2unit = ""
    # The timer for the minigame
    ryannactionsremaining = 25
    # For the laptop search thing
    ryannsearchterm = ""
    ryannsecretscene = False
    # For items in the minigame
    ryanncurrentitem = "Nothing"
    ryanncrowbarused = False
    ryannwrenchused = False
    ryanntapeused = False 
    ryannhaskey = False 
    ryannhaskeycard = False 
    ryannwrenchlocker = False
    # Things for the pump
    ryannpumpbefore = False
    ryannpumpused = False
    ryannpumpfixed = False
    ryannpumponoff = 0
    ryannvalveatpump = False
    ryannscrewdriveratpump = False
    ryannpumpon = False
    # Other things
    rnunlockedfootlocker = False 
    ryannlookedtable = False
    ryannlookedboxes = False
    ryannmovedboxes = False
    ryannlookedcabinet = False 
    ryannlookedlist = False 




# These are hooking from something to change a veriable

# This is for reading the book on Ixomen Sphere's

label ryann_lorem2_ixomenbook:
    $ ryannixomenbook = True
    jump ryann_lorem2_ixomenbook_return

# This is for fixing a bug in Lorem 5

label ryann_lorem2_spherecharged:
    $ SphereCharged = False
    return

# This is for overcoming Anna’s status being abandoned at the start of Lorem4 

label ryann_lorem2_c5annastatus:
    if rnannastatus == "neutral":
        $ annastatus = "neutral"
    elif rnannastatus == "good":
        $ annastatus = "good"
    elif rnannastatus == "bad":
        $ annastatus = "bad"
    else:
        pass
    return
    
    
label ryann_lorem2_annastatusneutral:
    $ rnannastatus = "neutral"
    return

label ryann_lorem2_annastatusgood:
    $ rnannastatus = "good"
    return

label ryann_lorem2_annastatusbad:
    $ rnannastatus = "bad"
    return
    

# Theres are about the defining the Anna3 tests (If you agreed to, did or canceled doing the tests.) 

label ryann_lorem2_agreeannatest:
    $ rnagreedannatest = True
    return

label ryann_lorem2_didannatest:
    $ rndidannatest = True
    return

label ryann_lorem2_cancelannatest:
    $ rncancelannatest = True
    return 


# Credits for the mod

label ryann_lorem2_credits:

play sound "mx/nostalgia.ogg" 

show ryannlorem2credits with dissolveslow

$ renpy.pause (10.0)

scene black with dissolvemed

show black2 at left with dissolvemed

show loremapt at Pan((200, 0), (700, 0), 25)
show credits1 at right
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits2 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show loremsphere at Pan ((250, 326), (750,0), 24.0)
show credits3 at right
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show meetingipsum at Pan ((-200, 0), (-100,324), 25)
show credits5 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show school at Pan ((200, 252), (700, 302), 25)
show credits7 at right
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show meetinglorem at Pan((90, 0), (90, 408), 25.0)
show credits9 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (9.5)

stop sound fadeout 1.5

$ renpy.pause (1.0)

scene black with dissolvemed

stop sound fadeout 2.5

$ renpy.pause (5.0)


jump ml_main_menu



