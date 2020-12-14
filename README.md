# pylcanim

<br>pylcanim is a simple library for playing animations made with sprite factory</br>
<br>(https://github.com/craftworkgames/SpriteFactory)</br>

## Installation of pylcanim library
<br>To install from pypi with pip</br>
```
pip install pylcanim
```
## Downloading SpriteFactory

<br>You can directly download the executable(note: At this point this is windows only).</br>
<br>From: https://craftworkgames.itch.io/sprite-factory</br>
<br>Or build it yourself</br>
<br>From: https://github.com/craftworkgames/SpriteFactory</br>

## Using SpriteFactory

<br>You can see this video https://www.youtube.com/watch?v=DnWvmI1qBAs (time stamp in description).</br>
<br>But the video is not pygame oriented(I will make one about it later)</br>

## Using the library

import the pylcanim into your project with

```py
from pylcanim import pylcanim
```
Then initialize the library with
```py
pylcanim.init('Path/To/Your/SpriteFactoryFile.sf')

```

In your main loop write
```py
image=pylcanim.lcAnim(fpscount,row)
```
Where 
```
fpscount is an integer which determines how fast your animation should run(0 is fastest and becomes slower increasingly)
```
and
```
row is the row number in which your sprite is situated(default=0 for single line spritesheets)
```
## An entire Example

```py
import pygame
from pylcanim import pylcanim as p

(width,height)=(300,200)
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height))
pygame.display.flip()
running=True
p.init('run.sf')
while running:
    image =p.lcAnim(3,0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:

            running=False
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 50))
    pygame.display.update()

    clock.tick(60)
pygame.quit()

```
