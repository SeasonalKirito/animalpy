from animalpy.utils import Utils
utils = Utils()

def cat(type="img"):
    if type == "img":
        return utils._get_img("cat")
    elif type == "gif":
        return utils._get_gif("cat")
    
def dog(type="img"):
    if type == "img":
        return utils._get_img("dog")
    elif type== "gif":
        return utils._get_gif("dog")
    
def fox(type="img"):
    if type == "img":
        return utils._get_img("fox")
    elif type== "gif":
        return utils._get_gif("fox")

def ferret(type="img"):
    if type == "img":
        return utils._get_img("ferret")
    elif type== "gif":
        return utils._get_gif("ferret")
    
def red_panda(type="img"):
    if type == "img":
        return utils._get_img("red_panda")
    elif type== "gif":
        return utils._get_gif("red_panda")
    
def capybara(type="img"):
    if type == "img":
        return utils._get_img("capybara")
    elif type== "gif":
        return utils._get_gif("capybara")
    