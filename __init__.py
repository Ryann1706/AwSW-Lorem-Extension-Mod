
from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod): 
    name="Lorem Ipsun't"
    version="v1.0"
    author="Ryann1706"
    nsfw=False
    dependencies = ["MagmaLink"]


    def mod_load(self):
        ml = modinfo.get_mod("MagmaLink").import_ml()

        # These are for changing Lorem's 4th date and the Reza confrontation
        ml.find_label("menubooks") \
            .search_menu("The Ixomen Sphere and How to Use it").branch() \
            .search_say("Quick start guide") \
            .hook_to("ryann_lorem2_ixomenbook")
        
        ml.find_label("lorem2") \
            .search_if("annadead == False", depth=550).branch() \
            .search_say("Yes, but that makes me wonder: [player_name], did you agree to visit her and undergo her rigorous testing regimen?") \
            .hook_to("ryann_lorem2_lo2change") \
            .search_say("Oh, and Lorem: Have you seen my Ixomen Sphere recently?") \
            .link_from("ryann_lorem2_lo2change_end")
        
        ml.find_label("lorem4") \
            .search_say("In the eyes of some, that makes me a freak of nature. Something that needs fixing, or shouldn't exist in the first place.", depth=600) \
            .hook_to("ryann_lorem2_lorem4change") \
            .search_menu("I don't mind.").branch() \
            .search_say("You know, it's not always the bullies who go after me once they know.") \
            .link_from("ryann_lorem2_lorem4change_end")

        ml.find_label("lorem4") \
            .search_say("See ya.", depth=700) \
            .hook_to("ryann_lorem2_spherecharge") \
            .search_python("renpy.pause (2.0)") \
            .link_from("ryann_lorem2_spherecharge_end")

        ml.find_label("lorem5") \
            .search_say("They belong to humanity!") \
            .hook_to("ryann_lorem2_rezaconfrontation", condition="SphereCharged == True")

        # These are defining variables for the tests in Anna3 
        # Agreeing to do the tests
        ml.find_label("anna1skip") \
            .search_say("Just look at that, I won.") \
            .hook_call_to("ryann_lorem2_agreeannatest")

        ml.find_label("cont4") \
            .search_if("annaanswers == 3").branch_else() \
            .search_say("And in a twist of fate that shocked no one, Anna, the magnificent, won the game.") \
            .hook_call_to("ryann_lorem2_agreeannatest")

        ml.find_label("cont4") \
            .search_if("annaanswers == 3").branch() \
            .search_say("Well, it appears to me that our game has ended in a tie.") \
            .hook_call_to("ryann_lorem2_agreeannatest")

        ml.find_label("c3fac") \
            .search_if("annasurvives == False").branch_else() \
            .search_if("annastatus == \"none\"").branch() \
            .search_menu("Sure.", depth=450).branch() \
            .search_say("Oh, great. In that case, I could make time for a few of your questions.") \
            .hook_call_to("ryann_lorem2_agreeannatest")

        # Canceling the test because lab was raided
        ml.find_label("c4facility") \
            .search_if("annasurvives == True").branch() \
            .search_if("annastatus == \"good\"").branch_else() \
            .search_say("Also, it doesn't look like I'll be able to do those tests on you any longer, so don't bother contacting me again.") \
            .hook_call_to("ryann_lorem2_cancelannatest", condition= "rnagreedannatest == True") 

        # Actually doing the tests
        ml.find_label("anna3") \
            .search_say("There you are. I was wondering if you'd even show up.") \
            .hook_call_to("ryann_lorem2_didannatest") 
        
        # These are overcoming Anna's status being abononed at the start of chapter 5
        ml.find_label("anna3skip") \
            .search_if("anna3mood >= 8").branch() \
            .search_say("I wouldn't mind staying for a bit longer.") \
            .hook_call_to("ryann_lorem2_annastatusgood")

        ml.find_label("anna3skip") \
            .search_if("anna3mood >= 8").branch_else() \
            .search_say("Sure. Thanks for having me.") \
            .hook_call_to("ryann_lorem2_annastatusneutral")

        ml.find_label("anna3") \
            .search_if("anna3mood <= 2", depth=1300).branch() \
            .search_say("We're done here. Get out.") \
            .hook_call_to("ryann_lorem2_annastatusbad")

        ml.find_label("chapter5") \
            .search_say("After a night of turbulent dreams, my consciousness returned to the shores of the waking world.", depth=450) \
            .hook_call_to("ryann_lorem2_c5annastatus", condition= "anna4unplayed == True")


    def mod_complete(self):
        pass

