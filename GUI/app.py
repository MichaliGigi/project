import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from imageSelector import imageSelectorManager

import os

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Photo Selector")
        self.create_window()
        self.create_widgets()
        #self.create_logo()

    def create_window(self):

        # Open an image file
        im = Image.open(os.path.join(os.path.dirname(__file__),"background.png"))
        # Convert the image to a PhotoImage object
        self.backgroundImage = ImageTk.PhotoImage(im)

        # Create a canvas widget
        self.canvas = tk.Canvas(self, width=im.width, height=im.height)
        #self.canvas.pack()
        self.canvas.grid(row=0,column=0,columnspan=6,rowspan=6,sticky="nsew")
        # set the background image
        self.canvas.create_image(0, 0, image=self.backgroundImage, anchor='nw')


        # Create an image item on the canvas and set the image to the PhotoImage object
        #self.canvas.create_image(0, 0, image=self.backgroundImage) #, anchor='nw'

        """# set the size of the window
        self.canvas.config(width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        # paint the row 1 in the canvas with the color #20bebe
        self.canvas.create_rectangle(0, 0, self.winfo_screenwidth(), 100, fill="#20bebe")
        self.canvas.grid(columnspan=self.winfo_screenwidth(), rowspan=self.winfo_screenheight(),sticky="nsew")
        # ability to responsive the widgets in the canvas
       # self.canvas.pack(fill='both', expand=True)
        #self.canvas.bind('<Configure>', self.on_resize)"""


    def create_widgets(self):
        # create a choose folder button
        self.create_choose_folder_btn()
        self.create_start_btn()
        self.create_cancel_btn()

    def create_choose_folder_btn(self):
        #browse button
        #button_text = tk.StringVar()
        #self.chooseFolderBtn = tk.Button(self, textvariable=button_text, command=lambda:self.select_folder(), font="Raleway", bg="#cd008e", fg="white", height=2, width=15,borderwidth=5)
        im=Image.open(os.path.join(os.path.dirname(__file__),"buttonSelect.png"))
        self.buttonSelect = ImageTk.PhotoImage(im)
        #button_text.set("Selecte Images Folder")
        self.chooseFolderBtn = tk.Button(self,command=lambda:self.select_folder(),image=self.buttonSelect,borderwidth=0)
        self.chooseFolderBtn.grid(column=3, row=3)
    def create_start_btn(self):
        im = Image.open(os.path.join(os.path.dirname(__file__), "startButton.png"))
        self.buttonStart = ImageTk.PhotoImage(im)
        self.startBtn = tk.Button(self, image=self.buttonStart,borderwidth=0)
        self.startBtn.grid(column=3,row=4)


    def create_cancel_btn(self):
        im = Image.open(os.path.join(os.path.dirname(__file__), "cancelButton.png"))
        self.buttonCancel = ImageTk.PhotoImage(im)
        self.cancelBtn = tk.Button(self, image=self.buttonCancel,borderwidth=0)
        self.cancelBtn.grid(column=4, row=4)

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




