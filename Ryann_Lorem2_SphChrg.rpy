
init python:
    ryannixomenbook = False

label ryann_lorem2_spherecharge:

$ renpy.pause (0.3)
hide lorem with dissolve
play sound "fx/door/doorclose3.wav"
$ renpy.pause (1.5)

# Dont really like this, will rewrite at some point.
play sound "fx/spheretake.ogg"
m "I went to move Ipsum's Ixomen Sphere so I wouldn't accidentally damage it, but when I picked it up, I noticed it was still unlocked."
play sound "fx/sphereboot.ogg"
m "I saw some of the features Lorem has shown me earlier, but the main thing I saw was an obnoxious flashing battery symbol."
c "(Huh, Lorem must have forgotten to put it back on the charger after showing off the other things it could do.)"

menu:
    "[[Leave it alone.]":
        $ SphereCharged = False
        m "I decided it wasn't a good idea to try and charge it since I didnt properly understand how it worked."
        if  ryannixomenbook == True:
            m "And I didn't really want to read through that book about Ixomen Spheres again."
        else:
            pass

    "[[Charge the sphere.]":
        $ SphereCharged = True
        if ryannixomenbook == True:
            play sound "fx/sphereslide.ogg"
            m "I remembered about the book I saw about Ixomen Spheres, and after skimming through the start-up guide I got it to start charging."
        else:
            play sound "fx/sphereslide.ogg"
            m "I tried to put the sphere on the charger, and after struggeling to get it working for a few seconds, I got it to start charging."

# Felt wrong not having a line here, want to change this, but right now its better than nothing.
m "After that, I settled down and got ready for bed."


stop music fadeout 2.0

$ loremscenesfinished = 4

jump ryann_lorem2_spherecharge_end
