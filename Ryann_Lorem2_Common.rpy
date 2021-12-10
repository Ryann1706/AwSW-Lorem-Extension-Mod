
# This file is for variables and defining stuff, so kinda just ignore this one.


define Rnn = Character(_("Ryan"), color="#008000")

# For extra backgrounds
image ryannfacilitylab = "bg/ryannfacilitylab.jpg"
image ryannkitchen = "bg/ryannkitchen.jpg"
image ryannundergroundlab = "bg/ryannundergroundlab.jpg"


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
    WindowSmashed = False

    # Other random stuff
    ryannmavapology = False
    ryannipsumalarm = False
    
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






# Dont look at this next part unless you're Eval, or do im just text I cant stop you


label ryann_lorem2_spiteeval:
    Rnn "Heya Eval buddy."
    Rnn "I really appreciate you looking through my mod for me."
    Rnn "I appreciate it so much I handpicked a song for this next scene just for you."
    Rnn "Hope you enjoy."
    scene o4 with dissolveslow
    play music "mx/funness.ogg"
    $ renpy.pause (10.0)
    stop music fadeout 2.0
    scene black 
    Rnn "Just kidding, im not that cruel."
    Rnn "(Hopefully no one looks through the code and finds this.)"
    jump ryann_lorem2_lorem6

