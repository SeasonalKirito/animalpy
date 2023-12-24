from animalpy import _get_animal, Animals
import time

while True:
    print(_get_animal(Animals.Dog, "img"))
    print(_get_animal(Animals.Dog, "gif"))

    time.sleep(1)