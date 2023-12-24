from animalpy.utils import Utils
utils = Utils()

class Animals:
    Cat = "cat"
    Dog = "dog"
    Ferret = "ferret"
    Capybara = "capybara"

def _get_animal(animal:None, type="img"):
    if animal == None:
        return("Please give the animal param, ex: Animals.Cat")
    else:
        pass

    if type == "img":
        return utils._get_img(animal)
    elif type == "gif":
        return utils._get_gif(animal)
    