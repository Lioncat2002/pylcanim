import pygame
import json

pygame.init()

c=0
fps=0
def lcAnim(sfile,fpslimit=2,animpos=0):
    global c,fps
    fps+=1
    with open(sfile) as f:
        data=json.load(f)

    width=data['textureAtlas']['regionWidth']
    height = data['textureAtlas']['regionHeight']
   # print(width)
    img=pygame.image.load(data['textureAtlas']['texture'])
    if c>=len(data['cycles']['animation0']['frames']):
        c=0
    if c<len(data['cycles']['animation0']['frames']):
        img.set_clip(pygame.Rect(data['cycles']['animation0']['frames'][c-1]*width,animpos*height,width,height))  # Locate the sprite you want
        draw_me = img.subsurface(img.get_clip())  # Extract the sprite you want
        if(fps>fpslimit):
            c =c+1
            fps=0
        #print(c)
        return draw_me


