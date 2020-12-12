# pylcanim

<br>pylcanim is a simple library for playing animations made with sprite factory</br>
<br>(https://github.com/craftworkgames/SpriteFactory)</br>

## Installation of pylcanim library
<br>To install from pypi with pip</br>
```
pip install pylcanim
```
## Downloading SpriteFactory

You can directly download the executable(note: At this point this is windows only)
From: https://craftworkgames.itch.io/sprite-factory
Or build it yourself
From: https://github.com/craftworkgames/SpriteFactory

## Using SpriteFactory

You can see this video https://www.youtube.com/watch?v=DnWvmI1qBAs (time stamp in description)
But the video is not pygame oriented(I will make one about it later)

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
