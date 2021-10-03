
from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod): 
    name="Lorem Extention Mod"
    version="v0.1"
    author="Ryann1706"
    nsfw=False


    def mod_load(self):
        ml = modinfo.get_mod("MagmaLink").import_ml()

        ml.find_label("menubooks") \
            .search_menu("The Ixomen Sphere and How to Use it").branch() \
            .search_say("Quick start guide") \
            .hook_to("ryann_lorem2_ixomenbook")
        
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


    def mod_complete(self):
        pass
        
