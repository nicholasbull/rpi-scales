import sys
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
    
from PIL import Image, ImageTk
from time import sleep
import random

from weigh import initialise, weigh

image_ba = Image.open("BA.PNG")
image_bi = Image.open("BI.PNG")
image_de = Image.open("DE.PNG")
image_ds = Image.open("DS.PNG")
image_gdao = Image.open("GDAO.PNG")

# No longer need this, import from weigh:
# def weigh():
#     """we'll repurpose this function with the scales weight"""
#     return random.choice([63, 69, 78, 85, 296])


root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

root.attributes('-fullscreen', True)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

canvas = tkinter.Canvas(root,width=w,height=h)
canvas.pack()
canvas.configure(background='black')

def configure_image(unconfigured_image):
    imgWidth, imgHeight = unconfigured_image.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        unconfigured_image = unconfigured_image.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    configured_image = ImageTk.PhotoImage(unconfigured_image)
    return configured_image

hx = initialise()
sleep(2)

while True:
    if root.state() != 'normal':
        # ESC key changes root state becauase of key binding above
        break
    weight = int(weigh(hx))
    
    if weigh() < 65:
        image = configure_image(image_de)
        canvas.create_image(w/2,h/2,image=image)

    elif weigh() < 72:
        image = configure_image(image_ds)
        canvas.create_image(w/2,h/2,image=image)

    elif weigh() < 80:
        image = configure_image(image_bi)
        canvas.create_image(w/2,h/2,image=image)

    elif weigh() < 100:
        image = configure_image(image_ba)
        canvas.create_image(w/2,h/2,image=image)

    else:
        image = configure_image(image_gdao)
        canvas.create_image(w/2,h/2,image=image)

    root.update_idletasks()
    root.update()
    sleep(1)
