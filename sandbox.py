# Let's read an example XML slide file.

import struct

import pygame
pygame.init()
pygame.font.init()


from lxml import etree

doc = etree.fromstring(open("examples/barebones.xml",'r').read())


# The width of the slide (in pixels). Since the slide defines its height/width ratio
# this then fixes the height.
slidewidth = 1000


color_presets = {"white":(255,255,255),
                 "black":(0,0,0)}

def html_to_pygame_color(htmlcol):
    """ Given a colour defined in HTML style (e.g. #00ff11) convert it into the colour
    format pygame likes. """
    htmlcol=htmlcol.strip()
    if htmlcol in color_presets:
        return color_presets[htmlcol]
    if htmlcol[0]=="#": htmlcol=htmlcol[1:]
    print(htmlcol)
    return struct.unpack('BBB',bytes.fromhex(htmlcol))





def slide_coords(x,y,slidedims):
    """ 
    Return the pixel coordinates corresponding to (x,y) on the slide. 
    By convention, (x,y) is expressed as a proportion of the slide width and height, respectively.
    """
    return (int(round(float(x)*slidedims["w"])),
            int(round(float(y)*slidedims["h"])))



def get_font(name,size,slidedims):
    """ Get the font object in question. """
    return pygame.font.Font(name+".ttf",int(size*slidedims["w"]))




# Set the defaults
defaults = {}
defa = doc.xpath('//slideshow/default')
for d in defa:
    for k in d.attrib:
        defaults[k]=d.attrib[k]


        
# Read the slides
slides = []
sl = doc.xpath('//slideshow/slide')
for s in sl:
    # Get the slide attributes
    slideattribs = s.attrib

    w = slidewidth
    h = int(round(slidewidth*float(slideattribs["ratio"])))
    slidedims = {"w":w,"h":h}
    
    surf = pygame.Surface((w,h))
    surf.fill(html_to_pygame_color(slideattribs["background"]))
    
    boxes = s.xpath('content/box')
    for b in boxes:
        box = b.attrib

        if box["type"]=="rect":
            xr,yr,wr,hr=float(box["x"]),float(box["y"]),float(box["w"]),float(box["h"])
            x ,y =slide_coords(xr,yr,slidedims)
            xe,ye=slide_coords(xr+wr,yr+hr,slidedims)
            pygame.draw.rect(surf,html_to_pygame_color(box["fill"]),(x,y,xe-x,ye-y))

        if box["type"]=="text":
            xr,yr = float(box["x"]),float(box["y"])
            x ,y =slide_coords(xr,yr,slidedims)
            fnt = get_font(box["font"],float(box["size"]),slidedims)
            textsurf = fnt.render(box["text"],True,html_to_pygame_color(box["color"]))
            surf.blit(textsurf,(x,y))
            
            #pygame.draw.rect(surf,html_to_pygame_color(box["fill"]),(x,y,xe-x,ye-y))


            
    pygame.image.save(surf,"slide.bmp")
    



    

pygame.font.quit()
pygame.quit()
