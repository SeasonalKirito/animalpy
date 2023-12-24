## AnimalPY 🐍
AnimalPY is your assistant in recieveing links to images of animals 🤖
## Installation 📩
Tested on Newest Python Versions, 
There are no requirements needed other then the standard library ✅
```cmd
pip install git+https://github.com/SeasonalKirito/AnimalPY.git
```
This pakage is not on pypi at this moment and will not have a ETA on pypi ⌚
## How it works 💽
AnimalPY is using its content folder as the images for ussage 
and the code gives a random image out of the images and returns the link. 📨
## Usage
To define and use all its functions you will do this -|
```py
from animalpy import _get_animal, Animals
```
 
---
 
Input - 🔤
```py
from animalpy import _get_animal, Animals

print(_get_animal(Animals.Dog, "img"))
print(_get_animal(Animals.Dog, "gif"))
```
Output - 🔢
```cmd
https://raw.githubusercontent.com/SeasonalKirito/animalpy/main/content/dog/img/[4].png
https://raw.githubusercontent.com/SeasonalKirito/animalpy/main/content/dog/gif/[1].gif
```
The type param located in the () in the animal function can only be either "img" or "gif" 💾
