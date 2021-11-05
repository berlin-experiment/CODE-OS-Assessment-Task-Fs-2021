# Stacey Kenny OS_01 Introduction to Software Engineering Assessment Task

I have built - or rather half built - a DUNE inspired space invader game rather than a basic one using pygame, online YouTube tutorials and a lot of caffeine and crying.

While we were shown how to download VS Code, I prefer to use PyCharm and did so for this task.


* All images were drawn by me using [Photoscape X](http://x.photoscape.org/) and pure talent.
** PS. My pygame assessment is inspired by DUNE by Frank Herbert and the names in the game are just Arabic translations to avoid copyright infringement.

## The Code


While some things may appear familiar, others I adapted to make the project more unique and personal to myself.

The Game is nowhere near complete, butI have tried to focus on structuring the game and code in a way I feel makes more sense and easier to follow, based on what I have seen on Stackoverflow and watch tutorials online.


```python
import sys
import pygame

from .general.settings.settings import Settings
from .general.bg import Background
from .player.alyaesub import Alyaesub
from .intruders.dakhil import CreateFleet
from .general.bullet import PewPew
```

## References
I used the following to better my understanding of Python, PyGame and Coding Concepts to be able to build the game.

1. Coding With Russ. (2021). Pygame Space Invaders Beginner Tutorial in Python - PART 1 | Initial Setup [Image]. Retrieved 29 October 2021, from https://www.youtube.com/watch?v=f4coFYbYQzw&t=20s.
2. Hamedani, M. (2019). Python Tutorial - Python for Beginners [Full Course]. YouTube. Retrieved October 28, 2021, from https://www.https://www.youtube.com/watch?v=_uQrJ0TkZlc&amp;t=11763syoutube.com/watch?v=_uQrJ0TkZlc&amp;t=11763s.
3. Matthes, E. Python Crash Course, 2nd Edition (2nd ed., pp. 1-181, 224-278). No Starch Press, Inc.
