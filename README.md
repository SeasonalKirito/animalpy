## AnimalPY 🐍
AnimalPY is you assistant in recieveing links to images of animals 🤖
## Installation 📩
Tested on Newest Python Versions
There are no requirements needed other then the standard library ✅
```cmd
pip install git+https://github.com/SeasonalKirito/AnimalPY.git
```
This pakage is not on pypi at this moment and will not have a ETA on pypi ⌚
## How it works 💽
AnimalPY is using its content folder as the images for ussage 
and the code gives a random image out of the images and returns the link. 📨
## Usage
To defind and use all its functions you will do this -|
```py
from animalpy import animal_name1, animal_name2, animal_name3
```
to find out the names of the animals go to the content folder in the repository 
and find the folder name of the animal you want to use and put that in the animal_name.
---
Input -
```py
from animalpy import dog
print(dog("img"))
print(dog("gif"))
```
Output -
```cmd
https://raw.githubusercontent.com/SeasonalKirito/AnimalPY/main/content/dog/img/[1].png
https://raw.githubusercontent.com/SeasonalKirito/AnimalPY/main/content/dog/gif/[3].png
```
The type param located in the () in the animal function can only be either "img" or "gif"
