import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from imageSelector import imageSelectorManager

import os

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        #self.root = tk.Tk()
        self.title("Photo Sort")
        self.create_window()
        self.create_widgets()
        self.create_logo()

    def create_window(self):
        # create a new window

        self.canvas = tk.Canvas(self)
        # set the size of the window
        self.canvas.config(width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        # paint the row 1 in the canvas with the color #20bebe
        self.canvas.create_rectangle(0, 0, self.winfo_screenwidth(), 100, fill="#20bebe")
        self.canvas.grid(columnspan=self.winfo_screenwidth(), rowspan=self.winfo_screenheight(),sticky="nsew")
        # ability to responsive the widgets in the canvas
       # self.canvas.pack(fill='both', expand=True)
        #self.canvas.bind('<Configure>', self.on_resize)


    def create_widgets(self):
        # create a choose folder button
        self.create_choose_folder_btn()

    def create_choose_folder_btn(self):
        #browse button
        button_text = tk.StringVar()
        self.chooseFolderBtn = tk.Button(self, textvariable=button_text, command=lambda:self.select_folder(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        button_text.set("Browse")
        self.chooseFolderBtn.grid(column=1, row=2)

    def create_logo(self):
        # create a logo
        # openn logo.png from the GUI folder
        self.logo = Image.open(os.path.join(os.path.dirname(__file__),"logo.png"))

        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.grid(column=1, row=0)
        # resize the logo to fit the canvas
        #self.canvas.create_image(0, 0, image=self.logo, anchor='nw')


    def select_folder(self):
        # save the path of the selected folder
        self.folder_path = filedialog.askdirectory()
        # get all the images in the selected folder
        self.get_images_in_folder()
        # stop the main loop and return the path of the selected folder
        i=imageSelectorManager.imageSelectorManager(self.folder_path,self.images_path)

#==============================================================================
    def get_images_in_folder(self):

        self.images_path = []
        for root, dirs, filenames in os.walk(self.folder_path):
            for filename in filenames:
                if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                    self.images_path.append(filename)
                #files.append(os.path.join(root, filename))



def run():
    app = App()
    app.mainloop()




