import os
from glob import glob
from watchdog.observers import Observer
from watchdog.events import FileCreatedEvent, FileModifiedEvent, FileSystemEventHandler
import random

app_dir = os.path.dirname(os.path.realpath(__file__))
media_dir = "./pi/"

# filechages handler
media_files = []




import tkinter
app = tkinter.Tk()
app.geometry(newGeometry="600x600")

tk = tkinter.Frame(app)

from PIL import Image, ImageTk
import math






oldframe = None
def open_url(url):
    global oldframe, tk, app

    
    win = tkinter.Frame(tkinter.Toplevel(app))

    image=  Image.open(url)
    mw, mh = 800, 600
    w, h  = image.size
    wd = w - mw
    hd  = h - mh
    m = 1
    if wd <= 0 and hd <= 0:
        pass
    elif wd > hd:
        m = mw/ w
    else:
        m = mh / h
    w =  int(m * w)
    h = int(m * h)
    image = image.resize((w, h))
    photo = ImageTk.PhotoImage(image)
    x = tkinter.Label(win, image = photo)
    x.image = photo
    x.pack()

    win.pack()
    oldframe = win

def draw():
    global tk, media_files
    r =  math.ceil(len(media_files) / 6 )
    tk.destroy()
    # tk.pack()
    tk = tkinter.Frame(app)
    for i in range(r):
        for j in range(6):
            def do():
                try:
                    image = Image.open(media_files[i * 6 + j])
                except:
                    return False
            
                image=  image.resize((100, 100))
                photo = ImageTk.PhotoImage(image)
                x = tkinter.Label(tk, image = photo)
                x.grid(row = i, column = j)
                x.width = 100
                x.height  = 100
                x.image = photo
                path = media_files[i * 6 + j]
                x.bind("<Button-1>",lambda e,url=None:open_url(path))
                # x.pack()
                return True
            if not do():
                break
    tk.pack()




def handleChanges(event):
    global media_files, media_hash
    exts = ['*.png', '*.jpg', '*.jpeg']
    media_files = []
    for ext in exts:
        media_files.extend(glob(media_dir + ext))
    media_files.sort(key = os.path.getmtime)
    media_files.reverse()
    draw()

handleChanges(0)

handler = FileSystemEventHandler()
handler.on_created = handleChanges
handler.on_modified = handleChanges
observer = Observer()
observer.schedule(handler, media_dir)
observer.start()




# tk.pack()
app.mainloop()