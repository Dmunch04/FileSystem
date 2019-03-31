import platform

if platform.system () == 'Linux':
    from Tkinter import Tk, Label, Button, Text, END, BOTTOM, E, W
else:
    from tkinter import Tk, Label, Button, Text, END, BOTTOM, E, W

from PIL import ImageTk, Image
from functools import partial
import os

# TODO: Display images if file type is: .jpg, .png, etc.
# TODO: Fix UI
# TODO: Optimize
# TODO: Fix path display (Title)

file_extensions = (
    '.txt',
    '.py',
    '.json',
    '.eve',
    '.com',
    '.java',
    '.gaba',
    '.cs',
    '.resx',
    '.config',
    '.lua',
    '.open',
    '.os',
    '.js',
    '.html',
    '.css',
    '.go',
    '.ru',
    '.rb',
    '.png',
    '.jpg',
    '.jpeg',
    '.gif',
    '.pytha',
    '.c',
    '.cpp'
)
image_extensions = (
    '.jpeg',
    '.png',
    '.jpg',
    '.gif'
)

class Directory:
    def __init__ (self, path):
        self.path = path

        self.contents = {}

        for item in os.listdir (path):
            if not item.endswith (file_extensions):
                self.contents[item] = item + ' >'
            else:
                self.contents[item] = item

class DirectoryWindow:
    def __init__ (self, root):
        self.root = root

        title = 'Desktop/'

        self.path = '../'

        self.AddItems (self.path)

        root.title (title)
        root.geometry ('800x600')
        root.resizable (False, False)

    def AddItems (self, path):
        folder = Directory (path)

        for item in folder.contents:
            btn = Button (
                self.root,
                text = str (folder.contents[item]),
                command = partial (self.GoTo, item)
            )
            btn.pack ()

        if len (self.path) > 3:
            btn = Button (
                self.root,
                text = '.. Back',
                command = self.GoBack
            )
            btn.pack ()

    def GoTo (self, item):
        elements = self.root.slaves ()
        for element in elements:
            element.destroy ()

        self.path = os.path.join (self.path, item)
        root.title (self.path.replace ('../', 'Destop/') + '/')

        if item.endswith (file_extensions):
            if item.endswith (image_extensions):
                img = ImageTk.PhotoImage (Image.open (self.path))
                panel = Label (self.root, image = img)
                panel.pack()
            else:
                self.txt = Text (self.root)
                self.txt.pack ()
                self.txt.insert (END, str (open (self.path, 'r').read ()))

            btn_back = Button (
                self.root,
                text = '.. Back',
                command = self.GoBack
            )
            btn_save = Button (
                self.root,
                text = 'Save',
                command = self.SaveFile
            )
            btn_back.pack (side = BOTTOM, anchor = E)
            btn_save.pack (side = BOTTOM, anchor = W)

        else:
            self.AddItems (self.path)

    def GoBack (self):
        elements = self.root.slaves ()
        for element in elements:
            element.destroy ()

        self.path = os.path.dirname (self.path)
        root.title (self.path + '/')

        self.AddItems (self.path)

    def SaveFile (self):
        text = self.txt.get (1.0, 'end-1c')
        with open (self.path, 'w') as file: file.write (text)

root = Tk ()
window = DirectoryWindow (root)
root.mainloop ()
