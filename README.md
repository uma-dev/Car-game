# Car-game

## Overview

Little classic car game using [pygame](https://www.pygame.org/news) modules on **Python**. 
This is a first look into 2D simple games and a easy **introduction to programming** for kids. 
The code was written with a FP _programming paradigm_ in order to ilustrate it's characteristics but it could be rewritten using the _OOP paradigm_. Keep in mind that it would require more code, more knowledge (wich is not the scope of this project) but it'll be more scalable and maybe more legible.
Hope you enjoy!

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/uma-dev/Car-game/blob/master/raceCar2.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/uma-dev/Car-game/blob/master/raceCar.png">
  <img alt="Shows two types of cars upon the theme" src="https://github.com/uma-dev/Car-game/blob/master/raceCar.png">
</picture>
</p>

##  How to use it 

### What you need
This program only needs a computer with **python** and **pygame** installed, If you don't know how to do it, here are some examples that can help. 
<p align="center">
	<img alt="Race.py" src="https://user-images.githubusercontent.com/22565959/213778656-6eb6b171-4fac-4513-acab-e979311e582b.png">
</p>

- Python 
  - [Installing Python on Windows](https://learn.microsoft.com/en-us/windows/python/beginners)
  - [Installing Python on Linux](https://docs.python-guide.org/starting/install3/linux/)
  
- Pip 
  - [Pip Installation](https://pip.pypa.io/en/stable/installation/)
  
- Pygame 
  - [Getting started with Pygame](https://www.pygame.org/wiki/GettingStarted) 

### Executing
  As easy as it is, if you have not executed any python script before, take a look to the following tutorial:
  - [Execute Python scripts](https://pythonbasics.org/execute-python-scripts/)
  - After going to the `root` folder of the proyect type

  ```
  python3 Race.py 
  ```
<p align="center"> 
	<img alt="Race.py" src="https://user-images.githubusercontent.com/22565959/213778425-4bfe8d48-25f5-4d27-bf7a-d6d28a94cc0f.png">
</p>

### Adding more levels
  
  The blocks move to the car and also increase their lenght and also speed, as you can see above in the **thing_width** and **thing_speed** incremments. 
  You can set wathever values and conditions you want to customize the level changes.
  
  ```
    if score % 5 == 0 and score < 20:
				thing_speed += 0.8
				thing_width += (score * 1.19)
			if score > 20 and score %10 == 0:
				thing_speed += 0.3
				thing_width += (score)
			if score > 90:
				pygame.mixer.Sound.play (magic)
  ```
<p align="center"> 
	<img alt="Race.py" src="https://user-images.githubusercontent.com/22565959/213778562-2d267fe4-5cad-4be6-8729-b1bb30db2663.png">
</p>
 
  The above conditions were setted to make almost imposible to pass the **100** score in levcel 1, **85** in level 2 and **69** in level 3, so if you do it, the car picture change to a better image as you can see in the following code:
   ```
   if score > 99 and level == 1 or score >85 and level == 2 or score > 69 and level == 3:
			animation ("¡New Car!")
			carImg = pygame.image.load ("raceCar2.png")
			skyBlue = (120,195,255)
			block = (5,70,20)
			wins += 1
   ```
   
  Feel free to add the values and conditions you want, and make the most out of it!
