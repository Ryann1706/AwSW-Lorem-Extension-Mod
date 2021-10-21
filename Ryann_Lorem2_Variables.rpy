
# This file is for variables and defining stuff, so kinda just ignore this one.


define Rn = Character(_("Ryan"), color="#008000")


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



# These are hooking from something to change a veriable

# This is for reading the book on Ixomen Sphere's

label ryann_lorem2_ixomenbook:
    $ ryannixomenbook = True
    jump ryann_lorem2_ixomenbook_return

# This is for overcoming Anna’s status being abandoned at the start of Lorem4 

label ryann_lorem2_lo4annastatus:
    if rnannastatus == "neutral":
        $ annastatus = neutral
    elif rnannastatus == "good":
        $ annastatus = good
    elif rnannastatus == "bad":
        $ annastatus = bad
    else:
        pass
    jump ryann_lorem2_lo4annastatusreturn

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
    Rn "Heya Eval buddy."
    Rn "I really appreciate you looking through my mod for me."
    Rn "I appreciate it so much I handpicked a song for this next scene just for you."
    Rn "Hope you enjoy."
    scene o4 with dissolveslow
    play music "mx/funness.ogg"
    $ renpy.pause (10.0)
    stop music fadeout 2.0
    scene black 
    Rn "Just kidding, im not that cruel."
    Rn "(Hopefully no one looks through the code and finds this.)"
    jump ryann_lorem2_lorem6

